# 08 - Exploring Python Modules and Packages

**Repository:** fullstack-webdev-python-django-react-ai
**Author:** Mrinmoy Shib
**Date:** 2026

## Topics Covered

| # | Topic | Folder |
|---|-------|--------|
| 1 | Creating and Using Modules | `01_creating_custom_modules/` |
| 2 | Using Built-in Modules | `02_using_builtin_modules/` |
| 3 | Installing and Using Packages with Pip | `03_installing_packages_with_pip/` |
| 4 | Python Standard Library Overview | `04_python_standard_library_overview/` |
| 5 | Using AI LLM Models with Python | `05_using_ai_llm_models_with_python/` |
| 6 | Using uv for Project and Packages | `06_using_uv_for_projects_and_packages/` |
| 7 | Python Type Hints | `07_python_type_hints/` |

## Why this class is a folder rather than a single file

Class 7 (Four Pillars of OOP) fit comfortably into a single `.py` file,
since every concept could be demonstrated with plain classes in one script.

Class 8 is different — topics such as **custom modules/packages** and
**uv** are fundamentally about how files and folders relate to each other.
A single file cannot really demonstrate what a package is; an actual
multi-file structure is required to import from. This class is therefore
organized as a folder, with one subfolder per topic, in the same order as
the topic list.

## Running each topic

```bash
# Topic 1 — custom modules & packages
cd 01_creating_custom_modules
python main.py

# Topic 2 — built-in modules
cd 02_using_builtin_modules
python builtin_modules_demo.py

# Topic 3 — pip packages
cd 03_installing_packages_with_pip
pip install -r requirements.txt
python pip_packages_demo.py

# Topic 4 — standard library tour
cd 04_python_standard_library_overview
python stdlib_overview.py

# Topic 5 — AI/LLM models (see setup note below)
cd 05_using_ai_llm_models_with_python
pip install google-genai python-dotenv
cp .env.example .env    # then edit .env and add the real API key
python ai_llm_demo.py

# Topic 6 — uv (command-line focused; read the guide rather than run a script)
cd 06_using_uv_for_projects_and_packages
cat uv_guide.md

# Topic 7 — type hints
cd 07_python_type_hints
python type_hints_demo.py
```

## Note on secrets

Topic 5 (`05_using_ai_llm_models_with_python/`) demonstrates the correct
pattern for handling API keys: secrets are loaded from a `.env` file via
`os.environ`, never written directly into a `.py` file. The accompanying
`.gitignore` excludes `.env` so real keys are never committed.
