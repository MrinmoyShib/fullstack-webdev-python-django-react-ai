# =============================================================================
# 06 - Python OOP Essentials
# =============================================================================
# Topic        : Intro to OOP, Instance Variables & Methods, Class Variables
#                & Methods, Constructors, Static Methods, Getters & Setters
# File         : 06_oop_essentials.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# =============================================================================
# 1. Introduction to OOP
# =============================================================================
# Before OOP, programs were written as long lists of instructions (procedural
# programming). That works for small scripts, but as programs grow it becomes
# hard to organise, reuse, and maintain code.
#
# OOP solves this by letting us model the real world in code:
#   - We describe a "thing" (its data + behaviour) inside a CLASS.
#   - We create real, usable copies of that thing called OBJECTS (instances).
#
# Real-world analogy:
#   Class  = a blueprint for a house  (describes rooms, windows, doors)
#   Object = an actual house built from that blueprint
#   Two houses can be built from the same blueprint but still be independent —
#   painting one red doesn't paint the other.
#
# Four pillars of OOP (we'll learn all of these over time):
#   1. Encapsulation  — bundle data + methods together; hide internal details
#   2. Abstraction    — expose only what the user needs, hide complexity
#   3. Inheritance    — a child class reuses and extends a parent class
#   4. Polymorphism   — different classes can share the same method name but
#                       behave differently
#
# This file focuses on the building blocks that underpin all four pillars.
#
# Python naming conventions (important for readable code):
#   snake_case   → variables & functions   e.g.  total_price, calculate_tax()
#   PascalCase   → class names             e.g.  ShoppingCart, BankAccount
#   UPPER_SNAKE  → constants               e.g.  MAX_RETRIES = 3
#   _underscore  → "private" attributes    e.g.  self._balance  (convention only)
#   camelCase    → common in Java/JS; avoid in Python


# =============================================================================
# 2. Our First Class & Object
# =============================================================================
# Defining a class is just writing a blueprint — nothing actually exists yet.
# Creating an object from the class is what brings it to life.
#
# Syntax:
#   class ClassName:
#       def method_name(self):   ← 'self' always comes first; Python fills it in
#           ...
#
# When we call  obj.method()  Python secretly translates it to
# ClassName.method(obj)  — that's why 'self' is needed.

class Laptop:
    def power_on(self):
        # 'self' refers to whichever Laptop object called this method
        print("Laptop is booting up...")

    def shutdown(self):
        print("Laptop is shutting down. Goodbye!")

# Create two independent Laptop objects from the same class
laptop_a = Laptop()    # object 1
laptop_b = Laptop()    # object 2  — completely separate from laptop_a

laptop_a.power_on()    # Expected output: Laptop is booting up...
laptop_b.shutdown()    # Expected output: Laptop is shutting down. Goodbye!

# Proof they are different objects in memory:
print(laptop_a is laptop_b)   # Expected output: False
print(type(laptop_a))         # Expected output: <class '__main__.Laptop'>


# =============================================================================
# 3. Instance Variables
# =============================================================================
# An instance variable is data that belongs to ONE specific object.
# Every object gets its own independent copy — changing one never affects another.
#
# We create an instance variable by assigning to  self.variable_name
# inside any method.  Once created, it can be read/changed from any method
# in the class (or from outside using  object.variable_name).

class Smartphone:
    def configure(self, brand, model, storage_gb):
        # Three instance variables created here:
        self.brand      = brand        # e.g. "Samsung"
        self.model      = model        # e.g. "Galaxy S24"
        self.storage_gb = storage_gb   # e.g. 256

    def show_specs(self):
        # Reading instance variables from a different method — totally fine
        print(f"Brand   : {self.brand}")
        print(f"Model   : {self.model}")
        print(f"Storage : {self.storage_gb} GB")
        print("-" * 30)

phone1 = Smartphone()
phone2 = Smartphone()

