# LED-Autogen-POC

Minimal schema-driven C code generator + Python simulator.

## Prerequisites

- [Anaconda or Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed
- Git

## Quick Start with Conda

1. **Clone the repo**

   ```bash
   git clone git@github.com:<your-org>/led-autogen-poc.git
   cd led-autogen-poc

2. **Create & activate the Conda environment**


conda create -n led-gen-poc python=3.11
conda activate led-gen-poc


3. **Install Python dependencies**


pip install -r requirements.txt

4. **Generate the C code from the spec**


python generator/generate.py specs/led_toggle.spec.yml


5. **Run the Python simulator**


python sim/run.py


## Repo Layout


├── schema/                # YAML schemas (function, etc.)
├── specs/                 # Module specs (*.spec.yml)
├── templates/             # Jinja2 templates for C, headers, CI
├── generator/             # Python code-gen script
├── sim/                   # Python “hardware” simulator
├── generated/             # Auto-generated C code (do not edit)
└── .github/workflows/ci.yml

## Development Workflow

Edit only the schema/, templates/, or specs/ files.

Run python generator/generate.py … to re-generate all C artifacts.

Commit both the updated spec and regenerated code (CI will reject drift).

Push to GitHub & open a PR; CI will validate schemas, regen, lint, and simulate.

