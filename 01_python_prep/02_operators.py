# =============================================================================
# 02 - Operators
# =============================================================================
# Topic        : Python Basics — Operators & Expressions
# File         : 02_operators.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================

import math  # Imported once at the top — Python best practice


# -----------------------------------------------------------------------------
# 1. Addition
# -----------------------------------------------------------------------------

a = 5
b = 6
print(f"The Addition is       : {a + b}")   # Output: 11


# -----------------------------------------------------------------------------
# 2. Subtraction
# -----------------------------------------------------------------------------

c = 15
d = 10
print(f"The Subtraction is    : {c - d}")   # Output: 5


# -----------------------------------------------------------------------------
# 3. Division
# -----------------------------------------------------------------------------

a = 10
b = 5
print(f"The Float Division is   : {a / b}")  # 2.0  — always returns float
print(f"The Integer Division is : {a // b}") # 2    — floor division, no decimal


# -----------------------------------------------------------------------------
# 4. Multiplication
# -----------------------------------------------------------------------------

a = 5
b = 10
print(f"The Multiplication is : {a * b}")   # Output: 50


# -----------------------------------------------------------------------------
# 5. Modulus (Remainder)
# -----------------------------------------------------------------------------
# The % operator returns the remainder after division.
# Commonly used to check if a number is even or odd.

a = 10
b = 3
print(f"The Modulus is        : {a % b}")   # Output: 1 (10 divided by 3 leaves remainder 1)
print(f"Is 10 even?           : {a % 2 == 0}") # True  — no remainder means even
print(f"Is 3 even?            : {b % 2 == 0}") # False — remainder 1 means odd


# -----------------------------------------------------------------------------
# 6. Exponentiation (Power)
# -----------------------------------------------------------------------------
# The ** operator raises a number to a power.

base  = 2
power = 8
print(f"2 to the power of 8  : {base ** power}")  # Output: 256
print(f"Square of 5          : {5 ** 2}")          # Output: 25
print(f"Square root of 16    : {16 ** 0.5}")        # Output: 4.0


# -----------------------------------------------------------------------------
# 7. Operator Precedence (BODMAS / PEMDAS)
# -----------------------------------------------------------------------------
# When an expression has multiple operators, Python follows BODMAS order:
# Brackets → Orders (powers) → Division → Multiplication → Addition → Subtraction
# Use brackets to make your intention clear and avoid unexpected results.

x = (2 + 4) + 45 * 23 / 2 - 0.5

# Step by step:
# (2 + 4)      = 6
# 45 * 23      = 1035
# 1035 / 2     = 517.5
# 6 + 517.5    = 523.5
# 523.5 - 0.5  = 523.0

print(f"Operator Precedence result : {x}")  # Output: 523.0


# -----------------------------------------------------------------------------
# 8. Comparison Operators
# -----------------------------------------------------------------------------
# Comparison operators compare two values and always return a Boolean.

a = 10
b = 5

print(f"a == b  : {a == b}")  # False — equal to
print(f"a != b  : {a != b}")  # True  — not equal to
print(f"a > b   : {a > b}")   # True  — greater than
print(f"a < b   : {a < b}")   # False — less than
print(f"a >= b  : {a >= b}")  # True  — greater than or equal to
print(f"a <= b  : {a <= b}")  # False — less than or equal to


# -----------------------------------------------------------------------------
# 9. Logical Operators
# -----------------------------------------------------------------------------
# Logical operators combine multiple conditions together.

x = True
y = False

print(f"x and y : {x and y}")  # False — both must be True
print(f"x or y  : {x or y}")   # True  — at least one must be True
print(f"not x   : {not x}")    # False — reverses the boolean


# -----------------------------------------------------------------------------
# 10. Assignment Operators
# -----------------------------------------------------------------------------
# Assignment operators update a variable's value in a shorthand way.

score = 100

score += 10   # score = score + 10  -> 110
print(f"After += 10  : {score}")

score -= 20   # score = score - 20  -> 90
print(f"After -= 20  : {score}")

score *= 2    # score = score * 2   -> 180
print(f"After *= 2   : {score}")

score //= 3   # score = score // 3  -> 60
print(f"After //= 3  : {score}")


# -----------------------------------------------------------------------------
# 11. Math Functions — math.ceil()
# -----------------------------------------------------------------------------
# ceil() rounds a number UP to the nearest whole integer,
# no matter how small the decimal part is.

x = 4.1
y = 4.9

print(f"ceil(4.1) : {math.ceil(x)}")  # Output: 5
print(f"ceil(4.9) : {math.ceil(y)}")  # Output: 5


# -----------------------------------------------------------------------------
# 12. Math Functions — math.floor()
# -----------------------------------------------------------------------------
# floor() rounds a number DOWN to the nearest whole integer,
# dropping the decimal entirely.

x = 4.1
y = 4.9

print(f"floor(4.1) : {math.floor(x)}")  # Output: 4
print(f"floor(4.9) : {math.floor(y)}")  # Output: 4


# -----------------------------------------------------------------------------
# 13. Math Functions — round()
# -----------------------------------------------------------------------------
# round() rounds to the nearest integer based on standard rounding rules.
# .5 and above rounds up, below .5 rounds down.
# round() also accepts a second argument for decimal places.

print(f"round(4.4) : {round(4.4)}")     # Output: 4
print(f"round(4.5) : {round(4.5)}")     # Output: 4 — Python uses banker's rounding
print(f"round(4.6) : {round(4.6)}")     # Output: 5
print(f"round(3.14159, 2) : {round(3.14159, 2)}")  # Output: 3.14


# -----------------------------------------------------------------------------
# 14. Other Useful math Module Functions
# -----------------------------------------------------------------------------

print(f"math.sqrt(25)    : {math.sqrt(25)}")    # 5.0  — square root
print(f"math.pow(2, 10)  : {math.pow(2, 10)}")  # 1024.0 — power (returns float)
print(f"math.pi          : {math.pi}")           # 3.14159... — value of pi
print(f"math.abs(-7)     : {abs(-7)}")           # 7    — absolute value


# =============================================================================
# Key Takeaways
# - +   : Addition          | -   : Subtraction
# - *   : Multiplication    | /   : Division (always float)
# - //  : Floor division    | %   : Modulus (remainder)
# - **  : Exponentiation    (e.g. 2 ** 3 = 8)
# - BODMAS / PEMDAS defines the order Python evaluates expressions
# - Comparison operators (==, !=, >, <, >=, <=) always return True or False
# - Logical operators (and, or, not) combine boolean conditions
# - Assignment operators (+=, -=, *=, //=) update variables in shorthand
# - import math should always be placed at the TOP of the file
# - math.ceil()  → always rounds UP
# - math.floor() → always rounds DOWN
# - round()      → rounds to nearest (uses banker's rounding on .5)
# =============================================================================