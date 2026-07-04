'''
Lists and Tuples
Lists and tuples are both data structures in Python that can hold a collection of items. 
However, they have some key differences:
- Lists are mutable, meaning you can change their content after creation.
- Tuples are immutable, meaning their content cannot be changed after creation.
Lists are defined using square brackets [], while tuples are defined using parentheses ().
Lists can contain elements of different data types, including other lists, 
while tuples can also contain elements of different data types.
We can use lists and tuples to store and manipulate collections of data in Python.
We can perform various operations on lists and tuples, such as indexing, slicing, concatenation, repetition, and membership testing.
Like strings, lists and tuples can be nested, meaning we can have lists or tuples inside other lists or tuples.
Like strings, we can index and slice lists and tuples
'''

# Lists 
print("\n======Lists======")

# Creating a List
fruits = ["Apple", "Mango", "Grapes", "Banana", "Orange"]
print("Original List:", fruits)

# Creating a List using list() constructor
numbers = list((1, 2, 3, 4, 5))
print("List using list() constructor:", numbers)

# Creating an Empty List
empty_list = []
print("Empty List:", empty_list)

# List with Different Data Types
mixed_list = [10, 3.14, "Python", True]
print("Mixed List:", mixed_list)

# Nested List (List inside another list)
nested_list = ["Python", [1, 2, 3], "Programming"]
print("Nested List:", nested_list)

# ADDED: Accessing elements inside a Nested List
print("\nAccessing Nested List Elements:")
print("Element at index 1 (the inner list):", nested_list[1])
print("First element of the inner list:", nested_list[1][0])
print("Last element of the inner list:", nested_list[1][-1])

# Accessing List Elements
print("\nAccessing List Elements:")
print("First Element:", fruits[0])
print("Second Element:", fruits[1])
print("Last Element:", fruits[-1])
print("Second Last Element:", fruits[-2])

# List Slicing
print("\nList Slicing:")
print("First Three Elements:", fruits[:3])
print("Last Three Elements:", fruits[-3:])
print("Elements from Index 1 to 3:", fruits[1:4])
print("Every Second Element:", fruits[::2])
print("Reverse List:", fruits[::-1])

# Updating List Elements
fruits[1] = "Pineapple"
print("After Updating:", fruits)

# Adding Elements
print("\nMethods for Adding Elements:")
# append() adds one element at the end
fruits.append("Kiwi")
print("After append():", fruits)

# insert() adds an element at a specific position
fruits.insert(2, "Watermelon")
print("After insert():", fruits)

# extend() adds multiple elements
fruits.extend(["Papaya", "Guava"])
print("After extend():", fruits)

# Removing Elements
print("\nMethods for Removing Elements:")
# remove() removes the specified element
fruits.remove("Banana")
print("After remove():", fruits)

# pop() removes an element using its index
removed_item = fruits.pop(2)
print("Removed Item:", removed_item)
print("After pop():", fruits)

# pop() without index removes the last element
last_item = fruits.pop()
print("Last Removed Item:", last_item)
print("After pop() without index:", fruits)

# del removes an element permanently
# del removes an element or an entire list permanently
del fruits[0]
print("After del:", fruits)

# clear() removes all elements
# clear() removes all elements but keeps the list object
copy_list = fruits.copy()
copy_list.clear()
print("After clear():", copy_list)

# ADDED: del can also delete an entire list, removing it completely from memory
print("\nDeleting an Entire List:")
temp_list = ["Temporary", "Data", "To", "Delete"]
print("Before del:", temp_list)
del temp_list
# Trying to print temp_list now would raise a NameError since it no longer exists
print("temp_list has been completely deleted using 'del temp_list'")

# List Operators
print("\nList Operators:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
print("Concatenation:", list1 + list2)

# Repetition
print("Repetition:", list1 * 3)

# Membership Operators
print("2 in list1:", 2 in list1)
print("10 not in list1:", 10 not in list1)

# List Methods
print("\nList Methods:")
numbers = [40, 10, 30, 20, 50]
print("Original Numbers:", numbers)

# sort()
numbers.sort()
print("After sort():", numbers)

# reverse()
# reverse() reverses the current order of the list
numbers.reverse()
print("After reverse():", numbers)

# count()
print("Count of 30:", numbers.count(30))

# index()
print("Index of 40:", numbers.index(40))

# copy()
new_numbers = numbers.copy()
print("Copied List:", new_numbers)

# ADDED: sorted() function vs sort() method
print("\nsorted() vs sort():")
unsorted_numbers = [40, 10, 30, 20, 50]
print("Original List:", unsorted_numbers)

# sorted() returns a NEW sorted list and leaves the original list unchanged
sorted_result = sorted(unsorted_numbers)
print("Result of sorted():", sorted_result)
print("Original List after sorted() (unchanged):", unsorted_numbers)

# sort() sorts the list IN PLACE and returns None (it modifies the original list)
# sort() modifies the original list in ascending order
unsorted_numbers.sort()
print("Original List after sort() (changed in place):", unsorted_numbers)

# Built-in Functions
# MODIFIED: renamed header from "Built-in Functions for accessing lists:" to "Built-in Functions for Lists"
print("\nBuilt-in Functions for Lists:")
marks = [85, 92, 78, 95, 88]

print("Length:", len(marks))
print("Maximum:", max(marks))
print("Minimum:", min(marks))
print("Sum:", sum(marks))

# List Comparison
print("\nList Comparison:")
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = [3, 2, 1]
print("list_a == list_b:", list_a == list_b)
print("list_a == list_c:", list_a == list_c)
print("list_a != list_c:", list_a != list_c)

# Copying Lists
print("\nCopying Lists:")
original = ["Python", "Java", "C++"]

# copy1 refers to the same list as original
copy1 = original

# copy2 creates a separate copy of the list
copy2 = original.copy()

print("Original:", original)
print("copy1:", copy1)
print("copy2:", copy2)

# List Packing
packed = [10, 20, 30]
print("Packed List:", packed)

# ADDED: List Unpacking
print("\nList Unpacking:")
packed_list = [10, 20, 30]
first, second, third = packed_list
print("Packed List:", packed_list)
print("first:", first)
print("second:", second)
print("third:", third)

# List unpacking with * to collect remaining items
num_list = [1, 2, 3, 4, 5]
head, *middle, tail = num_list
print("head:", head)
print("middle:", middle)
print("tail:", tail)




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