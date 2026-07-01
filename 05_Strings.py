'''
Strings are sequences of characters used to represent text in programming. 
In Python, strings are enclosed in either single quotes (' ') or double quotes (" "). 
They can contain letters, numbers, symbols, and whitespace. 
Strings are immutable, meaning that once they are created, their content cannot be changed.
It can be used as a data type to store and manipulate text-based information.
'''
# Single and double quotes (Identical behavior)
str1 = 'Hello'
str2 = "World"

# Triple quotes (For multi-line text and docstrings)
multiline_str = """This string spans
across multiple lines."""

print(f"String 1 {str1} and String 2 {str2}")
print(f"Multiline String: {multiline_str}")

# Concatenation (+) - Joins strings together
joined = "Python" + " " + "Programming"  # 'Python Programming'
print(f"\nConcatenated String: {joined}")

# Repetition (*) - Duplicates text
repeated = "Hi! " * 3  # 'Hi! Hi! Hi! '
print(f"\nRepeated String: {repeated}")

# Membership (in / not in) - Checks for a substring
text = "Data Science"
print("Data" in text)      # True
print("Java" not in text)  # True

# Indexing and Slicing - Accessing parts of a string
sample = "Python"

# Positive Indexing (Starts from 0, left-to-right)
print(sample[0])   # 'P'

# Negative Indexing (Starts from -1, right-to-left)
print(sample[-1])  # 'n'

# Slicing Syntax: string[start : end(exclusive) : step]
print(sample[0:4])   # 'Pyth' (Indices 0, 1, 2, 3)
print(sample[:3])    # 'Pyt'  (Defaults start to 0)
print(sample[2:])    # 'thon' (Defaults end to the finish)
print(sample[::2])   # 'Pto'  (Skips every second letter)
print(sample[::-1])  # 'nohtyP' (Tricks to reverse a string)
print(sample[-3:-1]) # 'ho' (Negative slicing)
print(sample[-1:-4:-1]) # 'noh' (Negative slicing in reverse)

# String Methods - Built-in functions to manipulate strings
text = "lEArn PYthON"

print(text.lower())       # 'learn python'
print(text.upper())       # 'LEARN PYTHON'
print(text.capitalize())  # 'Learn python' (First letter only)
print(text.title())       # 'Learn Python' (First letter of each word)
print(text.swapcase())    # 'LEarn pyTHon'

# Stripping whitespace
whitespace_str = "   Hello, World!   "
print(f"Original String: '{whitespace_str}'") # '   Hello, World!   '
print(f"String after stripping: '{whitespace_str.strip()}'") # 'Hello, World!'
print(f"String after left stripping: '{whitespace_str.lstrip()}'") # 'Hello, World!   '
print(f"String after right stripping: '{whitespace_str.rstrip()}'") # '   Hello, World!'

# Splitting and Joining Strings
sentence = "Python is a versatile language"
words = sentence.split()  # Splits on whitespace
print(f"Words: {words}")

# Joining strings
joined = " ".join(words)  # Joins with a space
print(f"Joined String: {joined}")

# String Formatting - Inserting variables into strings
name = "Alice"
age = int(input("Enter your age: "))
print(f"Hello, my name is {name} and I am {age} years old.")

# Escape Sequences - Special characters in strings
print("This is a line.\nThis is another line.\tTabbed text.")

# Raw Strings - Treats backslashes as literal characters
raw_str = r"C:\Users\Name\Documents"
print(raw_str)

# String Length - Using len() to find the number of characters
length = len(sample)
print(f"Length of the string: {length}")

# String Immutability - Strings cannot be changed in place
immutable_str = "Immutable"
# immutable_str[0] = "M"  # This would raise a TypeError

# String Comparison - Comparing strings lexicographically
str_a = "apple"
str_b = "banana"
print(str_a < str_b)  # True (lexicographic comparison)

# Finding the index of a substring
# find() returns the starting index if found, otherwise it returns -1
text = "Python Programming"

print(text.find("Program"))      # Output: 7
print(text.find("Java"))         # Output: -1

# index() is similar to find(), but raises an error if the substring is not found
print(text.index("Python"))      # Output: 0

# Counting occurrences of a character or substring
# count() returns how many times a character or word appears

text = "Programming"

print(text.count("m"))           # Output: 2
print(text.count("g"))           # Output: 2
print(text.count("Pro"))         # Output: 1

# Replacing part of a string
# replace(old, new) replaces all occurrences of the old value

text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)                  # Output: I like Python

# Checking how a string starts or ends
# startswith() and endswith() return True or False

filename = "notes.txt"

print(filename.startswith("note"))    # True
print(filename.startswith("book"))    # False

print(filename.endswith(".txt"))      # True
print(filename.endswith(".pdf"))      # False

# Checking the contents of a string

text1 = "Python"
text2 = "12345"
text3 = "Python123"
text4 = "HELLO"
text5 = "hello"
text6 = "     "

# Checks whether the string contains only letters
print(text1.isalpha())          # True

# Checks whether the string contains only digits
print(text2.isdigit())          # True

# Checks whether the string contains only letters and numbers
print(text3.isalnum())          # True

# Checks whether all letters are uppercase
print(text4.isupper())          # True

# Checks whether all letters are lowercase
print(text5.islower())          # True

# Checks whether the string contains only whitespace
print(text6.isspace())          # True

# Aligning text

word = "Python"

# Centers the text within the given width
print(word.center(20))

# Aligns text to the left
print(word.ljust(20))

# Aligns text to the right
print(word.rjust(20))

# Printing repeated symbols
# Useful for creating separators in console applications

print("=" * 4)
print("-" * 3)
print("*" * 2)

# Converting characters to ASCII values and vice versa

# ord() returns the ASCII (Unicode) value of a character
print(ord("A"))                 # Output: 65

# chr() returns the character for an ASCII value
print(chr(65))                  # Output: A

# Comparing strings

str_a = "apple"
str_b = "banana"

# Equality
print(str_a == str_b)           # False

# Not equal
print(str_a != str_b)           # True

# Lexicographical comparison (Dictionary order)
print(str_a < str_b)            # True

print(str_a > str_b)            # False

# Empty string

empty = ""

# len() returns the number of characters
print(len(empty))               # Output: 0

# Empty strings evaluate to False
print(bool(empty))              # Output: False

# zfill() pads the beginning of a string with zeros.

number = "25"

print(number.zfill(5))     # 00025

# Formatting strings using format()

name = "Alice"
age = 21

print("My name is {} and I am {} years old.".format(name, age))

# Finding smallest and largest characters alphabetically

text = "Python"

print(min(text))
print(max(text))

