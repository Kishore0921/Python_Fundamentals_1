'''
Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that helps in designing and organizing code in a modular,
reusable, and maintainable way. OOP allows us to create real-world models using classes and objects.

The main OOP concepts include:
- Classes and Objects
- Constructors
- Instance Variables
- Methods
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

Advantages of OOP:
1. Code Reusability
2. Better Code Organization
3. Easy Maintenance
4. Data Security through Encapsulation
5. Scalability for Large Applications

Key points about OOP:
1. A class is a blueprint/template used to create objects.
2. An object is a specific instance created from a class.
3. OOP is commonly built on four main pillars: Encapsulation, Inheritance, Polymorphism,
   and Abstraction.
4. OOP helps make code more organized, reusable, and easier to maintain for larger programs.
'''

from abc import ABC, abstractmethod

# Creating a Class
print("\n======Creating a Class======")
# A class is defined using the 'class' keyword, followed by the class name
class Car:
    pass

print("Class 'Car' has been defined")

# Creating an Object
print("\n======Creating an Object======")
# An object is created by calling the class name as if it were a function
car1 = Car()
print("Object 'car1' created from class Car:", car1)
print("Type of car1:", type(car1))

# __init__() Constructor
print("\n======__init__() Constructor======")
# __init__() is a special method that runs automatically when a new object is created
# It is commonly used to set up (initialize) the object's starting data
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Kishore", 20)
print("Student created using __init__():", student1.name, student1.age)

# self Keyword
print("\n======self Keyword======")
# 'self' refers to the current object itself; it lets a method access that object's own
# attributes and other methods. It is passed automatically and does not need to be provided
# by the caller.
class Person:
    def __init__(self, name):
        self.name = name

    def show_self(self):
        print("self refers to this exact object:", self)
        print("Accessing this object's name using self:", self.name)

person1 = Person("Alice")
person1.show_self()

# Instance Variables
print("\n======Instance Variables======")
# Instance variables are unique to each object and are usually defined inside __init__() using self
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("1984", "George Orwell")
print("book1's instance variables:", book1.title, "-", book1.author)
print("book2's instance variables:", book2.title, "-", book2.author)

# Instance Methods
print("\n======Instance Methods======")
# Instance methods are functions defined inside a class that operate on instance data via self
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rect1 = Rectangle(5, 3)
print("Area of rect1 using instance method:", rect1.calculate_area())

# Class Variables
print("\n======Class Variables======")
# Class variables are shared by ALL objects of a class, unlike instance variables which are unique
class Employee:
    company_name = "TechCorp"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

emp1 = Employee("Ravi")
emp2 = Employee("Meera")
print("emp1's company:", emp1.company_name)
print("emp2's company:", emp2.company_name)
print("Class variable accessed directly from the class:", Employee.company_name)

# Class Methods
print("\n======Class Methods======")
# Class methods use the @classmethod decorator and take 'cls' instead of 'self'
# They work with the class itself rather than a specific object, often used to modify class variables
class Company:
    company_name = "TechCorp"

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

print("Company name before:", Company.company_name)
Company.change_company_name("InnovateTech")
print("Company name after class method call:", Company.company_name)

# Static Methods
print("\n======Static Methods======")
# Static methods use the @staticmethod decorator; they don't use 'self' or 'cls' and behave
# like a regular function that is simply grouped inside the class for organization
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

print("Sum using static method MathHelper.add(4, 5):", MathHelper.add(4, 5))

# Encapsulation
print("\n======Encapsulation======")
# Encapsulation means bundling data and methods together, and controlling access to that data
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner          # Public Member - accessible from anywhere
        self._balance = balance     # Protected Member - convention: internal use, but accessible
        self.__pin = pin            # Private Member - name-mangled, not directly accessible outside

    # Getter - a basic method used to safely read a private value
    def get_pin(self):
        return self.__pin

    # Setter - a basic method used to safely update a private value
    def set_pin(self, new_pin):
        self.__pin = new_pin

account1 = BankAccount("Kishore", 5000, 1234)

# Public Members
print("\nPublic Member (accessible directly):")
print("account1.owner:", account1.owner)

# Protected Members
print("\nProtected Member (accessible, but signals 'internal use only' by convention):")
print("account1._balance:", account1._balance)

# Private Members
print("\nPrivate Member (not directly accessible from outside the class):")
# print(account1.__pin)  # This would raise an AttributeError
print("Trying account1.__pin directly would raise an AttributeError")
print("Private members are name-mangled internally as:", "_BankAccount__pin")

