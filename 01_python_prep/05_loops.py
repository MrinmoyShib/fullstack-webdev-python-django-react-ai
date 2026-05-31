# =============================================================================
# 05 - Loops
# =============================================================================
# Topic        : Python Basics — For Loop, While Loop, Break, Continue & List Comprehension
# File         : 05_loops.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# -----------------------------------------------------------------------------
# 1. For Loop — Definition & Declaration
# -----------------------------------------------------------------------------
# A for loop is used to iterate over a sequence (list, tuple, dictionary,
# set, or string) and execute a block of code for each item in that sequence.

a = (1, 2, 3)
for item in a:
    print(item)        # Output : 1, 2, 3 (each on a new line)

b = "Hello"
for item in b:
    print(item)        # Output : H, e, l, l, o (each on a new line)

# 'in' operator — checks if a value exists in a sequence
print('a' in b)        # Output : False — 'a' is not in "Hello"
print('H' in b)        # Output : True  — 'H' is in "Hello"


# -----------------------------------------------------------------------------
# 2. Range — Definition & Declaration
# -----------------------------------------------------------------------------
# The range() function generates a sequence of numbers.
# Most commonly used with for loops to repeat an action a specific number of times.
# Syntax: range(start, stop, step) — stop value is EXCLUDED

for item in range(1, 6):         # Output : 1, 2, 3, 4, 5 (6 is excluded)
    print(item)

for i in range(11):              # Output : 0, 1, 2 ... 10 (starts from 0 by default)
    print(f"Hacking...{i * 10}%")  
print("Hacked!")
# Output :
# Hacking...0%
# Hacking...10%
# Hacking...20%
# Hacking...30%
# Hacking...40%
# Hacking...50%
# Hacking...60%
# Hacking...70%
# Hacking...80%
# Hacking...90%
# Hacking...100%
# Hacked!


# -----------------------------------------------------------------------------
# 3. Break — Definition & Declaration
# -----------------------------------------------------------------------------
# The break statement exits a loop immediately when a condition is met.
# The rest of the loop — including remaining items — is skipped entirely.

a = [1, 2, 3, "Hello", 4, 5]

for i in a:
    if isinstance(i, str):
        break          # Stops the loop when a string is found
    print(i)
# Output : 1, 2, 3 (loop stops before "Hello", so 4 and 5 are never reached)


# -----------------------------------------------------------------------------
# 4. Continue — Definition & Declaration
# -----------------------------------------------------------------------------
# The continue statement skips the current iteration and moves to the next one.
# Unlike break, it does NOT stop the loop — it only skips that one item.

a = [10, 20, 30, "Hello", 40, 50]

for i in a:
    if isinstance(i, str):
        continue       # Skips "Hello" and continues with 40, 50
    print(i)
# Output : 10, 20, 30, 40, 50 (only "Hello" is skipped)


# -----------------------------------------------------------------------------
# 5. List Comprehension
# -----------------------------------------------------------------------------
# List comprehension offers a shorter, more concise syntax to create a new list
# based on the values of an existing list or any iterable.

# Without List Comprehension
a      = [1, 23, 324, 5346, 12, 65, 89, 2132]
result = []
for i in a:
    if i % 2 == 0:
        result.append(i)
print(result)          # Output : [324, 5346, 12, 2132]

# With List Comprehension — same result in one line
a          = [1, 23, 324, 5346, 12, 65, 89, 2132]
new_result = [i for i in a if i % 2 == 0]
print(new_result)      # Output : [324, 5346, 12, 2132]

# List Comprehension with condition — square evens, keep odds as-is
b      = [1, 2, 3, 4, 5]
square = [i**2 if i % 2 == 0 else i for i in b]
print(square)          # Output : [1, 4, 3, 16, 5]


# -----------------------------------------------------------------------------
# 6. While Loop — Definition & Declaration
# -----------------------------------------------------------------------------
# A while loop repeatedly executes a block of code as long as a condition is True.
# Unlike a for loop, it is used when the number of iterations is not known in advance.
# Always have to make sure the condition eventually becomes False — otherwise it loops forever.

a      = [1, 2, 3, 4, 5]
result = 0
i      = 0
n      = len(a)

while i < n:
    result = result + a[i]  # Adds each element to result
    i      = i + 1          # Increments i — prevents infinite loop
print(result)               # Output: 15 (1+2+3+4+5)


# =============================================================================
# Key Takeaways
# - for loop    : iterates over any sequence — list, tuple, string, range, etc.
# - range()     : generates numbers; range(start, stop, step) — stop is excluded
# - 'in'        : checks membership — returns True or False
# - break       : exits the loop completely when condition is met
# - continue    : skips only the current iteration, loop keeps going
# - List comp.  : concise one-line syntax to create/filter lists
# - while loop  : runs as long as a condition is True — use when iterations unknown
# - isinstance(): checks if a variable is of a specific type — isinstance(x, str)
# - Always have to increment the counter in a while loop to avoid an infinite loop
# =============================================================================