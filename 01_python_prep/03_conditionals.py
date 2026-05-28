# =============================================================================
# 03 - Conditionals
# =============================================================================
# Topic        : Python Basics — Conditional Statements & Decision Making
# File         : 03_conditionals.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# -----------------------------------------------------------------------------
# 1. if Statement
# -----------------------------------------------------------------------------
# An if statement is used to make decisions in code.
# The block inside runs ONLY if the condition is True.

today     = 1
rain      = 1

if rain == today:
    print("Today is raining.")  # Output: Today is raining.


# -----------------------------------------------------------------------------
# 2. if-else Statement
# -----------------------------------------------------------------------------
# if-else allows Python to choose between two paths.
# If the condition is True -> first block runs.
# If the condition is False -> else block runs.

yesterday = 1
rain      = 0

if rain == yesterday:
    print("Yesterday was raining.")
else:
    print("Yesterday was not raining.")  # Output: Yesterday was not raining.


# -----------------------------------------------------------------------------
# 3. elif (else-if) Statement
# -----------------------------------------------------------------------------
# elif checks multiple conditions one after the other.
# Python checks each condition top to bottom and runs the first True block.
# The else block runs only if ALL conditions above are False.

today     = 0
yesterday = 0
rain      = 1

if rain == today:
    print("Today is raining.")
elif rain == yesterday:
    print("Yesterday was raining.")
else:
    print("It was not raining yesterday and not raining today.")
    # Output: It was not raining yesterday and not raining today.


# -----------------------------------------------------------------------------
# 4. Comparison Operators in Conditions
# -----------------------------------------------------------------------------
# Conditions are built using comparison operators.
# ==  equal to
# !=  not equal to
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to

age = 20

if age >= 18:
    print("You are an adult.")      # Output: You are an adult.
else:
    print("You are a minor.")


# -----------------------------------------------------------------------------
# 5. Logical Operators in Conditions
# -----------------------------------------------------------------------------
# Logical operators combine multiple conditions.
# and -> both conditions must be True
# or ->  at least one condition must be True
# not -> reverses the condition

temperature = 35
is_sunny    = True

if temperature > 30 and is_sunny:
    print("It is a hot and sunny day.")  # Output: It is a hot and sunny day.

if temperature > 40 or is_sunny:
    print("Wear sunscreen.")             # Output: Wear sunscreen.

if not is_sunny:
    print("You can skip sunscreen.")
else:
    print("Stay protected from the sun.")# Output: Stay protected from the sun.


# -----------------------------------------------------------------------------
# 6. Nested if Statements
# -----------------------------------------------------------------------------
# A nested if is an if statement placed inside another if statement.
# Used when a second condition only matters if the first is already True.

is_registered = True
has_paid      = True

if is_registered:
    if has_paid:
        print("Access granted.")         # Output: Access granted.
    else:
        print("Please complete payment.")
else:
    print("Please register first.")


# -----------------------------------------------------------------------------
# 7. Shorthand if (Ternary Operator)
# -----------------------------------------------------------------------------
# Python allows writing a simple if-else in a single line.
# Syntax: value_if_true if condition else value_if_false

score  = 75
result = "Pass" if score >= 50 else "Fail"
print(result)  # Output: Pass


# -----------------------------------------------------------------------------
# 8. Checking Multiple Values with 'in'
# -----------------------------------------------------------------------------
# The 'in' keyword checks if a value exists inside a list or string.
# A clean alternative to writing many elif conditions.

day = "Saturday"

if day in ["Saturday", "Sunday"]:
    print(f"{day} is a weekend.")   # Output: Saturday is a weekend.
else:
    print(f"{day} is a weekday.")


# =============================================================================
# Key Takeaways
# - if        : runs a block only when the condition is True
# - else      : runs when the if condition is False
# - elif      : checks additional conditions between if and else
# - and       : both conditions must be True
# - or        : at least one condition must be True
# - not       : reverses/negates a condition
# - Nested if : an if statement inside another if for layered decisions
# - Ternary   : single-line if-else for simple assignments
# - in        : checks membership — cleaner than multiple elif conditions
# - Python uses indentation (4 spaces) to define conditional blocks
# =============================================================================