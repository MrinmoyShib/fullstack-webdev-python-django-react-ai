# =============================================================================
# 01 - Introduction to Python
# =============================================================================
# Topic        : Running Python, Variables, Data Types, Input & Type Conversion
# File         : 01_intro_to_python.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Printing Output
# -----------------------------------------------------------------------------
# print() is the most basic Python function. It displays whatever you give it
# on the screen. This is usually the very first thing every Python learner runs.

print("Hello, World!")


# -----------------------------------------------------------------------------
# 2. Variables
# -----------------------------------------------------------------------------
# A variable is just a labeled box that stores a value in memory.
# Python does NOT need you to declare a type — it figures it out automatically.

age = 25          # an integer value stored in the variable 'age'
city = "Dhaka"    # a string value stored in the variable 'city'

print(age)
print(city)

# A variable's value can change anytime by simply re-assigning it.
age = 26
print(age)        # now prints 26, not 25


# -----------------------------------------------------------------------------
# 3. Variable Naming Rules
# -----------------------------------------------------------------------------
# - Must start with a letter or underscore (never a number)
# - Can only contain letters, numbers, and underscores
# - Cannot use Python's reserved keywords (like "print", "for", "if")
# - Python is case-sensitive: "Age" and "age" are two different variables

student_name = "Karim"   # valid - descriptive and lowercase
_temp = 98.6              # valid - starts with an underscore
# 2nd_place = "Silver"    # invalid - cannot start with a number

print(student_name)


# -----------------------------------------------------------------------------
# 4. Data Types & the type() Function
# -----------------------------------------------------------------------------
# Every value in Python belongs to a "data type". The type() function tells
# you what type a value or variable currently is.

whole_number = 7
decimal_number = 3.14
text_value = "Python"
true_or_false = True

print(type(whole_number))     # <class 'int'>
print(type(decimal_number))   # <class 'float'>
print(type(text_value))       # <class 'str'>
print(type(true_or_false))    # <class 'bool'>


# -----------------------------------------------------------------------------
# 5. Taking Input from the User
# -----------------------------------------------------------------------------
# input() pauses the program and waits for the user to type something.
# IMPORTANT: input() ALWAYS returns a string, even if the user types a number.

favorite_color = input("What is your favorite color? ")
print("Nice! " + favorite_color + " is a great color.")


# -----------------------------------------------------------------------------
# 6. Type Conversion / Casting
# -----------------------------------------------------------------------------
# Since input() always gives back a string, we often need to convert it to a
# number before doing math with it. Converting it ourselves is "explicit" casting.

raw_input_value = input("Enter your age: ")   # this is a string, e.g. "20"
numeric_age = int(raw_input_value)             # now it's an integer

print(type(raw_input_value))   # <class 'str'>
print(type(numeric_age))       # <class 'int'>
print(numeric_age + 5)         # math now works correctly

# Implicit casting happens automatically when Python combines compatible
# types - for example, adding an int and a float always gives back a float.
whole = 10
decimal = 2.5
result = whole + decimal
print(type(result))    # <class 'float'> - Python converted it for you


# -----------------------------------------------------------------------------
# 7. Python is Dynamically Typed
# -----------------------------------------------------------------------------
# A variable's type can change completely just by assigning a new value to it.
# Python doesn't lock a variable to one type forever.

value = 100
print(type(value))     # <class 'int'>

value = "now I'm text"
print(type(value))     # <class 'str'> - same variable, brand new type


# -----------------------------------------------------------------------------
# 8. Basic Operators
# -----------------------------------------------------------------------------
# Arithmetic operators do math. Comparison/logical operators compare values
# and always give back True or False.

a = 9
b = 4

print(a + b)     # addition -> 13
print(a - b)     # subtraction -> 5
print(a * b)     # multiplication -> 36
print(a / b)     # division -> 2.25 (always gives a float)
print(a // b)    # floor division -> 2 (drops the decimal part)
print(a % b)     # modulus / remainder -> 1
print(a ** b)    # exponent -> 9 to the power of 4 -> 6561

print(a == b)              # equality check -> False
print(a > b and b > 0)     # logical "and" -> True


# -----------------------------------------------------------------------------
# 9. Strings & Indexing
# -----------------------------------------------------------------------------
# A string is just a sequence of characters. Each character has a position
# (an index), and counting starts at 0, not 1.

greeting = "Welcome"
print(greeting[0])     # 'W' -> the very first character
print(greeting[3])     # 'c' -> the 4th character (index starts at 0)


# -----------------------------------------------------------------------------
# 10. f-strings (Formatted Strings)
# -----------------------------------------------------------------------------
# f-strings let you insert variable values directly inside a string using
# curly braces {}. This is cleaner than joining text with "+".

user_name = "Sadia"
user_age = 21

print(f"My name is {user_name} and I am {user_age} years old.")


# -----------------------------------------------------------------------------
# 11. Common String Methods
# -----------------------------------------------------------------------------
# Strings come with built-in methods. .replace() swaps one piece of text for
# another and returns a brand-new string — it does NOT change the original.

message = "I love Java"
updated_message = message.replace("Java", "Python")

print(message)            # original is unchanged: "I love Java"
print(updated_message)    # new string: "I love Python"


# -----------------------------------------------------------------------------
# 12. Comments
# -----------------------------------------------------------------------------
# Single-line comments start with '#'. Multi-line comments use triple quotes.
# Comments are ignored by Python - they exist purely to explain code to humans.

# This is a single-line comment

"""
This is a multi-line comment.
It can span across several lines
and is often used for longer explanations.
"""


# =============================================================================
# Key Takeaways
# - print() displays output; input() collects text from the user (always as a string)
# - Variables don't need a declared type - Python infers it automatically
# - type() tells you the current data type of any value or variable
# - Use int(), float(), str() etc. to explicitly convert between types
# - Python is dynamically typed - a variable's type can change at any time
# - f-strings (f"...{variable}...") are the cleanest way to mix text and variables
# =============================================================================