# =============================================================================
# 04 - Functions
# =============================================================================
# Topic        : Functions, Default & Keyword Arguments, *args/**kwargs,
#                Lambda Functions, Variable Scope, Decorators,
#                Iterators & Generators
# File         : 04_functions.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Defining & Calling Functions
# -----------------------------------------------------------------------------
# A function is a named, reusable block of code. We define it once with "def",
# then "call" it as many times as we want instead of retyping the same lines.
# The values we list in the parentheses when defining it are called
# PARAMETERS. The actual values we pass in when calling it are called
# ARGUMENTS. The text in triple quotes right under "def" is called a
# docstring - it's optional, but it's good practice to describe what the
# function does.

def greet_user(name, hobby):
    """Print a personalized greeting for the given name and hobby."""
    print(f"Hi {name}! It's great that you enjoy {hobby}.")

greet_user("Maya", "painting")    # "Maya" and "painting" are the arguments
greet_user("Liam", "chess")


# -----------------------------------------------------------------------------
# 2. Default Parameter Values & Keyword Arguments
# -----------------------------------------------------------------------------
# A parameter can have a DEFAULT VALUE - if we don't pass anything for it,
# Python just uses the default instead.
# We can also pass arguments by NAME instead of by position - these are
# called KEYWORD ARGUMENTS, and their order doesn't matter when we do this.

def make_introduction(name, greeting="Hello"):
    print(f"{greeting}, my name is {name}.")

make_introduction("Nora")                              # uses the default greeting
make_introduction("Omar", "Hey there")                  # overrides the default
make_introduction(name="Priya", greeting="Welcome")     # keyword arguments
make_introduction(greeting="Yo", name="Diego")          # order doesn't matter here


# -----------------------------------------------------------------------------
# 3. *args & **kwargs
# -----------------------------------------------------------------------------
# Sometimes we don't know in advance how many arguments will be passed in.
# *args collects any number of extra POSITIONAL arguments into a tuple.
# **kwargs collects any number of extra KEYWORD arguments into a dictionary.
# (The names "args" and "kwargs" are just convention - the "*" and "**" are
# what actually matter.)

def add_all_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add_all_numbers(1, 2, 3))           # 6
print(add_all_numbers(10, 20, 30, 40))    # 100 - works with any amount of numbers

def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Sara", age=29, city="Dhaka")
# prints:
# name: Sara
# age: 29
# city: Dhaka


# -----------------------------------------------------------------------------
# 4. Returning Values from a Function
# -----------------------------------------------------------------------------
# "return" sends a value back out of the function so we can store it or use
# it elsewhere. Without "return", a function just runs and gives nothing back
# (print() only displays something, it doesn't hand a value back to us).
# A function can also return MORE than one value at once, separated by commas
# - Python automatically packs them into a tuple.

def calculate_circle_stats(radius):
    area = 3.14159 * radius * radius
    circumference = 2 * 3.14159 * radius
    return area, circumference     # returning two values at once

circle_area, circle_circumference = calculate_circle_stats(5)
print("Area:", circle_area)                  # Area: 78.53975
print("Circumference:", circle_circumference) # Circumference: 31.4159


# -----------------------------------------------------------------------------
# 5. Functions Are Objects Too
# -----------------------------------------------------------------------------
# In Python, a function is just another value - like a number or a string.
# That means we can store it in a variable, or even pass it INTO another
# function as an argument. This is what makes "higher-order functions"
# possible: functions that take other functions as input.

def double(number):
    return number * 2

def apply_operation(func, value):
    # we don't know (or care) exactly what "func" does - we just call it
    result = func(value)
    print(f"Result: {result}")

multiply_by_two = double      # storing the function itself, not calling it
apply_operation(multiply_by_two, 10)    # Result: 20
apply_operation(double, 7)              # Result: 14 - we can pass the function directly


# -----------------------------------------------------------------------------
# 6. Nested Functions & Closures
# -----------------------------------------------------------------------------
# We can define one function INSIDE another. The inner function can "remember"
# variables from the outer function even after the outer function has
# finished running - this remembered connection is called a CLOSURE.
# "nonlocal" tells Python "don't make a new local variable, update the one
# from the function that wraps me."

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment     # we return the inner function itself, not a value

counter = make_counter()
print(counter())    # 1
print(counter())    # 2
print(counter())    # 3 - "count" was remembered between calls!


# -----------------------------------------------------------------------------
# 7. Lambda Functions
# -----------------------------------------------------------------------------
# A lambda is a small, unnamed, one-line function. It's handy for short bits
# of logic we only need once, especially when another function expects a
# function as one of its arguments.

square = lambda number: number * number
print(square(6))    # 36

