# =============================================================================
# 01 - Variables & Data Types
# =============================================================================
# Topic        : Python Basics — Variables, Strings & Data Types
# File         : 01_variables_datatypes.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Hello World — First Python Program
# -----------------------------------------------------------------------------

print("Hello World!")  # Entry point of every Python journey


# -----------------------------------------------------------------------------
# 2. Strings — Definition & Declaration
# -----------------------------------------------------------------------------
# A string is a sequence of characters enclosed in quotes.
# Python supports three ways to define a string.

print("This is a String")               # Single quotation marks
print("This is also a String")          # Double quotation marks (most common)
print("""This is also a String""")      # Triple quotation marks (used for multiline)


# -----------------------------------------------------------------------------
# 3. Assigning a String to a Variable
# -----------------------------------------------------------------------------
# Variables are containers that store data values.
# In Python, no keyword is needed to declare a variable.

name = "Python Developer"                   # String variable
greeting = "Assigning string to a variable" # String variable

print(name)        # Python Developer
print(greeting)    # Assigning string to a variable


# -----------------------------------------------------------------------------
# 4. Checking Data Type with type()
# -----------------------------------------------------------------------------
# The type() function returns the data type of any variable or value.

print(type(name))  # Output: <class 'str'>
print(type(greeting))  # Output: <class 'str'>


# -----------------------------------------------------------------------------
# 5. Common String Operations
# -----------------------------------------------------------------------------

language = "python"

print(language.upper())                         # Python  — converts to uppercase
print(language.lower())                         # Python  — converts to lowercase
print(language.capitalize())                    # Python  — capitalizes first letter
print(len(language))                            # Python — returns length of string
print(language.replace("python", "django"))     # django — replaces substring


# -----------------------------------------------------------------------------
# 6. String Formatting
# -----------------------------------------------------------------------------

course = "Full Stack Web Development"
stack = "Python, Django, React & AI"

# f-string (modern, recommended approach)

print(f"Course  : {course}")
print(f"Stack   : {stack}")


# -----------------------------------------------------------------------------
# 7. Multiline Strings
# -----------------------------------------------------------------------------
# Triple quotes allow strings to span multiple lines.

about = """
I am learning Full Stack Web Development
using Python, Django, React and AI.
"""

print(about)


# -----------------------------------------------------------------------------
# 8. String Indexing
# -----------------------------------------------------------------------------

course = "Full Stack Web Development"
print(course[0])        # Indexing starts from 0
print(course[11])


# -----------------------------------------------------------------------------
# 9. String length
# -----------------------------------------------------------------------------

course = "Full Stack Web Development"
print(len(course))      # Python — returns length of string


# -----------------------------------------------------------------------------
# 10. Integers
# -----------------------------------------------------------------------------
# An integer is a whole number — positive, negative, or zero.
# No decimal point. No quotes. No limit on size in Python.
 
age        = 25       # Positive integer
year       = 2026     # Another positive integer
floors     = -3       # Negative integer
zero_value = 0        # Zero is also a valid integer
 
print(age)
print(year)
print(type(age))      
 
# Basic arithmetic with integers

print(age + 5)        # 30  — Addition
print(year - 2000)    # 26  — Subtraction
print(age * 2)        # 50  — Multiplication
print(age // 2)       # 12  — Floor division (no decimal)
print(age % 2)        # 1   — Modulus (remainder)
 
 
# -----------------------------------------------------------------------------
# 11. Floats (Decimal Numbers)
# -----------------------------------------------------------------------------
# A float is a number with a decimal point.
# Used when precision matters — prices, measurements, percentages.
 
price       = 19.99    # Float variable
temperature = 36.6     # Body temperature
pi          = 3.14159  # Mathematical constant
 
print(price)
print(temperature)
print(type(price))     
 
# Basic arithmetic with floats
print(price * 2)       
print(round(pi, 2))    # Python  — round() limits decimal places
 
 
# -----------------------------------------------------------------------------
# 12. Float vs Integer — Key Difference
# -----------------------------------------------------------------------------
# Division always returns a float in Python 3
# Floor division (//) always returns an integer
 
print(10 / 2)          # 5.0  — regular division -> float
print(10 // 2)         # 5    — floor division   -> integer
print(type(10 / 2))    # <class 'float'>
print(type(10 // 2))   # <class 'int'>
 
 
# -----------------------------------------------------------------------------
# 13. Booleans
# -----------------------------------------------------------------------------
# A boolean has only two possible values: True or False
# Used in conditions, comparisons, and logic control.
# Note: True and False are capitalized in Python.
 
is_learning  = True
is_expert    = False
is_employed  = False
 
print(is_learning)          # True
print(type(is_learning))    # Output: <class 'bool'>
 
# Booleans from comparisons
print(10 > 5)               # True
print(10 == 5)              # False
print(10 != 5)              # True
 
 
# -----------------------------------------------------------------------------
# 14. Type Conversion (Casting)
# -----------------------------------------------------------------------------
# Python allows converting one data type into another.
# This is called Type Casting or Type Conversion.
 
age_str    = "25"           # This is a string, not a number
age_int    = int(age_str)   # Convert string -> integer
age_float  = float(age_str) # Convert string -> float
 
print(age_int)              # 25
print(age_float)            # 25.0
print(type(age_int))        # <class 'int'>
print(type(age_float))      # <class 'float'>
 
# Convert number to string
score      = 99
score_str  = str(score)     # Convert integer -> string
print(score_str)            # "99"
print(type(score_str))      # <class 'str'>
 
 
# -----------------------------------------------------------------------------
# 15. All Data Types — Summary Table
# -----------------------------------------------------------------------------
# A quick reference of the core Python data types covered in this file.
 
name        = "Mrinmoy Shib"  # str   — text
age         = 25              # int   — whole number
gpa         = 5.00            # float — decimal number
is_learning = True            # bool  — True or False
 
print(f"Name        : {name}        | Type: {type(name)}")
print(f"Age         : {age}         | Type: {type(age)}")
print(f"GPA         : {gpa}         | Type: {type(gpa)}")
print(f"Is Learning : {is_learning} | Type: {type(is_learning)}")
 
 
# =============================================================================
# Key Takeaways
# - str   : text enclosed in quotes — single, double, or triple
# - int   : whole numbers with no decimal point
# - float : numbers with a decimal point, used for precision
# - bool  : only True or False — always capitalized in Python
# - type()       reveals the data type of any variable
# - int(), float(), str() convert between data types (type casting)
# - f-strings are the cleanest way to format strings (Python 3.6+)
# - String indexing starts at 0; negative indexing counts from the end
# - len() returns the total number of characters in a string
# =============================================================================
 
