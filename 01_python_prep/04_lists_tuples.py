# =============================================================================
# 04 - Lists & Tuples
# =============================================================================
# Topic        : Python Basics — Lists, Tuples & Range Method
# File         : 04_lists_tuples.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Lists — Definition & Declaration
# -----------------------------------------------------------------------------
# A list is a built-in, mutable data type used to store an ordered collection
# of items. Lists can hold mixed data types and allow duplicates.

a = [1, 2, 3, "Mark", "Micheal"]
print(a)        # Output: [1, 2, 3, 'Mark', 'Micheal']

# Lists are mutable — you can change values after creation
a[0] = 100
print(a)        # Output: [100, 2, 3, 'Mark', 'Micheal']

print(len(a))   # Output: 5 — total number of items

# Convert a string into a list of characters
s = "Hello"
print(list(s))  # Output: ['H', 'e', 'l', 'l', 'o']


# -----------------------------------------------------------------------------
# 2. List Methods
# -----------------------------------------------------------------------------
# Python provides 11 built-in methods to work with lists.

a = [1, 2, 3, "Mark", "Micheal"]


# append() — Adds a single element at the end of the list
a.append("Jason")
print(a)        # Output: [1, 2, 3, 'Mark', 'Micheal', 'Jason']


# insert() — Adds an element at the specified position
a.insert(2, "Inserted")
print(a)        # Output: [1, 2, 'Inserted', 3, 'Mark', 'Micheal', 'Jason']


# extend() — Adds all elements of another list to the end
a.extend(["Jack", "Jill"])
print(a)        # Output: [..., 'Jason', 'Jack', 'Jill']


# remove() — Removes the first item with the specified value
a.remove("Inserted")
print(a)        # Output: list without 'Inserted'


# pop() — Removes and returns the element at the specified position
#          If no index given, removes the last element
popped = a.pop()
print(popped)   # Output: Jill — last element removed
print(a)        # Output: list without 'Jill'

popped_index = a.pop(0)
print(popped_index)  # Output: 1 — element at index 0 removed


# index() — Returns the index of the first element with the specified value
a = [10, 20, 30, 20, 40]
print(a.index(20))   # Output: 1 — first occurrence of 20


# count() — Returns the number of times a value appears in the list
print(a.count(20))   # Output: 2 — 20 appears twice


# sort() — Sorts the list in ascending order (modifies original list)
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print(numbers)       # Output: [1, 2, 3, 5, 8, 9]

numbers.sort(reverse=True)
print(numbers)       # Output: [9, 8, 5, 3, 2, 1] — descending order


# reverse() — Reverses the order of the list
numbers.reverse()
print(numbers)       # Output: [1, 2, 3, 5, 8, 9]


# copy() — Returns a shallow copy of the list
original = [1, 2, 3]
copied   = original.copy()
copied.append(99)
print(original)      # Output: [1, 2, 3]    — original unchanged
print(copied)        # Output: [1, 2, 3, 99]


# clear() — Removes all elements from the list
temp = [1, 2, 3, 4, 5]
temp.clear()
print(temp)          # Output: [] — empty list


# -----------------------------------------------------------------------------
# 3. List Methods — Quick Reference Table
# -----------------------------------------------------------------------------

#  Method      | Description
# -------------|--------------------------------------------------------------
#  append()    | Adds an element at the end of the list
#  insert()    | Adds an element at the specified position
#  extend()    | Adds all elements of an iterable to the end of the list
#  remove()    | Removes the first item with the specified value
#  pop()       | Removes and returns element at specified position (default: last)
#  index()     | Returns the index of the first element with the specified value
#  count()     | Returns the number of elements with the specified value
#  sort()      | Sorts the list in ascending order (use reverse=True for descending)
#  reverse()   | Reverses the order of the list in place
#  copy()      | Returns a shallow copy of the list
#  clear()     | Removes all elements from the list


# -----------------------------------------------------------------------------
# 4. Tuples — Definition & Declaration
# -----------------------------------------------------------------------------
# A tuple is an immutable, ordered collection of items.
# Once created, its values CANNOT be changed — unlike lists.
# Tuples use parentheses () instead of square brackets [].

t = (1, 2, 3)
print(t)             # Output: (1, 2, 3)
print(type(t))       # Output: <class 'tuple'>

# Tuples are immutable — the line below would raise a TypeError:
# t[0] = 100         # TypeError: 'tuple' object does not support item assignment

# Reversing a tuple — must convert to a new tuple since tuples are immutable
t_reversed = tuple(reversed(t))
print(t_reversed)    # Output: (3, 2, 1)


# -----------------------------------------------------------------------------
# 5. List vs Tuple — Key Difference
# -----------------------------------------------------------------------------

my_list  = [1, 2, 3]   # Mutable   — can be changed after creation
my_tuple = (1, 2, 3)   # Immutable — cannot be changed after creation

my_list[0] = 99
print(my_list)         # Output: [99, 2, 3] — change allowed

# my_tuple[0] = 99     # This would raise a TypeError

# When to use which:
# - Use a LIST  when data needs to change (shopping cart, user inputs)
# - Use a TUPLE when data should stay fixed (coordinates, RGB colours, days of week)


# -----------------------------------------------------------------------------
# 6. Range Function
# -----------------------------------------------------------------------------
# range() is a built-in function used to generate a sequence of numbers.
# Syntax: range(start, stop, step)
# - start : where the sequence begins (default: 0)
# - stop  : where the sequence ends   (not included)
# - step  : how much to increment     (default: 1)

a = list(range(10))
b = tuple(range(10))
print(a)             # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b)             # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# range() with start, stop, and step
c = list(range(1, 10, 2))
print(c)             # Output: [1, 3, 5, 7, 9] — odd numbers only

# Counting down with a negative step
d = list(range(10, 0, -1))
print(d)             # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# =============================================================================
# Key Takeaways
# - list    : ordered, mutable, allows duplicates — uses square brackets []
# - tuple   : ordered, immutable, allows duplicates — uses parentheses ()
# - Use a list when data needs to change; use a tuple when it should stay fixed
# - append() adds one item; extend() adds many items from another iterable
# - pop() removes and RETURNS the item — useful when you need the removed value
# - sort() modifies the original list; sorted() returns a new sorted list
# - copy() creates an independent copy — changes won't affect the original
# - range(start, stop, step) generates number sequences; stop is NOT included
# - list() and tuple() can convert between types and from other iterables
# =============================================================================