phone1.configure("Samsung", "Galaxy S24", 256)
phone2.configure("Apple",   "iPhone 16",  128)

phone1.show_specs()
# Expected output:
# Brand   : Samsung
# Model   : Galaxy S24
# Storage : 256 GB
# ------------------------------

phone2.show_specs()
# Expected output:
# Brand   : Apple
# Model   : iPhone 16
# Storage : 128 GB
# ------------------------------

# We can also read/set instance variables from OUTSIDE the class:
phone1.storage_gb = 512         # upgrade phone1's storage
print(phone1.storage_gb)        # Expected output: 512
print(phone2.storage_gb)        # Expected output: 128  ← unchanged


# =============================================================================
# 4. Instance Methods (in depth)
# =============================================================================
# An instance method is any function defined inside a class with `self` as its
# first parameter.  It can:
#   - Read instance variables      (self.x)
#   - Modify instance variables    (self.x = new_value)
#   - Call other instance methods  (self.other_method())
#   - Return values just like a regular function
#
# Methods make objects *active* — they can do things, not just hold data.

class BankAccount:
    def open_account(self, owner, starting_balance=0):
        self.owner   = owner
        self.balance = starting_balance
        print(f"Account opened for {self.owner}. Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")

    def get_balance(self):
        # Returns the balance so the caller can use it in their own logic
        return self.balance

acc1 = BankAccount()
acc2 = BankAccount()

acc1.open_account("Alice", 500)     # Expected output: Account opened for Alice. Balance: $500.00
acc2.open_account("Bob")            # Expected output: Account opened for Bob. Balance: $0.00

acc1.deposit(200)                   # Expected output: Deposited $200.00. New balance: $700.00
acc1.withdraw(50)                   # Expected output: Withdrew $50.00. Remaining balance: $650.00
acc1.withdraw(1000)                 # Expected output: Insufficient funds. Current balance: $650.00

# acc2 is completely unaffected by anything done to acc1
print(acc2.get_balance())           # Expected output: 0


# =============================================================================
# 5. Class Variables & Class Methods
# =============================================================================
# A CLASS VARIABLE is defined directly in the class body (not inside a method).
# It is SHARED across every object of that class — like a setting for the
# whole group rather than one individual.
#
# When to use a class variable vs an instance variable:
#   Instance variable  → data that differs per object   (e.g. each student's name)
#   Class variable     → data that is the same for all  (e.g. school name, tax rate)
#
# A CLASS METHOD is decorated with @classmethod.
# Its first parameter is `cls` (the class itself, not an instance).
# Use it when we want to read or modify class-level data.
#
# Important gotcha:
#   Setting  object.class_var = value  does NOT change the class variable —
#   it creates a NEW instance variable that shadows it for that object only.

class Employee:
    company_name  = "TechNova Inc."   # class variable — shared by all employees
    headcount     = 0                 # tracks total number of Employee objects

    @classmethod
    def get_company(cls):
        return cls.company_name

    @classmethod
    def rename_company(cls, new_name):
        cls.company_name = new_name

    @classmethod
    def total_employees(cls):
        return cls.headcount

    def hire(self, name, role):
        # Instance variables — unique per employee
        self.name = name
        self.role = role
        Employee.headcount += 1     # update the class variable every time someone is hired
        print(f"Hired {self.name} as {self.role} at {Employee.company_name}.")

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.role} at {self.company_name}.")

e1 = Employee()
e2 = Employee()
e3 = Employee()

e1.hire("Priya",  "Backend Developer")   # Expected output: Hired Priya as Backend Developer at TechNova Inc.
e2.hire("Carlos", "UI Designer")         # Expected output: Hired Carlos as UI Designer at TechNova Inc.
e3.hire("Sam",    "DevOps Engineer")     # Expected output: Hired Sam as DevOps Engineer at TechNova Inc.

print(Employee.get_company())            # Expected output: TechNova Inc.
print(Employee.total_employees())        # Expected output: 3

