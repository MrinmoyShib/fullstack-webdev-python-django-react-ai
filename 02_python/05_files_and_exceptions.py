# =============================================================================
# 05 - Handling Files & Exceptions
# =============================================================================
# Topic        : Exceptions, try/except/else/finally, raise, Custom Exceptions,
#                File Handling (read/write/append), with statement,
#                Absolute vs Relative Paths, Files & Exceptions together
# File         : 05_files_and_exceptions.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# -----------------------------------------------------------------------------
# 1. What Is an Exception?
# -----------------------------------------------------------------------------
# When Python can't do what we're asking, it RAISES an exception - it stops
# running and shows an error message called a "traceback". This isn't the
# program "crashing" in a mysterious way; it's Python being very specific
# about exactly what went wrong and where. Learning to read these messages
# is one of the most useful skills in Python.

# Each line below would raise a different exception if uncommented.
# They're left commented so this file can run from top to bottom without
# stopping.

# print("Hello" + 5)          # TypeError    - wrong types combined
# print(user_name)             # NameError    - variable was never defined
# print(int("twenty"))         # ValueError   - right type, but bad value
# print(100 / 0)               # ZeroDivisionError - maths doesn't allow this
# items = ["a", "b"]
# print(items[9])              # IndexError   - index 9 doesn't exist
# data = {"name": "Ali"}
# print(data["age"])           # KeyError     - "age" key doesn't exist
# open("nowhere.txt", "r")     # FileNotFoundError - file doesn't exist


# -----------------------------------------------------------------------------
# 2. Common Built-in Exceptions (Quick Reference)
# -----------------------------------------------------------------------------
# Exception            | When it happens
# ---------------------|----------------------------------------------
# SyntaxError          | Code is written incorrectly (caught before running)
# NameError            | Using a variable that has never been defined
# TypeError            | Operation used on the wrong type (e.g. str + int)
# ValueError           | Right type, but the value makes no sense (int("hi"))
# IndexError           | Accessing a list index that doesn't exist
# KeyError             | Accessing a dict key that doesn't exist
# ZeroDivisionError    | Dividing any number by zero
# FileNotFoundError    | Trying to open a file that doesn't exist


# -----------------------------------------------------------------------------
# 3. try / except — Catching Exceptions
# -----------------------------------------------------------------------------
# Instead of letting an exception crash our program, we can "try" a risky
# block of code and "except" (catch) specific errors to handle gracefully.
# We can stack multiple except blocks to handle different errors differently.
#
# NOTE: This section is INTERACTIVE — it will pause and wait for us to type
# two numbers before continuing.

print("--- Safe Division Calculator ---")
try:
    numerator = int(input("Enter a number: "))
    denominator = int(input("Divide it by: "))
    result = numerator / denominator
    print(f"Answer: {result}")
except ValueError:
    print("Please type a whole number, not text.")
except ZeroDivisionError:
    print("You can't divide by zero.")
except Exception as error:
    # "Exception" is a catch-all - it catches anything we didn't list above.
    # "as error" gives us access to the actual error message Python generated.
    print(f"Something unexpected happened: {error}")


# -----------------------------------------------------------------------------
# 4. else & finally
# -----------------------------------------------------------------------------
# An optional "else" block runs ONLY when no exception was raised - perfect
# for code that should only happen on success.
# A "finally" block ALWAYS runs no matter what - exception or not. It's the
# right place for clean-up tasks (like closing a file or a database connection)
# that must happen regardless of what went wrong.
#
# NOTE: This section is INTERACTIVE — it will pause and wait for us to type
# a password before continuing.

print("\n--- Login Attempt ---")
try:
    password = input("Enter password: ")
    if password != "open123":
        raise ValueError("Incorrect password.")
    print("Access granted!")
except ValueError as error:
    print(f"Access denied: {error}")
else:
    print("Session started successfully.")    # only runs if no exception
finally:
    print("Login attempt recorded.")          # always runs, no matter what


