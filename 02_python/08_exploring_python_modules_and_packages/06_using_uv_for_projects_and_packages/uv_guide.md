# 08 - Exploring Python Modules and Packages

**Topic:** Using uv for Project and Package Management
**File:** `06_using_uv_for_projects_and_packages/uv_guide.md`
**Author:** Mrinmoy Shib
**Date:** 2026
**Repository:** fullstack-webdev-python-django-react-ai

---

## What is `uv`?

`uv` is a modern, extremely fast replacement for `pip` + `venv` +
`pip-tools`, built in Rust. It performs the same job — installing packages
and managing isolated project environments — but faster, and with fewer
commands to remember.

`pip` and `uv` are not mutually exclusive; many teams still rely on `pip`.
`uv` is worth learning because it is quickly becoming the default
recommendation across the Python community for new projects.

## Installing `uv`

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or, if pip is already available:
pip install uv
```

## Starting a new project

```bash
uv init my_project
cd my_project
```

This creates a folder structured as follows:

```
my_project/
├── .python-version
├── README.md
├── pyproject.toml
└── main.py
```

`pyproject.toml` is the modern, standard file that describes a Python
project — its name, its dependencies, and its required Python version — all
in one place. An example after adding a couple of packages:

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.32.3",
    "python-dotenv>=1.0.1",
]
```

## Adding packages (replaces `pip install`)

```bash
uv add requests
uv add python-dotenv
```

This performs three actions at once:
1. Installs the package into an isolated virtual environment (`.venv/`)
   that `uv` creates and manages automatically.
2. Adds it to `pyproject.toml` so anyone opening the project knows exactly
   what it requires.
3. Writes a `uv.lock` file that pins the exact version installed, so the
   project behaves identically on every machine it runs on.

## Removing a package

```bash
uv remove requests
```

## Running code (replaces "activate venv, then run script")

```bash
uv run main.py
```

`uv run` automatically locates and uses the project's `.venv` — no manual
`source .venv/bin/activate` step is required. This is the single biggest
quality-of-life improvement over the pip + venv workflow.

## Recreating a project on another machine

Anyone who clones the repository can rebuild the exact same environment
with:

```bash
uv sync
```

This reads `pyproject.toml` and `uv.lock`, then installs precisely the
packages and versions the project was built with.

## Comparison with the pip + venv workflow

| Task                            | pip + venv                          | uv                    |
|----------------------------------|--------------------------------------|-----------------------|
| Create isolated environment      | `python -m venv venv`               | done automatically    |
| Activate environment              | `source venv/bin/activate`          | not needed (`uv run`) |
| Install a package                 | `pip install requests`              | `uv add requests`     |
| Remove a package                  | `pip uninstall requests`            | `uv remove requests`  |
| Record dependencies               | `pip freeze > requirements.txt`     | done automatically    |
| Recreate environment elsewhere    | `pip install -r requirements.txt`   | `uv sync`             |
| Run a script                       | `python main.py` (after activating) | `uv run main.py`      |

## Key Takeaways

- `uv` is a faster, all-in-one replacement for pip + venv + requirements.txt.
- `uv init` starts a new project with a `pyproject.toml` already configured.
- `uv add <package>` installs and records a dependency in a single step.
- `uv run <file>` runs a script inside the project's environment without a
  manual activation step.
- `uv sync` rebuilds another machine's exact environment from
  `pyproject.toml` and `uv.lock` — this is what makes projects reproducible.
- `pyproject.toml` and `uv.lock` should be pushed to GitHub. The `.venv/`
  folder should not be — it belongs in `.gitignore`.

Official documentation: https://docs.astral.sh/uv/
