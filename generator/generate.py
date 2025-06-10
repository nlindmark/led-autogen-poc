# generator/generate.py

import hashlib
import pathlib
from jinja2 import Environment, FileSystemLoader
import importlib
import autogen.decorators as deco

ROOT = pathlib.Path(__file__).parent.parent
TEMPLATES = ROOT / "templates"
OUT_DIR = ROOT / "generated"

def main(spec_module: str):
    # load the spec
    mod = importlib.import_module(spec_module)
    # find the one class with a ._spec
    spec = None
    for attr in dir(mod):
        obj = getattr(mod, attr)
        if hasattr(obj, "_spec"):
            spec = obj._spec
            break
    if spec is None:
        raise RuntimeError("No @c_module found in " + spec_module)

    OUT_DIR.mkdir(exist_ok=True)

    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), trim_blocks=True, lstrip_blocks=True)
    for tmpl_name in ("module.h.j2", "module.c.j2"):
        tmpl = env.get_template(tmpl_name)
        rendered = tmpl.render(module=spec)
        sha = hashlib.sha256(rendered.encode()).hexdigest()
        content = f"// AUTOGEN_SHA256:{sha}\n" + rendered
        out_name = tmpl_name.replace("module", spec["name"]).replace(".j2", "")
        path = OUT_DIR / out_name
        path.write_text(content)
        print("Wrote", path)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
