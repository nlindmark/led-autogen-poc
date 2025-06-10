# LED-Autogen-PoC

Minimal Python-decorator-driven C code generator + Python simulator.

## Prerequisites

- Anaconda or Miniconda  
- Git  

## Quick Start

```bash
git clone git@github.com:<your-org>/led-autogen-poc.git
cd led-autogen-poc

# 1. Create and activate Conda env
conda create -n led-gen-poc python=3.11 -y
conda activate led-gen-poc

# 2. Install generator
pip install -r requirements.txt

# 3. Generate C
python generator/generate.py specs.led

# 4. Inspect generated/*.h & *.c

# 5. Run Python sim
python sim/run.py


## Project Layout

led-autogen-poc/
├── autogen/               # Python decorators & registry
├── specs/                 # Python-based module specs
├── templates/             # Jinja2 templates for C
├── generator/             # Harness that loads specs, renders templates
├── sim/                   # Python “hardware” simulator
├── generated/             # Auto-generated C code (do not edit)
├── requirements.txt
└── .github/               # CI: regen + drift check + sim



## Workflow
Edit only your specs/*.py with @c_module / @c_function.
Run python generator/generate.py specs.<module> to update C code.
Commit both specs and generated code (CI will catch any drift).
Simulate behavior instantly in Python via sim/run.py.
All .h/.c files carry an SHA-256 checksum comment. Any manual edits will cause CI to fail.