# Rename affects ALL employees instantly
Employee.rename_company("NovaSoft Ltd.")
e1.introduce()    # Expected output: Hi, I'm Priya, Backend Developer at NovaSoft Ltd.
e2.introduce()    # Expected output: Hi, I'm Carlos, UI Designer at NovaSoft Ltd.

# Shadowing demo — setting on one instance doesn't touch the class variable
e3.company_name = "Freelancer"
e3.introduce()    # Expected output: Hi, I'm Sam, DevOps Engineer at Freelancer.
e1.introduce()    # Expected output: Hi, I'm Priya, Backend Developer at NovaSoft Ltd.  (unchanged)


# =============================================================================
# 6. Constructors  (__init__)
# =============================================================================
# __init__ is a "dunder" (double-underscore) method — Python calls it
# AUTOMATICALLY the instant an object is created. We never call it manually.
#
# Its purpose: set up the object's starting state in one clean step.
#
# Without __init__ we'd have to call a setup method ourself every time, and
# if we forget, the object is in a broken half-initialised state.
#
# __init__ can have default parameter values just like any function.
#
# Step-by-step what happens when we write:
#   item = Product("Headphones", 79.99)
#   1. Python creates a blank Product object
#   2. Python calls  Product.__init__(item, "Headphones", 79.99)
#   3. __init__ assigns self.name = "Headphones", self.price = 79.99
#   4. The finished object is returned and stored in `item`

class Product:
    # Default stock of 0 means a product starts out of stock unless specified
    def __init__(self, name, price, stock=0):
        self.name  = name
        self.price = price
        self.stock = stock
        print(f"Product created: {self.name} @ ${self.price:.2f}  (stock: {self.stock})")

    def restock(self, quantity):
        self.stock += quantity
        print(f"Restocked {self.name}: +{quantity} units. Total stock: {self.stock}")

    def sell(self, quantity):
        if quantity > self.stock:
            print(f"Cannot sell {quantity} units — only {self.stock} in stock.")
            return
        self.stock -= quantity
        revenue = quantity * self.price
        print(f"Sold {quantity}x {self.name}. Revenue: ${revenue:.2f}. Remaining: {self.stock}")

    def display(self):
        print(f"{self.name:20s}  Price: ${self.price:7.2f}  Stock: {self.stock}")


# Constructor runs automatically — no extra setup call needed
p1 = Product("Mechanical Keyboard", 89.99, 50)
# Expected output: Product created: Mechanical Keyboard @ $89.99  (stock: 50)

p2 = Product("USB-C Hub", 34.99)
# Expected output: Product created: USB-C Hub @ $34.99  (stock: 0)

p2.restock(100)   # Expected output: Restocked USB-C Hub: +100 units. Total stock: 100
p1.sell(5)        # Expected output: Sold 5x Mechanical Keyboard. Revenue: $449.95. Remaining: 45
p1.sell(60)       # Expected output: Cannot sell 60 units — only 45 in stock.

p1.display()      # Expected output: Mechanical Keyboard    Price: $  89.99  Stock: 45
p2.display()      # Expected output: USB-C Hub              Price: $  34.99  Stock: 100


# =============================================================================
# 7. Static Methods
# =============================================================================
# A static method is a regular function that just happens to live inside a
# class.  It has NO access to `self` (instance) or `cls` (class).
#
# Use it for utility/helper logic that is logically related to the class
# but doesn't need any object data to do its job.
#
# Comparison:
#   Regular function    → lives at module level, unrelated to any class
#   Instance method     → needs self, works on one object's data
#   Class method        → needs cls, works on class-level data
#   Static method       → needs neither; pure utility, grouped inside the class
#
# We can call a static method on the class OR on an instance — both work.

