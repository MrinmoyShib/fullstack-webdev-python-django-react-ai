# =============================================================================
# 08 - Exploring Python Modules and Packages
# =============================================================================
# Topic        : Creating and Using Modules
# File         : 01_creating_custom_modules/shapes_package/square.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================
#
# A sibling module to circle.py, inside the same package.
# =============================================================================


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


def describe_square(side):
    s = Square(side)
    print(f"Square(side={side}) -> area={s.area():.2f}, perimeter={s.perimeter():.2f}")


if __name__ == "__main__":
    describe_square(4)
    # Expected output when run directly:
    # Square(side=4) -> area=16.00, perimeter=16.00
