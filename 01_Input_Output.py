# To print output
print("Hello, World!")
print('Single quotes work too!')

# Printing numbers (Numbers do not need quotes)
print(42)
print(3.14159)

# Multiple print statements (Each print statement defaults to a new line)
print("This is the first line.")
print("This is the second line.")
print("And this is the third.")

# Taking input from the user and storing it in a variable called 'username'
username = input("Please enter your username: ")

# Printing the user input
print("Username is :", username)

print("--- Addition Program ---")
# Using float() so the user can enter decimals or whole numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate and store the result and displaying the result 
total = num1 + num2

print(f"The sum of {num1} and {num2} is {total}.")

#Using eval in input to allow the user to enter an expression
#eval() evaluates a string as Python code.
num = eval(input("Enter a number: "))
print("Number is ",num) 

# Create a new line by using the \n escape character inside string
# Should be used inside double or single quotes
print("Hi \nThis is printed in next line")
