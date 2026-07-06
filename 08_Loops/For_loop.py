'''
Loops are used to execute a block of code repeatedly until a certain condition is met. 
In Python, there are two main types of loops: for loops and while loops.
"for loops" are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.
'''

# for loop
# It is ideal when you know in advance how many times the code needs to execute

# for loop with range() function
for i in range(5):  # This will iterate from 0 to 4
    print(f"Iteration {i + 1}: This is a for loop.")

# Generates numbers from the start value up to (but excluding) the stop value
for i in range(5, 9):
    print(i)  # Prints 5, 6, 7, 8

# Generates numbers with a specific increment/step size
for i in range(1, 10, 2):
    print(i)  # Prints 1, 3, 5, 7, 9 (skips by 2)

# Iterates through every element in a sequential list
print("\nIterating through a list")
colors = ["red", "green", "blue"]
for color in colors:
    print(color)  # Prints each color string

# Iterates through an immutable (unchangeable) tuple sequence
print("\nIterating through a tuple")
dimensions = (1920, 1080, 720, 480)
for dim in dimensions:
    print(dim)  # Prints 1920, then 1080, then 720, then 480

# Iterates through a text string character by character
print("\nIterating through a string")
for letter in "Code":
    print(letter)  # Prints 'C', 'o', 'd', 'e' on separate lines

# Iterates through an unordered collection of unique elements
print("\nIterating through a set")
unique_nums = {1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7}  # The duplicate '2' , '3' , '7' are automatically removed
for num in unique_nums:
    print(num)  # Prints 1, 2, 3, 4, 5, 6, 7 (order is not guaranteed)

# Iterates through keys and values using the .items() method
print("\nIterating through a dictionary")
user = {"name": "Alex", "age": 25}
for key, value in user.items():
    print(f"{key} is {value}")  # Prints key-value pairs

# Exits the loop entirely when a specific condition is met
print("\nExiting the loop")
for num in range(1, 10):
    if num == 4:
        break  # Stops the loop immediately at 4
    print(num)  # Prints 1, 2, 3

# Act as a temporary placeholder; does absolutely nothing
for num in range(3):
    if num == 1:
        pass  # TODO: Add logic here later without breaking syntax
    print(num)  # Prints 0, 1, 2

# A loop placed inside another loop; inner loop runs fully for every outer loop step
print("\nNested loops")
for row in range(4):
    for col in range(4):
        print(f"Row {row}, Col {col}")

# The else block runs ONLY if the loop finishes normally without hitting a 'break'
for item in (1, 2, 3, 4, 5):
    print(item)
else:
    print("Loop finished successfully!")  # This will run

# Iterates through a sequence backwards from the end to the start
for num in reversed([1, 2, 3]):
    print(num)  # Prints 3, 2, 1

# Keeps track of both the index position and the item value at the same time
items = ["a", "b", "c"]
for index, val in enumerate(items):
    print(f"Index {index}: Value {val}")


# Pairs up items from multiple lists side-by-side in parallel
names = ["Anna", "Bob"]
ages = [22, 28]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Program to check and display if numbers are even or odd
print("--- Even or Odd Check ---")
for num in range(1, 5):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Program to calculate the total sum of numbers from 1 to 10
print("--- Sum 1 to 10 ---")
total_sum = 0
for i in range(1, 11):
    total_sum += i  # Adds current number to the running total
print(f"Total Sum: {total_sum}")

# Program to calculate the factorial of a number (e.g., 5! = 5*4*3*2*1)
print("--- Factorial of 5 ---")
target = 5
factorial = 1
for i in range(1, target + 1):
    factorial *= i  # Multiplies the total by the current number
print(f"Factorial of {target} is {factorial}")

# Program to generate the multiplication table for a number
print("--- Table of 5 ---")
table_num = 5
for i in range(1, 11):
    print(f"{table_num} x {i} = {table_num * i}")

# Program to count the number of vowels in a text string
print("--- Count Vowels ---")
sentence = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in sentence:
    if char in vowels:
        vowel_count += 1  # Increments if the character is a vowel
print(f"Number of vowels: {vowel_count}")

# Program to print a right-angled triangle pattern made of stars
print("--- Star Pattern ---")
rows = 4
for i in range(1, rows + 1):
    print("*" * i)  # Multiplies the star character by the row index
