# =============================================================================
# 07 - Four Pillars of OOP
# =============================================================================
# Topic        : Inheritance, Access Modifiers, Polymorphism, Abstract Classes
# File         : 07_four_pillars_of_oop.py
# Author       : Mrinmoy Shib
# Date         : 2026
# Repository   : fullstack-webdev-python-django-react-ai
# =============================================================================


# =============================================================================
# 1. Inheritance
# =============================================================================
# Inheritance means a child class automatically gets everything the parent
# class has — all its methods and attributes — without us having to rewrite them.
#
# Real-world analogy:
#   A "Vehicle" has wheels and can move.
#   A "Car" IS a vehicle, so it inherits wheels + movement.
#   We only need to add what makes a Car unique (e.g. number of doors).
#
# Syntax:
#   class Child(Parent):   ← put the parent name inside the parentheses
#       ...
#
# Types of inheritance (all shown below):
#   Single       → one child, one parent
#   Multi-level  → grandparent → parent → child (chain)
#   Multiple     → one child, two parents

# ── Single Inheritance ──────────────────────────────────────────────────────
# The child class gets the parent's method for free.

class Vehicle:
    def start_engine(self):
        print("Engine started. Vroom!")

class Car(Vehicle):          # Car inherits from Vehicle
    def open_trunk(self):
        print("Trunk opened.")

my_car = Car()
my_car.start_engine()    # Inherited from Vehicle — Expected output: Engine started. Vroom!
my_car.open_trunk()      # Car's own method      — Expected output: Trunk opened.


# ── Multi-level Inheritance ──────────────────────────────────────────────────
# A chain: GrandParent → Parent → Child.
# Each level inherits everything above it.

class Animal:
    def breathe(self):
        print("Breathing...")

class Mammal(Animal):           # Mammal inherits from Animal
    def feed_young_with_milk(self):
        print("Feeding young with milk.")

class Dog(Mammal):              # Dog inherits from Mammal (which already inherited from Animal)
    def bark(self):
        print("Woof!")

buddy = Dog()
buddy.breathe()               # From Animal   — Expected output: Breathing...
buddy.feed_young_with_milk()  # From Mammal   — Expected output: Feeding young with milk.
buddy.bark()                  # From Dog      — Expected output: Woof!


# ── Multiple Inheritance ─────────────────────────────────────────────────────
# One child class inherits from MORE than one parent.
# Useful when something is a combination of two independent things.
# Example: a SmartTV is both a Screen and a MediaPlayer.

class Screen:
    def display(self):
        print("Displaying visuals on screen.")

class MediaPlayer:
    def play_audio(self):
        print("Playing audio.")

class SmartTV(Screen, MediaPlayer):   # inherits from BOTH
    def stream(self):
        print("Streaming content online.")

tv = SmartTV()
tv.display()      # From Screen       — Expected output: Displaying visuals on screen.
tv.play_audio()   # From MediaPlayer  — Expected output: Playing audio.
tv.stream()       # SmartTV's own     — Expected output: Streaming content online.


# =============================================================================
# 2. Access Modifiers
# =============================================================================
# Access modifiers control WHO is allowed to read or change an attribute.
# Python does not enforce them the way Java or C++ does — they are HINTS
# (conventions) that tell other developers (and our future self) how an
# attribute is intended to be used.
#
# Three levels:
#
#   public_var      → no prefix   → anyone can access it freely
#   _protected_var  → one underscore  → "please only use inside the class
#                                        and its subclasses"
#   __private_var   → two underscores → "internal use only — Python will
#                                        mangle the name to make it harder
#                                        to access accidentally"
#
# Name Mangling:
#   Python renames  __attr  to  _ClassName__attr  under the hood.
#   So  obj.__card_no  fails, but  obj._BankAccount__card_no  still works.
#   This is not security — it's a safety net to prevent accidental access.

class UserProfile:
    def __init__(self, username, email, password):
        self.username   = username     # Public    — visible to everyone
        self._email     = email        # Protected — intended for class/subclass
        self.__password = password     # Private   — internal use only

    def show_public_info(self):
        # A method INSIDE the class can access all three levels freely
        print(f"Username : {self.username}")
        print(f"Email    : {self._email}")
        print(f"Password : {self.__password}")   # readable from inside

    def change_password(self, old_pw, new_pw):
        # Controlled access to the private attribute through a method
        if old_pw == self.__password:
            self.__password = new_pw
            print("Password updated successfully.")
        else:
            print("Incorrect current password.")

profile = UserProfile("mrinmoy", "m@example.com", "secret123")

# Accessing public — totally fine:
print(profile.username)           # Expected output: mrinmoy

