# =============================================================================
# 08 - Exploring Python Modules and Packages
# =============================================================================
# Topic        : Creating and Using Modules
# File         : 01_creating_custom_modules/shapes_package/circle.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================
#
# A regular Python file becomes a module the moment another file imports it.
# There is nothing special about this file on its own — it only becomes part
# of the "shapes_package" package because it lives inside a folder that has
# an __init__.py.
# =============================================================================

PI = 3.14159   # A module-level constant, accessible as circle.PI


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def perimeter(self):
        return 2 * PI * self.radius


def describe_circle(radius):
    """A plain module-level function (does not need a class)."""
    c = Circle(radius)
    print(f"Circle(radius={radius}) -> area={c.area():.2f}, perimeter={c.perimeter():.2f}")


# This block only runs when this file is executed directly, e.g.:
#   python circle.py
# It will not run when this file is imported elsewhere — which is exactly
# why this pattern is used to keep quick tests inside a module without
# them firing every time the module gets imported.
if __name__ == "__main__":
    describe_circle(5)
    # Expected output when run directly:
    # Circle(radius=5) -> area=78.54, perimeter=31.42