# Getters and Setters (Basic)
print("\nGetters and Setters:")
print("Getting pin using get_pin():", account1.get_pin())
account1.set_pin(9999)
print("Pin after using set_pin(9999):", account1.get_pin())

# Inheritance
print("\n======Inheritance======")

# Single Inheritance
print("\nSingle Inheritance:")
# A single child class inherits from a single parent class
class Animal:
    def eat(self):
        print("This animal eats food")

class Dog(Animal):
    def bark(self):
        print("The dog barks")

dog1 = Dog()
dog1.eat()   # inherited from Animal
dog1.bark()  # defined in Dog

# Multilevel Inheritance
print("\nMultilevel Inheritance:")
# A class inherits from a child class, which itself inherits from another parent class
class Puppy(Dog):
    def weep(self):
        print("The puppy weeps")

puppy1 = Puppy()
puppy1.eat()   # inherited from Animal (grandparent)
puppy1.bark()  # inherited from Dog (parent)
puppy1.weep()  # defined in Puppy

# Multiple Inheritance
print("\nMultiple Inheritance:")
# A single child class inherits from more than one parent class at the same time
class Swimmer:
    def swim(self):
        print("Can swim")

class Runner:
    def run(self):
        print("Can run")

class Athlete(Swimmer, Runner):
    pass

athlete1 = Athlete()
athlete1.swim()  # inherited from Swimmer
athlete1.run()   # inherited from Runner

# Hierarchical Inheritance
print("\nHierarchical Inheritance:")
# Multiple child classes inherit from the same single parent class
class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass

bike1 = Bike()
truck1 = Truck()
bike1.start()   # inherited from Vehicle
truck1.start()  # inherited from Vehicle

# Hybrid Inheritance (Introduction)
print("\nHybrid Inheritance (Introduction):")
# Hybrid inheritance is simply a combination of more than one type of inheritance together
# (for example, hierarchical + multiple inheritance combined in the same class hierarchy)
class Machine:
    def power_on(self):
        print("Machine powered on")

class Electric(Machine):
    def charge(self):
        print("Charging battery")

class Manual(Machine):
    def refuel(self):
        print("Refueling manually")

class HybridCar(Electric, Manual):
    pass

hybrid1 = HybridCar()
hybrid1.power_on()  # inherited from Machine, through both Electric and Manual
hybrid1.charge()    # inherited from Electric
hybrid1.refuel()    # inherited from Manual

# Polymorphism
print("\n======Polymorphism======")

# Method Overriding
print("\nMethod Overriding:")
# A child class can provide its own version of a method that already exists in the parent class
class Bird:
    def sound(self):
        print("Some generic bird sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot says: Hello!")

bird1 = Bird()
parrot1 = Parrot()
bird1.sound()    # uses Bird's version
parrot1.sound()  # uses Parrot's overridden version

# Duck Typing (Basic)
print("\nDuck Typing (Basic):")
# Duck typing means Python cares about whether an object has the right method/behavior,
# not what class/type it officially belongs to ("If it walks like a duck and quacks like a duck...")
class Duck:
    def make_sound(self):
        print("Quack quack")

class Human:
    def make_sound(self):
        print("Hello there!")

def perform_sound(entity):
    entity.make_sound()

perform_sound(Duck())
perform_sound(Human())

# Operator Overloading (Basic)
print("\nOperator Overloading (Basic):")
# Operator overloading lets us redefine how built-in operators (like +) behave for custom objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point1 = Point(2, 3)
point2 = Point(4, 5)
point3 = point1 + point2  # calls __add__() behind the scenes
print("Result of point1 + point2:", point3.x, point3.y)

# Abstraction
print("\n======Abstraction======")
# Abstraction means hiding complex implementation details and only exposing the essential
# features/behavior that need to be used

# abc Module
# The 'abc' module (Abstract Base Classes) provides tools to create abstract classes in Python
print("\nabc Module:")
print("Imported ABC and abstractmethod from the 'abc' module")

# Abstract Class
print("\nAbstract Class:")
# An abstract class cannot be instantiated directly; it is meant to be inherited by other classes
class Shape(ABC):
    # Abstract Method
    # An abstract method has no implementation in the abstract class; subclasses MUST override it
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# shape1 = Shape()  # This would raise a TypeError since Shape is abstract
circle1 = Circle(4)
print("Area of circle1 using the implemented abstract method:", circle1.area())

# super() Function
print("\n======super() Function======")
# super() lets a child class call methods/constructors from its parent class
class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor called for:", self.name)

