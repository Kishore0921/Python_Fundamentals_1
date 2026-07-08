'''
Functions are a way to group code into reusable blocks. 
They allow you to define a set of instructions that can be executed whenever the function is called. 
Functions can take inputs (parameters) and return outputs (return values).
'''

# Function Definition
def greet(name):
    print(f"Hello, {name}! Welcome to the world of Python functions.")
greet("Alice")  # Calling the function with the argument "Alice"
print("\nGreeting with user input:")
a = str(input("Enter your name: "))
greet(a)  # Calling the function with user input