# -----------------------------------------------------------------------------
# 5. raise — Triggering Our Own Exceptions
# -----------------------------------------------------------------------------
# We're not limited to Python's built-in exceptions. We can use "raise" to
# deliberately trigger an exception ourselves - for example, when the user's
# input is technically valid but doesn't make sense for our program's rules.

def set_age(age):
    """Accept an age only if it's a realistic positive number."""
    if not isinstance(age, int):
        raise TypeError("Age must be a whole number.")
    if age < 0 or age > 130:
        raise ValueError(f"Age {age} is not realistic.")
    print(f"Age set to: {age}")

try:
    set_age(25)     # Age set to: 25
    set_age(-5)     # raises ValueError - jumps straight to except
except (TypeError, ValueError) as error:
    print(f"Invalid age: {error}")    # Invalid age: Age -5 is not realistic.


# -----------------------------------------------------------------------------
# 6. Custom Exceptions
# -----------------------------------------------------------------------------
# We can create our own exception types by making a class that inherits from
# "Exception". This lets us give our errors meaningful names that describe
# our specific problem domain - much clearer than a generic ValueError.
# (Classes are covered in depth in a later session - for now just notice the
# "class" keyword and "Exception" in parentheses.)

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available account balance."""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw {amount}. Balance is only {balance}."
        )
    return balance - amount

try:
    new_balance = withdraw(500, 800)
except InsufficientFundsError as error:
    print(f"Transaction failed: {error}")
    # Transaction failed: Cannot withdraw 800. Balance is only 500.


# -----------------------------------------------------------------------------
# 7. File Handling — Opening & Closing Files
# -----------------------------------------------------------------------------
# open() gives us access to a file on disk. We must always call .close()
# afterwards so the operating system can free up its resources.
# The second argument to open() is the MODE:
#
# Mode  | What it does
# ------|-------------------------------------------------------------
# "r"   | Read. File must already exist.
# "w"   | Write. Creates file if missing; ERASES existing content.
# "a"   | Append. Creates file if missing; adds to the END of content.
# "rb"  | Read binary (for images, PDFs, etc.)
# "wb"  | Write binary

# Writing a new file (creates it; overwrites if it already exists)
notes_file = open("study_notes.txt", "w")
notes_file.write("Python Notes\n")
notes_file.write("Lesson 1: Everything in Python is an object.\n")
notes_file.write("Lesson 2: Indentation defines code blocks.\n")
notes_file.close()

# Reading the file back
notes_file = open("study_notes.txt", "r")
content = notes_file.read()    # .read() returns the whole file as one string
notes_file.close()
print(content)

# Appending more content (doesn't erase what's already there)
notes_file = open("study_notes.txt", "a")
notes_file.write("Lesson 3: Functions help us avoid repeating ourselves.\n")
notes_file.close()


# -----------------------------------------------------------------------------
# 8. Reading Files Line by Line
# -----------------------------------------------------------------------------
# .read()      - returns the entire file as a single string
# .readline()  - returns only the NEXT line each time it's called
# .readlines() - returns all lines as a LIST of strings (each ends in "\n")

with open("study_notes.txt", "r") as notes_file:
    lines = notes_file.readlines()

for index, line in enumerate(lines, start=1):
    print(f"Line {index}: {line.strip()}")    # .strip() removes the "\n"
# prints:
# Line 1: Python Notes
# Line 2: Lesson 1: Everything in Python is an object.
# Line 3: Lesson 2: Indentation defines code blocks.
# Line 4: Lesson 3: Functions help us avoid repeating ourselves.


# -----------------------------------------------------------------------------
# 9. The "with" Statement — The Right Way to Open Files
# -----------------------------------------------------------------------------
# Manually calling .close() is easy to forget, especially if an exception
# happens before we get to that line. The "with" block solves this: Python
# automatically closes the file when the indented block ends, even if an
# error occurs. This is the recommended way to work with files.

with open("study_notes.txt", "r") as notes_file:
    content = notes_file.read()
    print("File content loaded successfully.")
# The file is closed here automatically - no .close() needed.


# -----------------------------------------------------------------------------
# 10. Mystery of Path — Absolute vs Relative Paths
# -----------------------------------------------------------------------------
# When we write open("study_notes.txt"), Python looks for that file in the
# CURRENT WORKING DIRECTORY - wherever the script is being run from.
# That's a RELATIVE path: relative to wherever we currently are.
#
# An ABSOLUTE path spells out the full address from the root of the drive,
# so it works regardless of where the script is run from.
#
# Relative path:  "study_notes.txt"          (same folder as the script)
#                 "data/study_notes.txt"      (inside a subfolder called data)
#                 "../study_notes.txt"        (one folder up)
#
# Absolute path:  "/home/username/project/study_notes.txt"   (Linux / Mac)
#                 "C:\\Users\\username\\project\\notes.txt"  (Windows)
#
# The os module lets us build and inspect paths in a way that works across
# all operating systems, so we don't have to worry about / vs \

import os

current_folder = os.getcwd()
print("Current working directory:", current_folder)

# os.path.join() builds a path correctly for the OS we're running on
full_path = os.path.join(current_folder, "study_notes.txt")
print("Full absolute path:", full_path)

# Checking whether a file or folder exists before trying to open it
print("Does the file exist?", os.path.isfile(full_path))     # True
print("Does the folder exist?", os.path.isdir(current_folder))  # True


# -----------------------------------------------------------------------------
# 11. Files & Exceptions Together — Real-World Pattern
# -----------------------------------------------------------------------------
# In real projects these two topics are almost always used together.
# "with" guarantees the file closes cleanly, and try/except stops a missing
# file (or bad input) from crashing the whole program.
# This pattern - an activity logger that records what happened even on errors
# - is something we'll see in Django, APIs, and almost every production app.

def run_calculator_with_log(log_path):
    """
    A simple calculator that logs every event (success or failure) to a file.
    Demonstrates combining file handling and exception handling in one flow.
    """
    with open(log_path, "a") as log:
        log.write("\n--- New session ---\n")
        print("Welcome to the logging calculator!")

        try:
            first  = int(input("First number: "))
            second = int(input("Second number: "))
            answer = first / second
            print(f"Result: {answer}")
            log.write(f"Calculated {first} / {second} = {answer}\n")

        except ValueError:
            msg = "User entered non-integer input."
            print("Please enter whole numbers only.")
            log.write(f"ValueError: {msg}\n")

        except ZeroDivisionError:
            msg = "User attempted division by zero."
            print("Cannot divide by zero.")
            log.write(f"ZeroDivisionError: {msg}\n")

        except Exception as error:
            print(f"Unexpected error: {error}")
            log.write(f"Unknown error: {error}\n")

        finally:
            log.write("Session ended.\n")
            print("Session closed.")

# Uncomment the line below to run the interactive logger:
# run_calculator_with_log("app_log.txt")


# =============================================================================
# Key Takeaways
# - An exception is Python's way of telling us exactly what went wrong and
#   where - reading the traceback carefully is the first step to fixing it
# - try/except lets us handle errors gracefully instead of crashing; stack
#   multiple except blocks to respond differently to different error types
# - The else block runs only when NO exception occurred; finally ALWAYS runs
#   and is the right place for clean-up code
# - raise lets us deliberately trigger an exception with our own message when
#   input breaks our program's own rules, not just Python's type rules
# - Custom exception classes (inheriting from Exception) give our errors
#   meaningful, domain-specific names
# - open() needs a mode: "r" to read, "w" to write (erases first),
#   "a" to append; always close the file when done
# - The "with" statement closes the file automatically - even if an exception
#   occurs - making it the safest and cleanest way to handle files
# - A relative path is relative to where the script is run from; an absolute
#   path is the full address from the root of the drive
# - os.path.join() builds paths correctly on any operating system;
#   os.path.isfile() and os.path.isdir() let us check existence before opening
# - Combining "with" + try/except is the standard real-world pattern for any
#   code that reads from or writes to files
# =============================================================================