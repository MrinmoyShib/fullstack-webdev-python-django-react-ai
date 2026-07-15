# =============================================================================
# 08 - Exploring Python Modules and Packages
# =============================================================================
# Topic        : Using Built-in Modules
# File         : 02_using_builtin_modules/builtin_modules_demo.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================
#
# Built-in modules ship with Python — no pip install required. They are
# written in C or Python and bundled into every Python installation. We
# simply import them by name.
#
# This file tours the modules we reach for most often.

# ── math ──────────────────────────────────────────────────────────────────
# Numeric operations beyond the basic + - * /
import math

print(math.sqrt(144))         # Expected output: 12.0
print(math.floor(4.9))        # Expected output: 4
print(math.ceil(4.1))         # Expected output: 5
print(math.pi)                 # Expected output: 3.141592653589793
print(math.factorial(5))       # Expected output: 120


# ── random ────────────────────────────────────────────────────────────────
# Generating randomness — numbers, choices, shuffles
import random

print(random.randint(1, 10))                    # Expected output: a random int 1-10 (inclusive)
print(random.choice(["red", "green", "blue"]))   # Expected output: one of the three, randomly
sample_list = [1, 2, 3, 4, 5]
random.shuffle(sample_list)                      # Shuffles the list in place
print(sample_list)                               # Expected output: same 5 numbers, random order


# ── datetime ──────────────────────────────────────────────────────────────
# Working with dates and times
from datetime import datetime, timedelta

now = datetime.now()
print(now.year, now.month, now.day)       # Expected output: current year, month, day

one_week_later = now + timedelta(weeks=1)
print(one_week_later.strftime("%Y-%m-%d"))  # Expected output: date 7 days from today, e.g. 2026-07-21


# ── os ────────────────────────────────────────────────────────────────────
# Talking to the operating system — files, folders, environment variables
import os

print(os.getcwd())                        # Expected output: current working directory path
print(os.listdir("."))                    # Expected output: list of files/folders in current dir

# Reading an environment variable safely (returns a default instead of
# raising an error if it doesn't exist)
print(os.environ.get("PATH_DOES_NOT_EXIST", "default_value"))
# Expected output: default_value


# ── sys ───────────────────────────────────────────────────────────────────
# Interacting with the Python interpreter itself
import sys

print(sys.version)                        # Expected output: the Python version string
# print(sys.argv)                         # Command-line arguments passed to the script


# ── json ──────────────────────────────────────────────────────────────────
# Converting between Python objects and JSON text — the standard data
# format used by nearly every web API
import json

user = {"name": "Micheal", "age": 16, "is_student": True}

json_string = json.dumps(user)            # Python dict -> JSON string
print(json_string)
# Expected output: {"name": "Micheal", "age": 16, "is_student": true}

parsed_back = json.loads(json_string)     # JSON string -> Python dict
print(parsed_back["name"])
# Expected output: Micheal


# ── string ────────────────────────────────────────────────────────────────
# Useful string constants
import string

print(string.ascii_lowercase)   # Expected output: abcdefghijklmnopqrstuvwxyz
print(string.digits)            # Expected output: 0123456789


# ── time ──────────────────────────────────────────────────────────────────
# Pausing execution, measuring elapsed time
import time

start = time.time()
time.sleep(1)   # Pauses the program for 1 second
end = time.time()
print(f"Elapsed: {end - start:.2f} seconds")
# Expected output: Elapsed: 1.00 seconds (approximately)


# =============================================================================
# Key Takeaways
# =============================================================================
# - Built-in modules come free with Python — simply `import` them.
# - math      -> numeric operations
# - random    -> randomness
# - datetime  -> dates and times
# - os        -> operating system, file paths, environment variables
# - sys       -> the interpreter itself
# - json      -> converting between Python objects and JSON
# - string    -> useful string constants
# - time      -> pausing and measuring time
#
# There are 200+ built-in modules in total. We do not need to memorize them —
# it is enough to know they exist, and to search "python <thing> module"
# whenever a need arises.
# =============================================================================
