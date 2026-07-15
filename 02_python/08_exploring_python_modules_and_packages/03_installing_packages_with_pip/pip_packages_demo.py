# =============================================================================
# 08 - Exploring Python Modules and Packages
# =============================================================================
# Topic        : Installing and Using Packages with Pip
# File         : 03_installing_packages_with_pip/pip_packages_demo.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================
#
# Built-in modules cover a lot, but not everything. To talk to a website,
# read Excel files, build a web server, or use AI models, we need
# THIRD-PARTY PACKAGES — code other developers wrote and published for
# everyone to reuse.
#
# pip = "Pip Installs Packages". It is the tool that downloads packages from
# PyPI (the Python Package Index, https://pypi.org) onto our machine.
#
# ── THE CORE COMMANDS ────────────────────────────────────────────────────────
#
#   pip install requests            -> installs the "requests" package
#   pip install requests==2.32.3    -> installs an exact version
#   pip uninstall requests          -> removes it
#   pip list                        -> shows everything installed
#   pip show requests               -> shows details about one package
#   pip freeze > requirements.txt   -> saves every installed package and its
#                                       version into a file so others can
#                                       recreate our exact setup
#   pip install -r requirements.txt -> installs everything listed in that file
#
# ── WHY requirements.txt MATTERS ─────────────────────────────────────────────
# When pushing code to GitHub, we should not push installed packages — they
# can be large and are OS-specific. Instead, we push requirements.txt, and
# whoever clones the repo runs:
#   pip install -r requirements.txt
# ...and gets the exact same packages we used. This folder includes one
# right next to this file.
#
# ── VIRTUAL ENVIRONMENTS (why they matter) ───────────────────────────────────
# If every project on a machine shares one global set of packages, projects
# can conflict (Project A needs requests==2.0, Project B needs requests==3.0).
# A virtual environment is an isolated folder of packages per project.
#
#   python -m venv venv          -> creates a virtual environment folder
#   source venv/bin/activate     -> activates it (Mac/Linux)
#   venv\Scripts\activate        -> activates it (Windows)
#   pip install requests         -> installs only inside this project
#   deactivate                   -> leaves the virtual environment
#
# (A modern, faster alternative to venv + pip — called uv — is covered in
# 06_using_uv_for_projects_and_packages.)


# ── USING A THIRD-PARTY PACKAGE: "requests" ─────────────────────────────────
# requests is the most widely used package for making HTTP requests (calling
# websites and APIs) in Python. It is not built-in — it must be pip installed:
#   pip install requests

import requests

response = requests.get("https://api.github.com")

print(response.status_code)
# Expected output: 200 (success)

print(type(response.json()))
# Expected output: <class 'dict'> (GitHub's API replies with JSON)

data = response.json()
print(data.get("current_user_url"))
# Expected output: something like https://api.github.com/user


# =============================================================================
# Key Takeaways
# =============================================================================
# - pip installs third-party packages from PyPI.
# - pip install <name>              -> install a package
# - pip install -r requirements.txt -> install everything a project needs
# - pip freeze > requirements.txt   -> record what is currently installed
# - Use a virtual environment (venv, or uv — next topic) to keep each
#   project's packages isolated from every other project on the machine.
# - Never push a virtual environment folder to GitHub — push
#   requirements.txt instead, and add the venv folder to .gitignore.
# =============================================================================
