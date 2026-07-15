# =============================================================================
# 08 - Exploring Python Modules and Packages
# =============================================================================
# Topic        : Creating and Using Modules (Package Initialization)
# File         : 01_creating_custom_modules/shapes_package/__init__.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================
#
# This file is what turns the "shapes_package" folder into a Python package.
#
# Rule: any folder containing an __init__.py can be imported like a module.
#   import shapes_package
#
# Whatever we write in __init__.py runs the moment the package is imported,
# even if only one function is needed from it. That makes it the ideal place
# for:
#   1. Package-level constants
#   2. Re-exporting names from inner files so callers don't need long import
#      paths
#
# Without the re-exports below, we would have to write:
#   from shapes_package.circle import Circle
#
# With the re-exports, we can instead write:
#   from shapes_package import Circle
# =============================================================================

PACKAGE_VERSION = "1.0.0"

# Re-export so callers can do `from shapes_package import Circle, Square`
# instead of digging into the submodules directly.
from .circle import Circle
from .square import Square

# __all__ controls what gets imported when someone does:
#   from shapes_package import *
# It is good practice to define this explicitly rather than let Python guess.
__all__ = ["Circle", "Square", "PACKAGE_VERSION"]
