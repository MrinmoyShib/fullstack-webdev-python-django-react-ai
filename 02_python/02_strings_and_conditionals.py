# =============================================================================
# 02 - Strings and Conditional Statements
# =============================================================================
# Topic        : Operators, Strings & String Methods, Indentation, Decision Making
# File         : 02_strings_and_conditionals.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Arithmetic Operators
# -----------------------------------------------------------------------------
# These operators perform basic math between two numbers.

x = 17
y = 5

print(x + y)     # addition       -> 22
print(x - y)     # subtraction    -> 12
print(x * y)     # multiplication -> 85
print(x / y)     # division       -> 3.4   (always returns a float)
print(x % y)     # modulus        -> 2     (the remainder after division)
print(x ** y)    # exponentiation -> 17 to the power of 5
print(x // y)    # floor division -> 3     (drops the decimal part)


# -----------------------------------------------------------------------------
# 2. Assignment Operators
# -----------------------------------------------------------------------------
# These let us update a variable's value in a short, readable way.

score = 10
score += 5    # same as: score = score + 5  -> 15
score -= 3    # same as: score = score - 3  -> 12
score *= 2    # same as: score = score * 2  -> 24
score //= 5   # same as: score = score // 5 -> 4

print(score)


# -----------------------------------------------------------------------------
# 3. Relational (Comparison) Operators
# -----------------------------------------------------------------------------
# These compare two values and always return True or False.

a = 8
b = 12

print(a == b)   # is Equal to                 -> False
print(a != b)   # is Not Equal to             -> True
print(a > b)    # is Greater Than             -> False
print(a < b)    # is Less Than                -> True
print(a >= b)   # is Greater Than or Equal to -> False
print(a <= b)   # is Less Than or Equal to    -> True


# -----------------------------------------------------------------------------
# 4. Logical Operators
# -----------------------------------------------------------------------------
# These combine multiple True/False conditions into one result.

age = 20
has_id = True

print(age >= 18 and has_id)   # "and" -> True only if BOTH sides are True
print(age >= 18 or has_id)    # "or"  -> True if AT LEAST ONE side is True
print(not has_id)             # "not" -> flips True to False (and vice versa)


# -----------------------------------------------------------------------------
# 5. Operator Precedence
# -----------------------------------------------------------------------------
# When an expression has multiple operators, Python follows this order:
# 1. ()           Parentheses
# 2. **            Exponent
# 3. *, /, //, %   Multiplication, Division, Floor Division, Modulus
# 4. +, -          Addition, Subtraction

result = 5 + 3 * 2               # multiplication happens first -> 5 + 6 -> 11
print(result)

result_with_parens = (5 + 3) * 2   # parentheses force addition first -> 16
print(result_with_parens)


# -----------------------------------------------------------------------------
# 6. Math Functions & the math Module
# -----------------------------------------------------------------------------
# Python's built-in math module gives us extra math tools beyond +, -, *, /.

import math  # noqa: E402

print(math.sqrt(81))     # square root -> 9.0
print(math.floor(7.9))   # rounds down -> 7
print(math.ceil(7.1))    # rounds up   -> 8
print(math.pow(2, 5))    # 2 to the power of 5 -> 32.0


# -----------------------------------------------------------------------------
# 7. Strings & Indexing / Slicing
# -----------------------------------------------------------------------------
# A string is just a sequence of characters. Every character has an index,
# and we can grab a single character or a whole "slice" (range) of them.

word = "Python"

print(word[0])      # 'P'    -> first character (index 0)
print(word[-1])     # 'n'    -> last character (negative index counts from the end)
print(word[0:3])    # 'Pyt'  -> characters from index 0 up to (not including) 3
print(word[2:])     # 'thon' -> everything from index 2 onward


# -----------------------------------------------------------------------------
# 8. Formatted Strings (f-strings)
# -----------------------------------------------------------------------------
# f-strings let us drop variables directly into a string using {}.

city = "Faridpur"
temperature = 32

print(f"Right now in {city}, it's {temperature}°C.")


# -----------------------------------------------------------------------------
# 9. Common String Methods
# -----------------------------------------------------------------------------
# Strings have many built-in methods. None of them change the original string
# - they always return a brand-new string.

raw_text = "   Hello PYTHON   "

print(raw_text.lower())                            # "   hello python   "
print(raw_text.strip())                            # "Hello PYTHON" (no outer spaces)
print(raw_text.strip().replace("PYTHON", "World"))  # "Hello World"


# -----------------------------------------------------------------------------
# 10. Indentation / Code Blocks
# -----------------------------------------------------------------------------
# Python uses indentation (spaces) instead of curly braces {} to define a
# block of code. Everything indented under a statement belongs to that block.

temperature_today = 35

if temperature_today > 30:
    print("It's hot today!")     # this line belongs to the "if" block
    print("Stay hydrated.")      # so does this one

print("This line always runs.")  # not indented, so it's outside the block


# -----------------------------------------------------------------------------
# 11. Decision Making: if
# -----------------------------------------------------------------------------
# An "if" statement only runs its block when the condition is True.

marks = 85

if marks >= 80:
    print("Excellent result!")

print("Result check complete.")


# -----------------------------------------------------------------------------
# 12. Decision Making: if ... else
# -----------------------------------------------------------------------------
# "else" gives us a fallback block that runs only when the "if" condition
# is False.

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# -----------------------------------------------------------------------------
# 13. Decision Making: if ... elif ... else
# -----------------------------------------------------------------------------
# "elif" lets us check multiple conditions in order. Python checks them
# top to bottom and stops at the first one that's True.

wallet_balance = 40

if wallet_balance >= 50:
    print("You can buy the ice cream box!")
elif wallet_balance >= 25:
    print("You can buy a snack.")
else:
    print("Maybe save up a bit more!")


# -----------------------------------------------------------------------------
# 14. Decision Making: match ... case (Python 3.10+)
# -----------------------------------------------------------------------------
# "match" is a cleaner alternative to a long chain of if/elif statements
# when we are comparing one value against several fixed options.

day_number = 3

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:                      # "_" is the default case (like "else")
        print("Some other day")


# =============================================================================
# Key Takeaways
# - Arithmetic, assignment, relational, and logical operators are the
#   building blocks of almost every Python expression
# - Operator precedence decides what gets calculated first - use () to be sure
# - Strings can be sliced and indexed; string methods always return a NEW string
# - Indentation defines code blocks in Python - there are no curly braces {}
# - if / elif / else (and match/case) let your program make decisions
# =============================================================================