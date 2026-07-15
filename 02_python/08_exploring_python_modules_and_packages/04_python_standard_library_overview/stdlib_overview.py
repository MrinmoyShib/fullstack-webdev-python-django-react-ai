# =============================================================================
# 08 - Exploring Python Modules and Packages
# =============================================================================
# Topic        : Python Standard Library Overview
# File         : 04_python_standard_library_overview/stdlib_overview.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================
#
# The "Standard Library" is the full collection of built-in modules shipped
# with every Python installation — 200+ modules covering almost everything
# needed before reaching for a third-party package.
#
# Python's own documentation describes this philosophy as "batteries
# included", meaning we rarely need to pip install something for common
# tasks.
#
# math, random, datetime, os, sys, json, string, and time were covered in
# the previous topic. This file tours a second wave of modules that come up
# constantly once we start building real projects.
# Full official reference: https://docs.python.org/3/library/


# ── collections ───────────────────────────────────────────────────────────
# Specialized container types beyond list/dict/set/tuple
from collections import Counter, defaultdict, namedtuple

word_counts = Counter("mississippi")
print(word_counts)
# Expected output: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# defaultdict never raises a KeyError — it produces a default value instead
groups = defaultdict(list)
groups["fruits"].append("apple")
groups["fruits"].append("banana")
print(dict(groups))
# Expected output: {'fruits': ['apple', 'banana']}

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)
# Expected output: 3 4


# ── itertools ─────────────────────────────────────────────────────────────
# Efficient tools for looping and combining data
import itertools

print(list(itertools.permutations([1, 2, 3])))
# Expected output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

print(list(itertools.combinations([1, 2, 3], 2)))
# Expected output: [(1, 2), (1, 3), (2, 3)]


# ── functools ─────────────────────────────────────────────────────────────
# Tools for working with functions themselves
from functools import reduce, lru_cache

total = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
print(total)
# Expected output: 15

@lru_cache(maxsize=None)   # Caches results so repeated calls are instant
def slow_square(n):
    return n * n

print(slow_square(9))
# Expected output: 81


# ── pathlib ───────────────────────────────────────────────────────────────
# The modern, object-oriented way to work with file paths
from pathlib import Path

current_folder = Path(".")
print(current_folder.resolve())
# Expected output: the absolute path of the current folder

py_files = list(current_folder.glob("*.py"))
print(py_files)
# Expected output: [PosixPath('stdlib_overview.py')]


# ── re (regular expressions) ─────────────────────────────────────────────
# Pattern matching inside text
import re

text = "Contact numbers are 017-1234-5678 and 018-9876-5432"
numbers = re.findall(r"\d{3}-\d{4}-\d{4}", text)
print(numbers)
# Expected output: ['017-1234-5678', '018-9876-5432']


# ── csv ───────────────────────────────────────────────────────────────────
# Reading and writing spreadsheet-style comma-separated files
import csv
import io

fake_file = io.StringIO()   # An in-memory "file" so this demo needs no disk
writer = csv.writer(fake_file)
writer.writerow(["name", "age"])
writer.writerow(["Micheal", 16])

fake_file.seek(0)
reader = csv.reader(fake_file)
for row in reader:
    print(row)
# Expected output:
# ['name', 'age']
# ['Micheal', '16']


# ── statistics ────────────────────────────────────────────────────────────
# Common statistical calculations without needing numpy for simple cases
import statistics

marks = [78, 85, 92, 88, 76]
print(statistics.mean(marks))     # Expected output: 83.8
print(statistics.median(marks))   # Expected output: 85


# ── argparse ──────────────────────────────────────────────────────────────
# Building command-line tools that accept flags and options.
# (Shown as reference code — it must be run from a terminal with actual
# arguments, e.g. `python stdlib_overview.py --name Micheal`)
#
#   import argparse
#   parser = argparse.ArgumentParser()
#   parser.add_argument("--name", help="Name to greet")
#   args = parser.parse_args()
#   print(f"Hello, {args.name}!")


# =============================================================================
# Key Takeaways
# =============================================================================
# - The Standard Library is Python's built-in toolbox — no pip install needed.
# - collections -> smarter containers (Counter, defaultdict, namedtuple)
# - itertools   -> efficient looping and combining
# - functools   -> tools for working with functions (reduce, caching)
# - pathlib     -> modern file path handling
# - re          -> pattern matching in text
# - csv         -> reading and writing spreadsheet-style files
# - statistics  -> mean, median, and more
# - argparse    -> building command-line tools
#
# Rule of thumb: before pip installing something, check whether the
# Standard Library already solves it. Browse: https://docs.python.org/3/library/
# =============================================================================
