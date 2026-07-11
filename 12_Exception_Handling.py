'''
Exception Handling
While a program is running, errors can occur that stop it from executing normally.
These runtime errors are called "exceptions". Exception Handling is the process of
anticipating, catching, and responding to these errors gracefully, instead of letting
the program crash.

What is an Exception?
An exception is an event that occurs during program execution which disrupts the normal
flow of the program's instructions (for example, dividing by zero, or accessing a key that
does not exist in a dictionary).

Why Exception Handling?
- It prevents the entire program from crashing when an error occurs.
- It allows the program to respond to errors in a controlled, predictable way.
- It helps show clear, user-friendly messages instead of confusing error tracebacks.
- It allows a program to clean up resources (like closing a file) even if an error happens.
'''

# 1. Theory - covered above in the module docstring
print("\n======1. Theory======")
print("An exception is an unexpected event that interrupts the normal flow of a program.")
print("Exception Handling lets us catch these events and respond instead of crashing.")


# 2. Basic try-except
print("\n======2. Basic try-except======")
# The 'try' block contains code that might cause an error
# The 'except' block contains code that runs ONLY IF an error occurs in the try block
try:
    result = 10 / 2
    print("Result of division:", result)
except:
    print("Something went wrong")


# 3. Handling ZeroDivisionError
print("\n======3. Handling ZeroDivisionError======")
# ZeroDivisionError occurs when a number is divided by zero
try:
    value = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide a number by zero")


# 4. Handling ValueError
print("\n======4. Handling ValueError======")
# ValueError occurs when a function receives an argument of the right type but an invalid value
try:
    number = int("Python")  # "Python" cannot be converted to an integer
except ValueError:
    print("Error: Invalid value, cannot convert this text to an integer")


# 5. Handling TypeError
print("\n======5. Handling TypeError======")
# TypeError occurs when an operation is performed on an incompatible data type
try:
    total = "5" + 5  # cannot add a string and an integer directly
except TypeError:
    print("Error: Cannot add a string and an integer together")


# 6. Handling IndexError
print("\n======6. Handling IndexError======")
# IndexError occurs when trying to access a list/tuple index that does not exist
try:
    numbers_list = [10, 20, 30]
    print(numbers_list[5])
except IndexError:
    print("Error: That index does not exist in the list")


# 7. Handling KeyError
print("\n======7. Handling KeyError======")
# KeyError occurs when trying to access a dictionary key that does not exist
try:
    student = {"name": "Kishore", "age": 20}
    print(student["grade"])
except KeyError:
    print("Error: That key does not exist in the dictionary")


# 8. Handling FileNotFoundError
print("\n======8. Handling FileNotFoundError======")
# FileNotFoundError occurs when trying to open a file that does not exist on disk
try:
    missing_file = open("this_file_does_not_exist.txt", "r")
except FileNotFoundError:
    print("Error: The file you are trying to open does not exist")


# 9. Multiple except Blocks
print("\n======9. Multiple except Blocks======")
# Multiple except blocks let a single try block handle different types of errors differently
try:
    marks = {"Math": 90, "Science": 85}
    print(marks["English"])
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except KeyError:
    print("Error: That subject was not found in the marks dictionary")
except TypeError:
    print("Error: A type mismatch occurred")


# 10. Using Exception as e
print("\n======10. Using Exception as e======")
# 'as e' stores the actual exception object in a variable, so its details can be printed/used
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught an exception using 'as e':", e)


# 11. else Block
print("\n======11. else Block======")
# The 'else' block runs ONLY IF the try block completes successfully, with no exceptions
try:
    result = 10 / 5
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("No errors occurred, division successful. Result:", result)


# 12. finally Block
print("\n======12. finally Block======")
# The 'finally' block always runs, whether an exception occurred or not - commonly used for cleanup
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("This finally block always runs, regardless of whether an error occurred")


# 13. Nested try-except
print("\n======13. Nested try-except======")
# A try-except block can be placed inside another try-except block for more specific handling
try:
    numbers_data = [10, 20, 30]
    index_to_access = 1
    try:
        print("Accessing index:", numbers_data[index_to_access])
        print("Now dividing by zero inside the nested try block:")
        print(10 / 0)
    except ZeroDivisionError as inner_error:
        print("Inner except caught:", inner_error)
except IndexError as outer_error:
    print("Outer except caught:", outer_error)


# 14. raise Keyword
print("\n======14. raise Keyword======")
# 'raise' is used to manually trigger an exception, even if Python itself wouldn't raise one
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Caught a manually raised exception:", e)


# 15. User-defined Exception
print("\n======15. User-defined Exception======")
# Custom exceptions are created by defining a new class that inherits from the Exception class
class InsufficientBalanceError(Exception):
    pass

def withdraw_amount(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Withdrawal amount exceeds available balance")
    return balance - amount

try:
    remaining_balance = withdraw_amount(1000, 1500)
except InsufficientBalanceError as e:
    print("Caught a user-defined exception:", e)


# 16. assert Statement
print("\n======16. assert Statement======")
# 'assert' checks if a condition is True; if it is False, it raises an AssertionError
# It is commonly used to catch bugs early by verifying assumptions in the code
try:
    marks_scored = 105
    assert marks_scored <= 100, "Marks cannot be greater than 100"
except AssertionError as e:
    print("Caught an AssertionError:", e)

# A passing assertion produces no error and the program continues normally
age_value = 20
assert age_value > 0, "Age must be positive"
print("Assertion passed: age_value is a valid positive number")


# 17. Best Practices
print("\n======17. Best Practices======")
print("1. Catch specific exceptions (like ValueError, KeyError) instead of a bare 'except:',")
print("   so you don't accidentally hide unrelated bugs.")
print("2. Keep the code inside the 'try' block as small as possible, so you only cover the")
print("   exact lines that might fail.")
print("3. Use 'finally' (or 'with' for files) to make sure resources are always cleaned up,")
print("   whether an error occurs or not.")
print("4. Avoid using exceptions for normal program logic; use them only for genuine error cases.")
print("5. Give clear, descriptive messages when raising exceptions, so they are easy to debug.")