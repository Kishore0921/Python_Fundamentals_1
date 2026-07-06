'''
Sets and Dictionaries
Sets and Dictionaries are two important data structures in Python that allow you to store and manipulate collections of data.
It is important to understand the differences between these two data structures and when to use each one.
Main differences between Sets and Dictionaries:
1. Sets are unordered collections of unique elements, while dictionaries are unordered collections of key-value pairs.
2. Sets are defined using curly braces {} or the set() function, while dictionaries are defined using curly braces {} with key-value pairs separated by colons.
3. Sets store single values, while dictionaries store a value linked to a unique key (key: value).
4. Sets automatically remove duplicate values, while dictionaries automatically overwrite duplicate keys with the latest value.
5. Sets do not support indexing or slicing, while dictionary values are accessed using their keys instead of a numeric index.
6. Sets are mutable (elements can be added/removed), but the elements inside a set must themselves be immutable (e.g. numbers, strings, tuples).
7. Dictionary keys must be immutable (e.g. numbers, strings, tuples), but dictionary values can be of any data type, including lists or other dictionaries.
8. Both sets and dictionaries are unordered in the sense that they do not maintain elements based on a numeric position/index like lists and tuples do.
'''

# Sets
print("\n======Sets======")
print("\nSets")

# Creating a Set
# Note: duplicate values are automatically removed when a set is created
fruits_set = {"Apple", "Mango", "Grapes", "Banana", "Orange"}
print("Original Set:", fruits_set)

# Creating a Set using set() constructor
# set() can convert other iterables (like lists or tuples) into a set
numbers_set = set([1, 2, 3, 4, 5])
print("Set using set() constructor:", numbers_set)

# Creating an Empty Set
# Important: {} creates an empty dictionary, NOT an empty set, so set() must be used instead
empty_set = set()
print("Empty Set:", empty_set)

# Set with Mixed Data Types
# Sets can hold different data types together, as long as each element is immutable/hashable
mixed_set = {10, 3.14, "Python", True}
print("Mixed Set:", mixed_set)

# Note on Nested Sets
# Sets cannot contain other sets directly because sets are mutable and their elements must be
# immutable/hashable. Python provides an immutable variant called frozenset() for this purpose,
# but frozenset is outside the scope of this file, so nested sets are not demonstrated here.
print("\nNote: Nested sets are not possible with regular sets because sets are mutable;")
print("Python offers 'frozenset' for such cases, which is not covered here.")

# Duplicate Removal
# A quick, common use of sets is removing duplicate values from a collection
print("\nDuplicate Removal:")
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers_with_duplicates)
print("Original List with Duplicates:", numbers_with_duplicates)
print("Set after Removing Duplicates:", unique_numbers)

# Accessing Elements
# Sets are unordered, so they do NOT support indexing or slicing like lists and tuples
print("\nAccessing Set Elements:")
print("Sets do not support indexing, e.g. fruits_set[0] would raise a TypeError")
# The following line is commented out because it would cause an error:
# print(fruits_set[0])  # TypeError: 'set' object is not subscriptable
print("To check for a value, use membership testing instead (see below)")

# Membership Operators
# Since sets don't support indexing, 'in' and 'not in' are the standard way to check for values
print("\nMembership Operators:")
print("'Apple' in fruits_set:", "Apple" in fruits_set)
print("'Kiwi' not in fruits_set:", "Kiwi" not in fruits_set)

# Adding Elements
print("\nMethods for Adding Elements:")
# add() adds a single element to the set
fruits_set.add("Kiwi")
print("After add():", fruits_set)

# update() adds multiple elements from another iterable (list, tuple, or another set)
fruits_set.update(["Papaya", "Guava"])
print("After update():", fruits_set)

# ADDED: update() using another set
# update() can also merge in all the elements of another set directly
update_set_a = {1, 2}
update_set_b = {3, 4}

update_set_a.update(update_set_b)

print("After update() using another set:", update_set_a)

# Removing Elements
print("\nMethods for Removing Elements:")
# remove() removes the specified element; raises an error if the element is not found
fruits_set.remove("Banana")
print("After remove():", fruits_set)

# discard() also removes the specified element, but does NOT raise an error if it is not found
fruits_set.discard("Watermelon")
print("After discard() of a non-existent element (no error):", fruits_set)

# pop() removes and returns a random element (sets are unordered, so you cannot choose which one)
popped_item = fruits_set.pop()
print("Popped Item:", popped_item)
print("After pop():", fruits_set)

# clear() removes all elements from the set
copy_set = fruits_set.copy()
copy_set.clear()
print("After clear():", copy_set)

# Set Operations
# These combine two sets together in different ways using either operators or methods
print("\nSet Operations:")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union: all unique elements from both sets
print("Union (|):", set1 | set2)

# Intersection: only the elements common to both sets
print("Intersection (&):", set1 & set2)

# Difference: elements in set1 but not in set2
print("Difference (-):", set1 - set2)

# Symmetric Difference: elements in either set, but not in both
print("Symmetric Difference (^):", set1 ^ set2)

# Set Methods
# These do the same operations as above, but as explicit method calls instead of operators
print("\nSet Methods:")
print("union():", set1.union(set2))
print("intersection():", set1.intersection(set2))
print("difference():", set1.difference(set2))
print("symmetric_difference():", set1.symmetric_difference(set2))

# issubset() checks if all elements of one set exist in another set
subset_check = {1, 2}
print("{1, 2}.issubset(set1):", subset_check.issubset(set1))

# issuperset() checks if a set contains all elements of another set
print("set1.issuperset({1, 2}):", set1.issuperset(subset_check))

# isdisjoint() checks if two sets have no elements in common
print("set1.isdisjoint(set2):", set1.isdisjoint(set2))

# Set Comparison
# Sets can be compared for equality; order does not matter since sets are unordered
print("\nSet Comparison:")
set_a = {1, 2, 3}
set_b = {3, 2, 1}
set_c = {4, 5, 6}
print("set_a == set_b:", set_a == set_b)
print("set_a == set_c:", set_a == set_c)
print("set_a != set_c:", set_a != set_c)

# ADDED: Order Doesn't Matter in Sets
# Since sets are unordered, two sets with the same elements are equal regardless of the
# order in which those elements were added
print("\nOrder Does Not Matter in Sets:")
order_set_a = {1, 2, 3}
order_set_b = {3, 2, 1}
print("Set A:", order_set_a)
print("Set B:", order_set_b)
print("Are both sets equal?", order_set_a == order_set_b)

# Copying Sets
# copy() creates a new, independent set so changes to the copy do not affect the original
print("\nCopying Sets:")
original_set = {"Python", "Java", "C++"}
copy_of_set = original_set.copy()
print("Original:", original_set)
print("Copy:", copy_of_set)

# Built-in Functions
print("\nBuilt-in Functions for Sets:")
marks_set = {85, 92, 78, 95, 88}

print("Length:", len(marks_set))
print("Maximum:", max(marks_set))
print("Minimum:", min(marks_set))
print("Sum:", sum(marks_set))

# Conversion
# Sets can be converted to/from other collection types
print("\nSet Conversion:")
list_to_convert = [1, 2, 2, 3, 3, 3]
converted_set = set(list_to_convert)
print("List:", list_to_convert)
print("Converted to Set (duplicates removed):", converted_set)

converted_list = list(converted_set)
print("Converted back to List:", converted_list)

converted_tuple = tuple(converted_set)
print("Converted to Tuple:", converted_tuple)