# A common real use: telling sorted() exactly HOW to sort something.
words = ["banana", "kiwi", "apple", "fig"]
words_by_length = sorted(words, key=lambda word: len(word))
print(words_by_length)    # ['fig', 'kiwi', 'apple', 'banana'] - by length, not A-Z


# -----------------------------------------------------------------------------
# 8. Variable Scope
# -----------------------------------------------------------------------------
# A variable's SCOPE is where in the code it's visible/usable.
# - A "global" variable is created outside any function - every function can
#   READ it.
# - To actually CHANGE (reassign) a global variable from inside a function,
#   we must explicitly say "global variable_name" first.

favorite_color = "blue"    # this is a global variable

def show_color():
    print(f"My favorite color is {favorite_color}")    # just reading it - fine

def change_color():
    global favorite_color
    favorite_color = "green"    # without "global" above, this would create a
                                 # brand new LOCAL variable instead of changing
                                 # the original one

show_color()           # My favorite color is blue
change_color()
show_color()            # My favorite color is green - the global was updated


# -----------------------------------------------------------------------------
# 9. Decorators
# -----------------------------------------------------------------------------
# A decorator is a function that WRAPS another function to add extra behavior
# before and/or after it runs - without rewriting the original function.
# The "@decorator_name" line right above a function definition is just a
# shortcut for: my_function = decorator_name(my_function)
# *args and **kwargs (see section 3) let the wrapper accept ANY arguments and
# pass them straight through to whatever function it's wrapping.

def add_timestamp(func):
    def wrapper(*args, **kwargs):
        print("--- Starting task ---")
        result = func(*args, **kwargs)
        print("--- Task finished ---")
        return result
    return wrapper

@add_timestamp
def water_the_plants(plant_name):
    print(f"Watering the {plant_name}.")

water_the_plants("tomato plant")
# prints:
# --- Starting task ---
# Watering the tomato plant.
# --- Task finished ---


# -----------------------------------------------------------------------------
# 10. Iterators
# -----------------------------------------------------------------------------
# Lists, tuples, and sets are "iterable" - but they aren't iterators
# themselves. Calling iter() on one gives us an ITERATOR: an object that
# remembers its position and hands us one item at a time with next().
# A "for" loop is secretly doing exactly this behind the scenes for us.

playlist = ["Song A", "Song B", "Song C"]
playlist_iterator = iter(playlist)

print(next(playlist_iterator))    # "Song A"
print(next(playlist_iterator))    # "Song B"
print(next(playlist_iterator))    # "Song C"
# print(next(playlist_iterator))  # would raise StopIteration - nothing left!


# -----------------------------------------------------------------------------
# 11. Generators
# -----------------------------------------------------------------------------
# A generator function looks like a normal function, but uses "yield" instead
# of "return". Each time it yields, it PAUSES and hands back one value -
# remembering exactly where it left off for next time. This means it produces
# values one at a time, on demand, instead of building a whole list in memory
# up front. A "for" loop can consume a generator directly, or we can manually
# pull values out with next(), just like an iterator.

def countdown(start):
    while start > 0:
        yield start
        start -= 1
    print("Liftoff!")

for number in countdown(3):
    print(number)
# prints: 3, 2, 1, then "Liftoff!" last - the code after the final yield only
# runs once the for loop asks for "next" one more time and finds nothing left

launch_sequence = countdown(3)    # calling it doesn't run the code yet...
print(next(launch_sequence))      # 3 - ...it only runs up to the next "yield"
print(next(launch_sequence))      # 2


# =============================================================================
# Key Takeaways
# - A function packages reusable code; parameters are the placeholders,
#   arguments are the real values we pass in when calling it
# - A parameter can have a default value, and arguments can be passed by
#   name (keyword arguments) instead of by position
# - *args gathers extra positional arguments into a tuple; **kwargs gathers
#   extra keyword arguments into a dictionary - both let a function accept a
#   flexible number of inputs
# - return hands a value back out of a function - and can return several
#   values at once, packed into a tuple
# - Functions are values too: they can be stored in variables and passed into
#   other functions, which is what makes higher-order functions possible
# - A nested function can remember variables from its outer function even
#   after that outer function has finished - this is called a closure
# - A lambda is a quick, unnamed, one-line function, often used inline as an
#   argument to another function (like sorted())
# - Scope controls where a variable can be seen; use "global" inside a
#   function only when we need to change a global variable, not just read it
# - A decorator wraps a function to add behavior before/after it runs,
#   without touching the original function's own code
# - An iterator hands out one item at a time via next(); a for loop is doing
#   this automatically under the hood
# - A generator function uses "yield" to produce values lazily, one at a
#   time, pausing and resuming instead of building everything in memory first
# =============================================================================