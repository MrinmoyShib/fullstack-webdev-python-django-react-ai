# =============================================================================
# 08 - Exploring Python Modules and Packages
# =============================================================================
# Topic        : Creating and Using Modules
# File         : 01_creating_custom_modules/main.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================
#
# WHAT IS A MODULE?
#   Any single .py file is a module. The moment we write code in a file and
#   another file imports it, that file is acting as a module.
#
# WHAT IS A PACKAGE?
#   A folder containing an __init__.py file. It is a way of grouping related
#   modules together (like "shapes_package" sitting next to this file).
#
# WHY THIS MATTERS
#   Without modules, an entire project would live in one giant file.
#   Splitting code into modules lets us:
#     - reuse code across multiple files and projects
#     - keep related logic together (all shape math in one place)
#     - avoid naming collisions (two functions can both be called "area"
#       if they live in different modules)
#
# This file demonstrates every common way to import from a custom package.
# =============================================================================

# ── Import style 1: import the whole package ────────────────────────────────
# Access everything through the package name.
import shapes_package

c1 = shapes_package.Circle(3)
print(c1.area())
# Expected output: 28.27431


# ── Import style 2: import a specific submodule ─────────────────────────────
# Useful when only one file out of a larger package is needed.
from shapes_package import square

sq1 = square.Square(6)
print(sq1.perimeter())
# Expected output: 24


# ── Import style 3: import a specific name (re-exported via __init__.py) ────
# This works because shapes_package/__init__.py contains:
#   from .circle import Circle
from shapes_package import Circle, Square

c2 = Circle(10)
sq2 = Square(2)
print(c2.perimeter())
# Expected output: 62.8318
print(sq2.area())
# Expected output: 4


# ── Import style 4: rename on import with "as" ───────────────────────────────
# Handy for shortening long names or avoiding clashes with other imports.
from shapes_package.circle import Circle as Round

r = Round(1)
print(r.area())
# Expected output: 3.14159


# ── Import style 5: importing package-level constants ───────────────────────
print(shapes_package.PACKAGE_VERSION)
# Expected output: 1.0.0


# ── A note on relative imports ──────────────────────────────────────────────
# Inside shapes_package/__init__.py, this line appears:
#   from .circle import Circle
#
# That leading dot means "from this package". It is called a relative
# import, and it only works when the file doing the importing is itself
# part of a package (i.e. sits in a folder with an __init__.py). A relative
# import cannot be used in a standalone script like this main.py file —
# which is why main.py uses absolute imports (shapes_package.circle) instead.


# ── __name__ == "__main__" ───────────────────────────────────────────────────
# Every Python file has a hidden variable called __name__.
#   - When a file is run directly            -> __name__ == "__main__"
#   - When a file is imported by another file -> __name__ == "<module name>"
#
# This lets a module hold demo code that only runs when that file is
# executed directly, and stays silent when the module is imported elsewhere.
# (See the bottom of circle.py and square.py for this pattern in action.)

if __name__ == "__main__":
    print("\n--- Running main.py directly ---")
    print(f"This file's __name__ is: {__name__}")
else:
    print(f"main.py was imported, __name__ is: {__name__}")

# Expected output when run directly (python main.py):
# --- Running main.py directly ---
# This file's __name__ is: __main__


# =============================================================================
# Key Takeaways
# =============================================================================
# - A module is any .py file; a package is a folder with an __init__.py.
# - Common import styles: import package, from package import module,
#   from package import Name, and renaming with "as".
# - __init__.py can re-export names so callers get shorter import paths.
# - Relative imports (from .module import X) only work inside a package.
# - __name__ == "__main__" lets a file behave differently when run directly
#   versus when it is imported.
# =============================================================================
