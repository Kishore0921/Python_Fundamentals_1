

# Tuples
print("\n======Tuples======")
# Creating a Tuple
fruits_tuple = ("Apple", "Mango", "Grapes", "Banana", "Orange")
print("Original Tuple:", fruits_tuple)

# ADDED: Creating a Tuple using tuple() constructor
tuple_from_constructor = tuple([1, 2, 3, 4, 5])
print("Tuple using tuple() constructor:", tuple_from_constructor)

# Creating an Empty Tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# Tuple with Different Data Types
mixed_tuple = (10, 3.14, "Python", True)
print("Mixed Tuple:", mixed_tuple)

# Nested Tuple (Tuple inside another tuple)
nested_tuple = ("Python", (1, 2, 3), "Programming")
print("Nested Tuple:", nested_tuple)

# ADDED: Accessing elements inside a Nested Tuple
print("\nAccessing Nested Tuple Elements:")
print("Element at index 1 (the inner tuple):", nested_tuple[1])
print("First element of the inner tuple:", nested_tuple[1][0])
print("Last element of the inner tuple:", nested_tuple[1][-1])

# Single Element Tuple
single_tuple = ("Python",)
print("Single Element Tuple:", single_tuple)

# Accessing Tuple Elements
print("\nAccessing Tuple Elements:")
print("First Element:", fruits_tuple[0])
print("Second Element:", fruits_tuple[1])
print("Last Element:", fruits_tuple[-1])
print("Second Last Element:", fruits_tuple[-2])

# Tuple Slicing
print("\nTuple Slicing:")
print("First Three Elements:", fruits_tuple[:3])
print("Last Three Elements:", fruits_tuple[-3:])
print("Elements from Index 1 to 3:", fruits_tuple[1:4])
print("Every Second Element:", fruits_tuple[::2])
print("Reverse Tuple:", fruits_tuple[::-1])

# Tuple Operators
print("\nTuple Operators:")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
print("Concatenation:", tuple1 + tuple2)

# Repetition
print("Repetition:", tuple1 * 3)

# Membership Operators
print("2 in tuple1:", 2 in tuple1)
print("10 not in tuple1:", 10 not in tuple1)

# Tuple Methods
print("\nTuple Methods:")

numbers = (40, 10, 30, 20, 50, 30)

# count()
print("Count of 30:", numbers.count(30))

# index()
print("Index of 40:", numbers.index(40))

# ADDED: sorted() works on tuples too, but always returns a list (tuples have no sort() method
# because they are immutable and cannot be sorted in place)
print("\nsorted() with a Tuple:")
print("Original Tuple:", numbers)
sorted_tuple_result = sorted(numbers)
print("Result of sorted() (returned as a list):", sorted_tuple_result)
print("Original Tuple after sorted() (unchanged):", numbers)

# Built-in Functions
# MODIFIED: renamed header from "Built-in Functions for Tuples:" to "Built-in Functions for Tuples"
print("\nBuilt-in Functions for Tuples:")

marks = (85, 92, 78, 95, 88)

print("Length:", len(marks))
print("Maximum:", max(marks))
print("Minimum:", min(marks))
print("Sum:", sum(marks))

# Tuple Comparison
print("\nTuple Comparison:")

tuple_a = (1, 2, 3)
tuple_b = (1, 2, 3)
tuple_c = (3, 2, 1)

print("tuple_a == tuple_b:", tuple_a == tuple_b)
print("tuple_a == tuple_c:", tuple_a == tuple_c)
print("tuple_a != tuple_c:", tuple_a != tuple_c)

# Packing Tuples
print("\nTuple Packing:")

packed = (10, 20, 30)
print("Packed Tuple:", packed)

# Unpacking Tuples
print("\nTuple Unpacking:")

name, age, city = ("Kishore", 20, "Bengaluru")

print("Name:", name)
print("Age:", age)
print("City:", city)

# Swapping Variables Using Tuples
print("\nSwapping Variables:")

a = 10
b = 20

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)

# Tuple Immutability
print("\nTuple Immutability:")

student = ("Alice", 20)

print("Original Tuple:", student)

# The following statement will produce an error because tuples are immutable.

# student[0] = "Rahul"

# ADDED: List vs Tuple Mutability Comparison
print("\nList vs Tuple Mutability Comparison:")

demo_list = [1, 2, 3]
demo_tuple = (1, 2, 3)

print("Original List:", demo_list)
print("Original Tuple:", demo_tuple)

# Lists are mutable - this works fine
demo_list[0] = 100
print("List after modifying index 0:", demo_list, "(allowed, lists are mutable)")

# Tuples are immutable - attempting this would raise a TypeError
# demo_tuple[0] = 100  # Uncommenting this line would cause:
# TypeError: 'tuple' object does not support item assignment
print("Tuple cannot be modified the same way:", demo_tuple, "(not allowed, tuples are immutable)")

# Converting Between List and Tuple
print("\nList and Tuple Conversion:")

list_data = [1, 2, 3, 4]

tuple_data = tuple(list_data)

print("List:", list_data)
print("Converted Tuple:", tuple_data)

new_list = list(tuple_data)

print("Converted Back to List:", new_list)