# Accessing protected — works, but convention says don't:
print(profile._email)             # Expected output: m@example.com

# Accessing private directly — raises AttributeError:
# print(profile.__password)       # ← uncomment to see the error

# Accessing via name mangling — possible but not recommended:
print(profile._UserProfile__password)   # Expected output: secret123

# The right way — use the method the class provides:
profile.show_public_info()
# Expected output:
# Username : mrinmoy
# Email    : m@example.com
# Password : secret123

profile.change_password("secret123", "newsecret456")
# Expected output: Password updated successfully.

profile.change_password("wrongpassword", "hack")
# Expected output: Incorrect current password.


# =============================================================================
# 3. Polymorphism  (Method Overriding)
# =============================================================================
# Polymorphism means "many forms". In OOP, it means that different classes
# can share the same method NAME but each does something different with it.
#
# The most common form is METHOD OVERRIDING:
# a child class redefines a method it inherited from the parent.
# When we call that method, Python runs the CHILD's version, not the parent's.
#
# Why is this useful?
# We can write one loop that calls the same method on different objects and
# each object responds in its own way — clean and flexible code.
#
# super() lets the child call the PARENT's version of the method first,
# then add its own behaviour on top.

class Notification:
    def send(self, message):
        # Default behaviour — every notification can be sent "somehow"
        print(f"[Notification] Sending: {message}")

class EmailNotification(Notification):
    def send(self, message):
        # Overrides the parent's send() with email-specific behaviour
        print(f"[Email] Composing and sending email: '{message}'")

class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS] Sending text message: '{message}'")

class PushNotification(Notification):
    def send(self, message):
        # Uses super() to run the parent's version first, then adds its own step
        super().send(message)
        print(f"[Push] Also triggering push alert on device.")

# Polymorphism in action — same method call, different behaviour per object:
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification(),
]

for notif in notifications:
    notif.send("Your order has been shipped!")
    print()

# Expected output:
# [Email] Composing and sending email: 'Your order has been shipped!'
#
# [SMS] Sending text message: 'Your order has been shipped!'
#
# [Notification] Sending: Your order has been shipped!
# [Push] Also triggering push alert on device.


