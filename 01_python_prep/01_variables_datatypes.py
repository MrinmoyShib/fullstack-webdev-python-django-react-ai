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


print("This is a String")  # Single quotation marks
print("This is also a String")  # Double quotation marks (most common)
print("""This is also a String""")  # Triple quotation marks (used for multiline)


# -----------------------------------------------------------------------------
# 3. Assigning a String to a Variable
# -----------------------------------------------------------------------------
# Variables are containers that store data values.
# In Python, no keyword is needed to declare a variable.

name = "Python Developer"  # String variable
greeting = "Assigning string to a variable"

print(name)
print(greeting)


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

print(language.upper())  # PYTHON  — converts to uppercase
print(language.capitalize())  # Python  — capitalizes first letter
print(len(language))  # 6       — returns length of string
print(language.replace("python", "django"))  # django — replaces substring


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
print(course[0])  # Indexing starts from 0
print(course[11])

# -----------------------------------------------------------------------------
# 9. String length
#

course = "Full Stack Web Development"
print(len(course))
