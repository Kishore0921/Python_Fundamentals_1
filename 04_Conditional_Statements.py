'''
Conditional Statements are used to perform different actions based on different conditions. 
In Python, we use if, elif, and else statements to implement conditional logic.
Control the execution flow of a Python program, allowing it to make choices and repeat operations. 
Python uses indentation (4 spaces) rather than curly braces to define the structural code blocks for these statements
'''
# if statement is used to execute a block of code only if a specified condition is true.
print("if statement execution")
x = 10
if x > 5:
    print("x is greater than 5")  # This line will be executed because the condition is true

a = 20
if a < 15:
    print("a is less than 15")  # This line will not be executed because the condition is false

# if-else statement is used to execute one block of code if a condition is true, 
# and another block of code if the condition is false.
print("\nif-else statement execution")
p = 8
if p % 2 == 0:
    print("p is an even number")  # This line will be executed because the condition is true
else:
    print("p is an odd number")  # This line will not be executed

y = 7
if y % 2 == 0:
    print("y is an even number")  # This line will not be executed because the condition is false
else:
    print("y is an odd number")  # This line will be executed

# if-elif-else statement is used to check multiple conditions.
print("\nif -elif-else statement execution")
num = 15
if num > 20:
    print("num is greater than 20")  # This line will not be executed because the condition is false
elif num > 10:
    print("num is greater than 10")  # This line will be executed because the condition is true
else:
    print("num is not greater than 20 or 10")  # This line will not be executed

# Nested if statements are used to check multiple conditions within another if statement.
print("\nNested if statement execution")
score = 85
if score >= 80:
    if score >= 90:
        print("Excellent! You have an A grade.")
    else:
        print("Good job! You have a B grade.")
else:
    print("You need to improve your grade.")

# Ternary operator (conditional expression) is a one-liner shorthand for if-else statements.
print("\nTernary operator execution")
age = 18
status = "adult" if age >= 18 else "not adult"
print(status)

# Case statements (match-case) are used to match a value against multiple patterns 
# execute the corresponding block of code.
print("\nCase statement execution (match-case)")
OP = input("Enter the operator (+, -, *, /): ")  # Removed eval()
N1 = int(input("Enter the first number: "))
N2 = int(input("Enter the second number: "))
match OP:
    case "+":
        print("Addition", N1 + N2)
    case "-":
        print("Subtraction", N1 - N2)
    case "*":
        print("Multiplication", N1 * N2)
    case "/":
        print("Division", N1 / N2)
    case _:
        print("Invalid operator")  # '_' acts as the default 'else' case
        