class Child(Parent):
    def __init__(self, name, grade):
        super().__init__(name)  # calls Parent's __init__()
        self.grade = grade
        print("Child constructor called, grade:", self.grade)

child1 = Child("Rahul", "5th")

# isinstance()
print("\n======isinstance()======")
# isinstance() checks if an object is an instance of a particular class (or its subclasses)
print("isinstance(child1, Child):", isinstance(child1, Child))
print("isinstance(child1, Parent):", isinstance(child1, Parent))
print("isinstance(child1, str):", isinstance(child1, str))

# issubclass()
print("\n======issubclass()======")
# issubclass() checks if a class is a subclass of another class
print("issubclass(Child, Parent):", issubclass(Child, Parent))
print("issubclass(Parent, Child):", issubclass(Parent, Child))

# hasattr()
print("\n======hasattr()======")
# hasattr() checks whether an object has a given attribute or method
print("hasattr(child1, 'grade'):", hasattr(child1, "grade"))
print("hasattr(child1, 'salary'):", hasattr(child1, "salary"))

# getattr()
print("\n======getattr()======")
# getattr() retrieves the value of an attribute; an optional default avoids an AttributeError
print("getattr(child1, 'name'):", getattr(child1, "name"))
print("getattr(child1, 'salary', 'Not Found'):", getattr(child1, "salary", "Not Found"))

# setattr()
print("\n======setattr()======")
# setattr() sets (or creates) the value of an attribute on an object
setattr(child1, "grade", "6th")
print("child1.grade after setattr():", child1.grade)

# delattr()
print("\n======delattr()======")
# delattr() removes an attribute from an object
delattr(child1, "grade")
print("hasattr(child1, 'grade') after delattr():", hasattr(child1, "grade"))

# Object Comparison
print("\n======Object Comparison======")
# By default, '==' compares object identity (whether they are the same object in memory)
# unless the class defines its own __eq__() method to compare based on actual data
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

coord1 = Coordinate(1, 2)
coord2 = Coordinate(1, 2)
coord3 = coord1
print("coord1 == coord2 (different objects, same data, no __eq__ defined):", coord1 == coord2)
print("coord1 == coord3 (same object reference):", coord1 == coord3)
print("coord1 is coord3 (identity check):", coord1 is coord3)

# Built-in Class Attributes
print("\n======Built-in Class Attributes======")
class Laptop:
    """A simple class representing a laptop."""
    brand = "Generic"

    def __init__(self, model):
        self.model = model

laptop1 = Laptop("UltraBook")

# __dict__
print("\n__dict__:")
print("laptop1.__dict__ (instance attributes):", laptop1.__dict__)
print("Laptop.__dict__ includes class-level attributes and methods (shown partially below):")
print("'brand' in Laptop.__dict__:", "brand" in Laptop.__dict__)

# __doc__
print("\n__doc__:")
print("Laptop.__doc__:", Laptop.__doc__)

# __name__
print("\n__name__:")
print("Laptop.__name__:", Laptop.__name__)

# __module__
print("\n__module__:")
print("Laptop.__module__:", Laptop.__module__)

# Special (Magic/Dunder) Methods
print("\n======Special (Magic/Dunder) Methods======")

# __str__()
print("\n__str__():")
# __str__() defines a readable, user-friendly string version of an object, used by print()
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

fraction1 = Fraction(3, 4)
print("print(fraction1) uses __str__():", fraction1)

# __repr__()
print("\n__repr__():")
# __repr__() defines an unambiguous, developer-facing representation of an object, ideally one
# that could help recreate the object; it is used when an object is displayed without print()
class FractionWithRepr:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return "FractionWithRepr(" + str(self.numerator) + ", " + str(self.denominator) + ")"

fraction2 = FractionWithRepr(1, 2)
print("repr(fraction2) uses __repr__():", repr(fraction2))

# Object Deletion
print("\n======Object Deletion======")

# del
print("\ndel:")
# del removes a reference to an object; once no references remain, Python cleans it up from memory
class Temporary:
    def __init__(self, name):
        self.name = name

temp_obj = Temporary("TempObject")
print("Object exists:", temp_obj.name)
del temp_obj
print("temp_obj has been deleted using 'del' and can no longer be accessed")

# __del__() (Introduction)
print("\n__del__() (Introduction):")
# __del__() is a special method that Python calls automatically right before an object is
# destroyed/garbage-collected; it is often used for basic cleanup notifications
class Resource:
    def __init__(self, name):
        self.name = name
        print("Resource", self.name, "created")

    def __del__(self):
        print("Resource", self.name, "is being deleted")

resource1 = Resource("FileHandle")
del resource1