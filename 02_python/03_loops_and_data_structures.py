# =============================================================================
# 03 - Loops and Built-in Data Structures
# =============================================================================
# Topic        : while loop, break/continue, List, Tuple, Set, Dictionary, for loop
# File         : 03_loops_and_data_structures.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# -----------------------------------------------------------------------------
# 1. The while Loop
# -----------------------------------------------------------------------------
# A while loop repeats its block of code AS LONG AS its condition stays True.
# Always make sure something inside the loop eventually makes the condition
# False, or we'll create an infinite loop!

counter = 1

while counter <= 5:
    print(f"Counting: {counter}")
    counter += 1     # without this line, the loop would run forever

print("While loop finished!")


# -----------------------------------------------------------------------------
# 2. break & continue
# -----------------------------------------------------------------------------
# break    -> stops the loop completely, right where we are
# continue -> skips just the current round and jumps to the next one

i = 0
while i < 6:
    i += 1
    if i == 4:
        break          # loop stops entirely once i reaches 4
    print("break demo:", i)

print()

j = 0
while j < 6:
    j += 1
    if j == 4:
        continue       # skips printing only when j is 4, loop keeps going
    print("continue demo:", j)


# -----------------------------------------------------------------------------
# 3. Lists & Tuples
# -----------------------------------------------------------------------------
# Both store multiple items in order. A List uses [] and CAN be changed
# (mutable). A Tuple uses () and CANNOT be changed after creation (immutable).

colors_list = ["Red", "Green", "Blue"]
colors_tuple = ("Red", "Green", "Blue")

print(colors_list[0])     # 'Red'
print(colors_tuple[1])    # 'Green'

colors_list[0] = "Purple"     # this works fine, lists are mutable
print(colors_list)

# colors_tuple[0] = "Purple"  # this would raise an error - tuples can't change


# -----------------------------------------------------------------------------
# 4. Updating Values in a List
# -----------------------------------------------------------------------------
# we can update an item in a list by assigning a new value at its index.

shopping_list = ["Rice", "Milk", "Sugar", "Bread"]
print(shopping_list)

shopping_list[1] = "Almond Milk"
shopping_list[3] = "Whole Wheat Bread"

print(shopping_list)


# -----------------------------------------------------------------------------
# 5. List & Tuple Slicing
# -----------------------------------------------------------------------------
# Slicing grabs a range of items using [start:stop:step].

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:2])     # [10, 20]                  - index 0 up to (not incl.) 2
print(numbers[2:])      # [30, 40, 50, 60]          - everything from index 2 on
print(numbers[-1])      # 60                        - the last item
print(numbers[-3:-1])   # [40, 50]                  - negative index from the end
print(numbers[::2])     # [10, 30, 50]              - every 2nd item
print(numbers[::-1])    # [60, 50, 40, 30, 20, 10]  - the whole list, reversed


# -----------------------------------------------------------------------------
# 6. Operators on Lists & Tuples
# -----------------------------------------------------------------------------
# "+" joins two lists together. "*" repeats a list's items multiple times.

team_a = ["Alex", "Sam"]
team_b = ["Jordan", "Taylor"]

print(team_a + team_b)    # ['Alex', 'Sam', 'Jordan', 'Taylor']
print(team_a * 3)         # ['Alex', 'Sam', 'Alex', 'Sam', 'Alex', 'Sam']


# -----------------------------------------------------------------------------
# 7. Unpacking Lists & Tuples
# -----------------------------------------------------------------------------
# Unpacking lets we assign multiple variables from a list/tuple in one line.
# The "*" symbol scoops up "everything else" into its own list.

scores = (95, 88, 76, 60, 45)

highest, *the_rest = scores

print(highest)     # 95
print(the_rest)    # [88, 76, 60, 45]


# -----------------------------------------------------------------------------
# 8. Comparing Lists & Tuples
# -----------------------------------------------------------------------------
# Python compares lists/tuples item by item, from left to right, just like
# comparing words alphabetically.

list_a = [5, 6, 25, 51]
list_b = [1, 9, 18, 46, 25]

if list_a > list_b:
    print("list_a is bigger")
else:
    print("list_b is bigger")


# -----------------------------------------------------------------------------
# 9. List Methods
# -----------------------------------------------------------------------------
# These methods CHANGE the original list:
#   append()  - adds one item to the end
#   extend()  - adds every item from another list to the end
#   insert()  - inserts an item at a specific index
#   reverse() - flips the order of all items
#   pop()     - removes and returns an item (last item by default)
#   remove()  - removes the first matching item by value
#   clear()   - empties the whole list
#   sort()    - sorts the items in place
#
# These methods DO NOT change the original list:
#   index()   - finds the position of an item
#   count()   - counts how many times an item appears

groceries = ["Apple", "Banana"]

