'''
Functions
A function is a reusable block of code that performs a specific task. Functions help us
organize code, avoid repetition, and make programs easier to read and maintain.
Key points about functions:
1. Functions are defined using the 'def' keyword, followed by a name and parentheses.
2. Functions can accept input values called parameters/arguments.
3. Functions can send back a result using the 'return' statement, or return nothing at all.
4. Functions can be called (used) as many times as needed after they are defined.
5. Python also provides many built-in functions (like print(), len(), etc.) that are ready to use.
'''

# Defining a Function
print("\n======Defining a Function======")
# A function is defined using the 'def' keyword, a function name, and parentheses
def greet():
    print("Hello! Welcome to Python Functions.")

print("Function 'greet' has been defined")

# Calling a Function
print("\n======Calling a Function======")
# A function only runs when it is called using its name followed by parentheses
greet()
greet()

# Function with Parameters
print("\n======Function with Parameters======")
# Parameters allow a function to accept input values when it is called
def greet_person(name):
    print("Hello,", name + "!")

greet_person("Kishore")

# Function with Multiple Parameters
print("\n======Function with Multiple Parameters======")
# Functions can accept more than one parameter, separated by commas
def greet_with_age(name, age):
    print(name, "is", age, "years old.")

greet_with_age("Alice", 22)

# Function with Return Value
print("\n======Function with Return Value======")
# The 'return' statement sends a value back to wherever the function was called
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Result of add_numbers(5, 3):", result)

# Function without Return Value
print("\n======Function without Return Value======")
# A function without a 'return' statement automatically returns None
def display_message(message):
    print("Message:", message)

output = display_message("This function has no return value")
print("Value returned by display_message():", output)

# Positional Arguments
print("\n======Positional Arguments======")
# Positional arguments are matched to parameters based on their order/position
def describe_pet(animal, name):
    print(name, "is a", animal)

describe_pet("Dog", "Rocky")

# Keyword Arguments
print("\n======Keyword Arguments======")
# Keyword arguments are passed using the parameter name, so their order does not matter
describe_pet(name="Whiskers", animal="Cat")

# Default Parameters
print("\n======Default Parameters======")
# Default parameters provide a fallback value if no argument is given for that parameter
def greet_with_default(name="Guest"):
    print("Hello,", name + "!")

greet_with_default("Rahul")
greet_with_default()

# Variable-Length Arguments (*args)
print("\n======Variable-Length Arguments (*args)======")
# *args lets a function accept any number of positional arguments, collected as a tuple
def add_all(*args):
    print("Arguments received:", args)
    return sum(args)

print("Sum using add_all(1, 2, 3):", add_all(1, 2, 3))
print("Sum using add_all(10, 20, 30, 40):", add_all(10, 20, 30, 40))

# Keyword Variable-Length Arguments (**kwargs)
print("\n======Keyword Variable-Length Arguments (**kwargs)======")
# **kwargs lets a function accept any number of keyword arguments, collected as a dictionary
def print_student_info(**kwargs):
    print("Student Info:", kwargs)

print_student_info(name="Kishore", age=20, city="Bengaluru")

# Local Variables
print("\n======Local Variables======")
# A local variable is created inside a function and can only be accessed within that function
def local_variable_demo():
    local_message = "I am a local variable"
    print(local_message)

local_variable_demo()
# print(local_message)  # This would raise a NameError since local_message doesn't exist outside

# Global Variables
print("\n======Global Variables======")
# A global variable is defined outside any function and can be accessed inside functions
global_message = "I am a global variable"

def global_variable_demo():
    print(global_message)

global_variable_demo()

# Modifying a global variable inside a function requires the 'global' keyword
counter = 0

def increment_counter():
    global counter
    counter += 1

increment_counter()
increment_counter()
print("Counter after calling increment_counter() twice:", counter)

# Lambda Functions
print("\n======Lambda Functions======")
# A lambda function is a small, anonymous, single-expression function defined using 'lambda'
square = lambda x: x * x
print("Square of 5 using lambda:", square(5))

add_lambda = lambda a, b: a + b
print("Sum of 4 and 6 using lambda:", add_lambda(4, 6))

# Recursive Functions
print("\n======Recursive Functions======")
# A recursive function is a function that calls itself to solve a smaller version of the problem
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Nested Functions
print("\n======Nested Functions======")
# A nested function is a function defined inside another function
def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    inner_function()

outer_function()

# Function Returning Multiple Values
print("\n======Function Returning Multiple Values======")
# A function can return multiple values at once, separated by commas; they are packed into a tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = get_min_max([10, 25, 3, 48, 7])
print("Smallest:", smallest)
print("Largest:", largest)

result = get_min_max([10, 20, 30])
print("Returned Value:", result)
print("Type:", type(result))

# Docstrings
print("\n======Docstrings======")
# A docstring is a description placed as the first statement inside a function, written in
# triple quotes, explaining what the function does. It can be accessed using __doc__
def multiply(a, b):
    """Returns the product of two numbers a and b."""
    return a * b

print("Docstring of multiply():", multiply.__doc__)
print("Result of multiply(4, 5):", multiply(4, 5))

# Built-in Functions
print("\n======Built-in Functions======")
# Python provides many ready-to-use built-in functions that do not need to be defined manually
print("len('Python'):", len("Python"))
print("abs(-15):", abs(-15))
print("round(3.14159, 2):", round(3.14159, 2))
print("type(42):", type(42))

# Scope (LEGB - Basics)
print("\n======Scope (LEGB - Basics)======")
# Python looks up variable names in this order: Local -> Enclosing -> Global -> Built-in
scope_variable = "Global Scope"

def outer_scope_function():
    scope_variable = "Enclosing Scope"

    def inner_scope_function():
        scope_variable = "Local Scope"
        print("Inside inner_scope_function:", scope_variable)

    inner_scope_function()
    print("Inside outer_scope_function:", scope_variable)

outer_scope_function()
print("Outside all functions:", scope_variable)

# pass Statement in Functions
print("\n======pass Statement in Functions======")
# 'pass' is a placeholder that does nothing; it is used when a function needs a body but the
# logic has not been written yet, so the code does not raise a syntax/indentation error
def function_to_be_implemented():
    pass

print("function_to_be_implemented() defined using 'pass', ready to be filled in later")
function_to_be_implemented()

print("\n======Function Annotations======")

def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))

print("\n======*args and **kwargs Together======")

def details(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

details(1, 2, 3, name="Kishore", city="Bengaluru")

print("\n======Calling One Function from Another======")

def square(x):
    return x * x

def cube(x):
    return square(x) * x

print("Cube of 3:", cube(3))

print("\nAnother Lambda Example:")

numbers = [1, 2, 3, 4]

print(list(map(lambda x: x * x, numbers)))

def factorial(n):
    # Base case stops infinite recursion
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))