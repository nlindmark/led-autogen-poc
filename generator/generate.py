import sys, yaml, hashlib, pathlib
from jinja2 import Environment, FileSystemLoader
from jsonschema import validate, ValidationError

root = pathlib.Path(__file__).parent.parent
env  = Environment(loader=FileSystemLoader(root / "templates"))

def main(spec_path):
    spec = yaml.safe_load(open(spec_path))
    schema = yaml.safe_load(open(root / "schema" / "function.yaml"))
    for fn in spec["functions"]:
        validate(fn, schema)       # fail fast if spec is wrong

    out_dir = root / "generated"
    out_dir.mkdir(exist_ok=True)

    for tmpl_name in ("module.h.j2", "module.c.j2"):
        tmpl = env.get_template(tmpl_name)
        code = tmpl.render(**spec)
        sha  = hashlib.sha256(code.encode()).hexdigest()
        code = f"// AUTOGEN_SHA256:{sha}\n" + code
        out_file = out_dir / tmpl_name.replace(".j2", "").replace("module", spec["module"]["name"])
        out_file.write_text(code)
        print("Wrote", out_file)

if __name__ == "__main__":
    main(sys.argv[1])
