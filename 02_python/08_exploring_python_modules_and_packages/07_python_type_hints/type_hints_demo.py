# =============================================================================
# 08 - Exploring Python Modules and Packages
# =============================================================================
# Topic        : Python Type Hints
# File         : 07_python_type_hints/type_hints_demo.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================
#
# Python is dynamically typed — a variable's type never needs to be
# declared, and Python will not stop us from putting the wrong type into a
# function.
#
# Type hints do not change that at runtime. Python still will not enforce
# them on its own. What they do provide:
#   - An editor (VS Code, PyCharm) can warn about mistakes before the code
#     even runs.
#   - Tools like `mypy` can scan an entire project and catch type errors.
#   - Anyone reading a function instantly knows what to pass in and what
#     comes back out, without reading the full function body.
#
# Type hints are best thought of as documentation that a machine can also
# check.


# ── Basic type hints on variables ────────────────────────────────────────────
name: str = "Micheal"
age: int = 16
gpa: float = 3.9
is_student: bool = True

# Nothing stops this from happening — Python itself does not enforce hints:
age = "sixteen"   # No error at runtime, but the editor will flag this.
age = 16          # Reset for the rest of the demo


# ── Type hints on function parameters and return values ─────────────────────
# Syntax:  def function_name(param: Type) -> ReturnType:

def add(a: int, b: int) -> int:
    """Adds two numbers. The hints tell readers: pass ints, get an int back."""
    return a + b

print(add(5, 7))
# Expected output: 12

# add("Hi", 7)   # An editor or mypy would flag this as a type error, but
                 # Python would still run it (and only crash because
                 # str + int genuinely is not supported).


# ── Hinting collections: list, dict, tuple, set ──────────────────────────────
# Since Python 3.9+, built-in collection types can be hinted directly
# (older code used typing.List, typing.Dict — this style may still appear).

def average_marks(marks: list[int]) -> float:
    return sum(marks) / len(marks)

print(average_marks([80, 90, 70]))
# Expected output: 80.0


def get_user(user_id: int) -> dict[str, str | int]:
    return {"id": user_id, "name": "Micheal"}

print(get_user(1))
# Expected output: {'id': 1, 'name': 'Micheal'}


# ── Optional and Union: "this may be one of several types (or missing)" ─────
from typing import Optional, Union

# Optional[X] means "X, or None". Common for values that may be missing.
def find_user_email(username: str) -> Optional[str]:
    fake_database = {"micheal": "micheal@example.com"}
    return fake_database.get(username)   # Returns None if not found

print(find_user_email("micheal"))   # Expected output: micheal@example.com
print(find_user_email("unknown"))   # Expected output: None

# Union[X, Y] means "either X or Y". In modern Python this can also be
# written as "X | Y" directly (no import needed) — both mean the same thing.
def format_id(user_id: Union[int, str]) -> str:
    return f"USER-{user_id}"

def format_id_modern(user_id: int | str) -> str:
    return f"USER-{user_id}"

print(format_id(42))          # Expected output: USER-42
print(format_id("A100"))      # Expected output: USER-A100


# ── Callable: hinting that a parameter should be a function ─────────────────
from typing import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

def double(n: int) -> int:
    return n * 2

print(apply_twice(double, 3))
# Expected output: 12 (double(double(3)) -> double(6) -> 12)


# ── dataclasses: type hints that build a class automatically ────────────────
# A dataclass uses type hints on its fields to auto-generate __init__,
# __repr__, and __eq__ — removing common boilerplate.
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    gpa: float = 0.0   # Default value if not provided

s1 = Student("Micheal", 16, 3.9)
print(s1)
# Expected output: Student(name='Micheal', age=16, gpa=3.9)

s2 = Student("Alice", 17)
print(s2)
# Expected output: Student(name='Alice', age=17, gpa=0.0)


# ── Type aliases: giving a complex type a readable name ──────────────────────
# Useful when the same complicated type hint recurs frequently.
StudentRecord = dict[str, str | int | float]

def print_record(record: StudentRecord) -> None:
    for key, value in record.items():
        print(f"  {key}: {value}")

print_record({"name": "Micheal", "age": 16, "gpa": 3.9})
# Expected output:
#   name: Micheal
#   age: 16
#   gpa: 3.9


# =============================================================================
# Key Takeaways
# =============================================================================
# - Type hints are optional and are not enforced by Python at runtime.
# - They exist to help editors, static checkers (mypy), and other developers
#   understand code faster and catch mistakes earlier.
# - Syntax: variable: Type = value      |      def f(param: Type) -> Return:
# - list[int], dict[str, int]           -> hinting collections
# - Optional[X]  (same as X | None)     -> "may be missing"
# - Union[X, Y]  (same as X | Y)        -> "one of several types"
# - Callable[[ArgTypes], ReturnType]    -> hinting a function parameter
# - @dataclass turns type-hinted fields into a full class automatically
# - Running `pip install mypy` then `mypy your_file.py` checks type hints
#   across an entire project.
# =============================================================================