# =============================================================================
# 4. Abstract Classes
# =============================================================================
# An abstract class is a class that says: "here is the SHAPE of what we must
# build — but I won't build it for you."
#
# It defines a list of methods that every subclass MUST implement.
# If a subclass forgets to implement even one abstract method, Python raises
# a TypeError when we try to create an object from it.
#
# An abstract class CANNOT be instantiated directly — it only exists to be
# inherited from. It is a contract, not a product.
#
# When to use it:
#   Use an abstract class when we want to guarantee that every subclass
#   provides specific behaviour, but the exact behaviour differs per subclass.
#
# Syntax:
#   - Import ABC and abstractmethod from the abc module
#   - Inherit from ABC
#   - Decorate required methods with @abstractmethod

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base — all shapes MUST provide area() and perimeter()."""

    @abstractmethod
    def area(self):
        pass    # no implementation here — subclasses must provide it

    @abstractmethod
    def perimeter(self):
        pass

    # A concrete method IS allowed in an abstract class:
    def describe(self):
        print(f"I am a {type(self).__name__}.")
        print(f"  Area      : {self.area():.2f}")
        print(f"  Perimeter : {self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b, side_c):
        self.base   = base
        self.height = height
        self._sides = (side_a, side_b, side_c)

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return sum(self._sides)


# Trying to create a Shape directly would crash:
# s = Shape()   # ← TypeError: Can't instantiate abstract class

# Creating concrete subclasses works fine:
c = Circle(7)
r = Rectangle(5, 3)
t = Triangle(6, 4, 6, 5, 5)

c.describe()
# Expected output:
# I am a Circle.
#   Area      : 153.94
#   Perimeter : 43.98

r.describe()
# Expected output:
# I am a Rectangle.
#   Area      : 15.00
#   Perimeter : 16.00

t.describe()
# Expected output:
# I am a Triangle.
#   Area      : 12.00
#   Perimeter : 16.00

# Polymorphism + Abstract class working together:
print("\n--- All shapes in one loop ---")
shapes = [c, r, t]
for shape in shapes:
    print(f"{type(shape).__name__:12s}  area={shape.area():.2f}")

# Expected output:
# --- All shapes in one loop ---
# Circle        area=153.94
# Rectangle     area=15.00
# Triangle      area=12.00


# =============================================================================
# 5. Putting It All Together — a Mini System
# =============================================================================
# This section combines all four concepts in one coherent example:
# a simple payment processing system.
#
#   Abstract class → PaymentMethod (defines the contract)
#   Inheritance    → CreditCard, MobilePay, BankTransfer all extend it
#   Polymorphism   → each overrides process() differently
#   Access Control → _fee_rate is protected; __transaction_log is private

class PaymentMethod(ABC):
    """Abstract base — every payment method must be able to process a payment."""

    def __init__(self, owner):
        self.owner            = owner        # Public
        self._fee_rate        = 0.0          # Protected — subclasses may override
        self.__transaction_log = []          # Private   — only this class manages it

    @abstractmethod
    def process(self, amount):
        """Must be implemented by every subclass."""
        pass

    def _log(self, entry):
        # Protected helper — subclasses can call this but outside code should not
        self.__transaction_log.append(entry)

    def get_history(self):
        # Public method that exposes private data in a controlled way
        if not self.__transaction_log:
            print(f"No transactions yet for {self.owner}.")
        else:
            print(f"Transaction history for {self.owner}:")
            for record in self.__transaction_log:
                print(f"  {record}")


class CreditCard(PaymentMethod):
    def __init__(self, owner, card_last4):
        super().__init__(owner)
        self._card_last4 = card_last4
        self._fee_rate   = 0.015          # 1.5% fee

    def process(self, amount):
        fee   = amount * self._fee_rate
        total = amount + fee
        print(f"[Credit Card ****{self._card_last4}] Charging ${total:.2f} "
              f"(${amount:.2f} + ${fee:.2f} fee) for {self.owner}.")
        self._log(f"Credit card charge: ${total:.2f}")


class MobilePay(PaymentMethod):
    def __init__(self, owner, phone_number):
        super().__init__(owner)
        self._phone      = phone_number
        self._fee_rate   = 0.005          # 0.5% fee

    def process(self, amount):
        fee   = amount * self._fee_rate
        total = amount + fee
        print(f"[MobilePay {self._phone}] Sending ${total:.2f} "
              f"(${amount:.2f} + ${fee:.2f} fee) for {self.owner}.")
        self._log(f"MobilePay transfer: ${total:.2f}")


class BankTransfer(PaymentMethod):
    def __init__(self, owner, account_number):
        super().__init__(owner)
        self._account  = account_number
        self._fee_rate = 0.0              # no fee

    def process(self, amount):
        print(f"[Bank Transfer → {self._account}] Transferring ${amount:.2f} "
              f"(no fee) for {self.owner}.")
        self._log(f"Bank transfer: ${amount:.2f}")


# Using the system — all three behave differently but share the same interface:
payments = [
    CreditCard("Alice",   "4242"),
    MobilePay("Bob",     "+8801712345678"),
    BankTransfer("Carol", "BD-ACC-9987"),
]

print("--- Processing Payments ---")
for p in payments:
    p.process(1000)

print()
print("--- Transaction Histories ---")
for p in payments:
    p.get_history()

# Expected output:
# --- Processing Payments ---
# [Credit Card ****4242] Charging $1015.00 ($1000.00 + $15.00 fee) for Alice.
# [MobilePay +8801712345678] Sending $1005.00 ($1000.00 + $5.00 fee) for Bob.
# [Bank Transfer → BD-ACC-9987] Transferring $1000.00 (no fee) for Carol.
#
# --- Transaction Histories ---
# Transaction history for Alice:
#   Credit card charge: $1015.00
# Transaction history for Bob:
#   MobilePay transfer: $1005.00
# Transaction history for Carol:
#   Bank transfer: $1000.00


# =============================================================================
# Key Takeaways
# =============================================================================
# - INHERITANCE: a child class gets everything the parent has for free.
#   Use it to reuse code instead of rewriting it.
#   Syntax: class Child(Parent)
#
# - MULTI-LEVEL: grandparent → parent → child — each level builds on the last.
# - MULTIPLE: one child with two parents — use with care.
#
# - ACCESS MODIFIERS are naming conventions, not hard locks:
#     no prefix   → public    → use freely from anywhere
#     _single     → protected → use inside the class and subclasses only
#     __double    → private   → internal use; Python mangles the name
#
# - POLYMORPHISM (method overriding): a child redefines an inherited method.
#   Python always runs the CHILD's version when called on a child object.
#   Use super() to call the parent's version first, then extend it.
#
# - ABSTRACT CLASS: a class that defines a required interface but provides
#   no implementation for abstract methods.
#   - Import ABC and abstractmethod from the abc module.
#   - Decorate required methods with @abstractmethod.
#   - Cannot be instantiated directly — it forces every subclass to implement
#     the methods, guaranteeing a consistent interface.
# =============================================================================