groceries.append("Cherry")            # ['Apple', 'Banana', 'Cherry']
groceries.extend(["Mango", "Guava"])  # adds multiple items at once
groceries.insert(1, "Pineapple")      # inserts 'Pineapple' at index 1
print(groceries)

groceries.sort()                      # sorts alphabetically, in place
print(groceries)

removed_item = groceries.pop()        # removes & returns the last item
print("Removed:", removed_item)
print(groceries)

print(groceries.index("Banana"))      # finds Banana's current position
print(groceries.count("Apple"))       # counts how many "Apple" entries exist


# -----------------------------------------------------------------------------
# 10. 2D Lists (Matrix)
# -----------------------------------------------------------------------------
# A 2D list is simply a list where each item is itself a list - perfect for
# representing grids, tables, or matrices.

seating_chart = [
    ["Alex",   "Sam",   "Jordan"],
    ["Taylor", "Casey", "Riley"],
]

print(seating_chart)              # the whole grid
print(seating_chart[1])           # the second row -> ['Taylor', 'Casey', 'Riley']
print(seating_chart[1][2])        # row 1, column 2 -> 'Riley'

# Grabbing one column from every row using a loop
middle_column = []
for row in seating_chart:
    middle_column.append(row[1])

print(middle_column)              # ['Sam', 'Casey']


# -----------------------------------------------------------------------------
# 11. Sets
# -----------------------------------------------------------------------------
# A Set is a collection that is unordered and only stores UNIQUE values.
# Duplicate values are automatically dropped.

unique_visitors = {"Alex", "Sam", "Alex", "Jordan"}
print(unique_visitors)    # 'Alex' only appears once, even though we wrote it twice


# -----------------------------------------------------------------------------
# 12. Set Operations
# -----------------------------------------------------------------------------
# Sets support classic math operations: union, intersection, and difference.

morning_class = {"Alex", "Sam", "Jordan"}
evening_class = {"Jordan", "Taylor", "Riley"}

print(morning_class | evening_class)               # union: everyone, no duplicates
print(morning_class.union(evening_class))          # same thing, method form

print(morning_class & evening_class)               # intersection: in BOTH classes
print(morning_class.intersection(evening_class))   # same thing, method form

print(morning_class - evening_class)               # difference: only in morning_class
print(morning_class.difference(evening_class))     # same thing, method form


# -----------------------------------------------------------------------------
# 13. Dictionaries
# -----------------------------------------------------------------------------
# A Dictionary stores data as key-value pairs, written as {key: value}.
# Instead of finding items by position (like a list), we find them by name.

student = {
    "name": "Tania",
    "course": "Full Stack Web Development",
    "batch": 11,
    "is_active": True,
}

print(student["name"])               # 'Tania'
print(type(student["batch"]))        # <class 'int'>
print(type(student["is_active"]))    # <class 'bool'>


# -----------------------------------------------------------------------------
# 14. Dictionary Operations
# -----------------------------------------------------------------------------
# .items()  - returns all key-value pairs
# .keys()   - returns only the keys
# .values() - returns only the values
# .update() - adds new key-value pairs or updates existing ones

print(student.items())
print(student.keys())
print(student.values())

student.update({
    "platform": "Online Class",
    "course": "Full Stack Web Development with AI"   # this overwrites the old value
})

print(student)


# -----------------------------------------------------------------------------
# 15. The for Loop & Iterating Items
# -----------------------------------------------------------------------------
# Lists, sets, and tuples are all "iterable" - a for loop can walk through
# every item in them, one at a time.

fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print("I want to eat some", fruit)


# -----------------------------------------------------------------------------
# 16. Looping Through a Dictionary
# -----------------------------------------------------------------------------
# .items() gives us both the key and the value together in each loop round.

for key, value in student.items():
    print(key, "->", value)


# -----------------------------------------------------------------------------
# 17. range() in a for Loop
# -----------------------------------------------------------------------------
# range(stop)               -> counts from 0 up to (not including) stop
# range(start, stop)        -> counts from start up to (not including) stop
# range(start, stop, step)  -> counts with a custom step size

for i in range(3):
    print("range(3):", i)          # 0, 1, 2

for i in range(2, 6):
    print("range(2, 6):", i)       # 2, 3, 4, 5

for i in range(0, 20, 5):
    print("range(0, 20, 5):", i)   # 0, 5, 10, 15


# =============================================================================
# Key Takeaways
# - while loops repeat based on a condition; for loops repeat over a collection
# - break exits a loop completely; continue skips only the current round
# - Lists are mutable (changeable); Tuples are immutable (locked after creation)
# - Sets automatically remove duplicates and support union/intersection/difference
# - Dictionaries store key-value pairs and are looked up by key, not position
# - range() is the standard way to loop a specific number of times
# =============================================================================