class PasswordChecker:
    MIN_LENGTH = 8   # class variable used as a constant

    @staticmethod
    def has_min_length(password):
        # Checks length only — no object data needed
        return len(password) >= PasswordChecker.MIN_LENGTH

    @staticmethod
    def has_digit(password):
        return any(char.isdigit() for char in password)

    @staticmethod
    def has_uppercase(password):
        return any(char.isupper() for char in password)

    @staticmethod
    def is_strong(password):
        # Calls the other static methods — still no self or cls needed
        return (
            PasswordChecker.has_min_length(password) and
            PasswordChecker.has_digit(password) and
            PasswordChecker.has_uppercase(password)
        )

test_passwords = ["hello", "Hello1", "Secure99pass", "nouppercase9"]

for pw in test_passwords:
    result = PasswordChecker.is_strong(pw)
    print(f"{pw:20s}  Strong: {result}")

# Expected output:
# hello                 Strong: False
# Hello1                Strong: False
# Secure99pass          Strong: True
# nouppercase9          Strong: False


# =============================================================================
# 8. Getters & Setters  (@property decorator)
# =============================================================================
# WHY protect attributes at all?
# If we allow direct access to an attribute (e.g. account.balance = -500),
# nothing stops someone from setting it to a nonsensical value.
# Getters and setters let us add validation/logic around reads and writes.
#
# The traditional approach (other languages):
#   def get_balance(self): return self._balance
#   def set_balance(self, v): ...validate... self._balance = v
#
# The Pythonic approach — @property:
#   @property               → turns a method into a read-like attribute (getter)
#   @attribute.setter       → adds write access with validation
#   No setter defined       → attribute becomes READ-ONLY
#
# The single underscore prefix (_balance) is a convention meaning
# "treat this as private — don't access it directly".  Python won't stop us,
# but other developers (and our future self) will know not to.

class Thermostat:
    def __init__(self, location, initial_temp=20):
        self._location    = location     # read-only — set once at creation
        self._temperature = initial_temp

    # --- Read-only property (no setter) ---
    @property
    def location(self):
        return self._location
    # There is deliberately no @location.setter — trying to set it raises AttributeError

    # --- Read-write property with validation ---
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_temp):
        # Valid household range: -10 °C to 40 °C
        if new_temp < -10 or new_temp > 40:
            print(f"Error: {new_temp}°C is outside the safe range (-10 to 40°C). Ignored.")
        else:
            self._temperature = new_temp
            print(f"[{self._location}] Temperature set to {self._temperature}°C.")

    @property
    def status(self):
        # A computed property — derived from existing data, no stored variable needed
        if self._temperature < 18:
            return "Too cold"
        elif self._temperature > 26:
            return "Too hot"
        else:
            return "Comfortable"

    def display(self):
        print(f"Thermostat ({self._location}): {self._temperature}°C — {self.status}")


t1 = Thermostat("Living Room", 22)
t2 = Thermostat("Bedroom",     19)

t1.display()    # Expected output: Thermostat (Living Room): 22°C — Comfortable
t2.display()    # Expected output: Thermostat (Bedroom): 19°C — Comfortable

# Using the setter — reads exactly like a normal assignment but validation runs
t1.temperature = 28
# Expected output: [Living Room] Temperature set to 28°C.
print(t1.status)        # Expected output: Too hot

t1.temperature = 99     # Expected output: Error: 99°C is outside the safe range (-10 to 40°C). Ignored.
print(t1.temperature)   # Expected output: 28  (unchanged)

t2.temperature = 15
# Expected output: [Bedroom] Temperature set to 15°C.
print(t2.status)        # Expected output: Too cold

# Reading the read-only property works fine
print(t1.location)      # Expected output: Living Room
print(t2.location)      # Expected output: Bedroom

# Attempting to write to a read-only property:
# t1.location = "Kitchen"   ← uncomment to see:  AttributeError: can't set attribute


# =============================================================================
# 9. Putting It All Together — a Mini System
# =============================================================================
# This section builds a small Library Catalogue that uses every concept above
# in one coherent example so we can see how they interact.

class LibraryBook:
    """Represents a single book in a library's catalogue."""

    # Class variable — same for every book in this library
    library_name = "City Central Library"
    total_books  = 0

    def __init__(self, title, author, copies=1):
        self.title   = title
        self.author  = author
        self._copies = copies          # "private" — controlled via property
        LibraryBook.total_books += 1

    # --- @property: controlled access to _copies ---
    @property
    def copies(self):
        return self._copies

    @copies.setter
    def copies(self, n):
        if n < 0:
            print("Number of copies cannot be negative.")
        else:
            self._copies = n

    # --- Instance method ---
    def checkout(self):
        if self._copies == 0:
            print(f"Sorry, '{self.title}' is currently unavailable.")
        else:
            self._copies -= 1
            print(f"Checked out: '{self.title}'. Copies remaining: {self._copies}")

    def return_book(self):
        self._copies += 1
        print(f"Returned: '{self.title}'. Copies now available: {self._copies}")

    def info(self):
        availability = "Available" if self._copies > 0 else "Unavailable"
        print(f"[{availability}] '{self.title}' by {self.author} — {self._copies} copy/copies")

    # --- Class method ---
    @classmethod
    def catalogue_summary(cls):
        print(f"\n{cls.library_name} — Total titles in catalogue: {cls.total_books}")

    # --- Static method ---
    @staticmethod
    def is_valid_isbn(isbn):
        # A real ISBN-13 is 13 digits; this is a simplified check
        return isbn.isdigit() and len(isbn) == 13


# Create books (constructor runs automatically each time)
book1 = LibraryBook("Deep Work",        "Cal Newport",     copies=3)
book2 = LibraryBook("Sapiens",          "Yuval Noah Harari", copies=2)
book3 = LibraryBook("Clean Code",       "Robert C. Martin",  copies=1)

book1.info()    # Expected output: [Available] 'Deep Work' by Cal Newport — 3 copy/copies
book2.info()    # Expected output: [Available] 'Sapiens' by Yuval Noah Harari — 2 copy/copies
book3.info()    # Expected output: [Available] 'Clean Code' by Robert C. Martin — 1 copy/copies

book3.checkout()    # Expected output: Checked out: 'Clean Code'. Copies remaining: 0
book3.checkout()    # Expected output: Sorry, 'Clean Code' is currently unavailable.
book3.return_book() # Expected output: Returned: 'Clean Code'. Copies now available: 1

book1.copies = -5   # Expected output: Number of copies cannot be negative.
print(book1.copies) # Expected output: 3  (unchanged)

LibraryBook.catalogue_summary()
# Expected output:
# City Central Library — Total titles in catalogue: 3

print(LibraryBook.is_valid_isbn("9780141036144"))  # Expected output: True
print(LibraryBook.is_valid_isbn("123"))            # Expected output: False


# =============================================================================
# Key Takeaways
# =============================================================================
# - A CLASS is a blueprint; an OBJECT is a live instance created from it.
# - INSTANCE VARIABLES (self.x) are unique per object — each object has its own.
# - INSTANCE METHODS take `self` and can read/write the object's own data.
# - CLASS VARIABLES are shared by all objects of that class.
# - CLASS METHODS take `cls` and are used to read/modify class-level data.
# - __init__ (constructor) runs automatically on object creation — use it to
#   set up starting state and avoid half-initialised objects.
# - STATIC METHODS (@staticmethod) are utility functions grouped inside a class;
#   they have no access to self or cls.
# - @PROPERTY turns a method into a readable attribute (getter).
# - @attribute.SETTER adds controlled write access with optional validation.
# - Omitting a setter makes the property READ-ONLY.
# - A single underscore prefix (_x) signals "treat as private" by convention.
# - All four ideas work together: classes organise code, constructors initialise
#   state, properties protect data, and static/class methods handle shared logic.
# =============================================================================