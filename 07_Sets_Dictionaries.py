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




# Dictionaries
print("\n======Dictionaries======")
print("\nDictionaries")

# Creating a Dictionary
# A dictionary stores data as key-value pairs, separated by colons, inside curly braces
student_dict = {"name": "Kishore", "age": 20, "city": "Bengaluru"}
print("Original Dictionary:", student_dict)

# Creating a Dictionary using dict() constructor
# dict() can build a dictionary from keyword arguments or from a list of key-value pairs
dict_from_constructor = dict(name="Alice", age=22, city="Mumbai")
print("Dictionary using dict() constructor:", dict_from_constructor)

# ADDED: Duplicate Keys
# The latest value overwrites the previous one.
print("\nDuplicate Keys:")
duplicate_keys = {
    "name": "Kishore",
    "name": "Rahul"
}
print("Dictionary with Duplicate Keys:", duplicate_keys)

# ADDED: Duplicate Values
# Dictionaries allow duplicate values.
print("\nDuplicate Values:")
marks_duplicate_values = {
    "Math": 90,
    "Science": 90,
    "English": 85
}
print("Dictionary with Duplicate Values:", marks_duplicate_values)

# ADDED: fromkeys()
# Creates a dictionary using a list of keys and one default value.
print("\nfromkeys():")
keys_for_dict = ["Name", "Age", "City"]
dict_from_keys = dict.fromkeys(keys_for_dict, "Not Assigned")
print("Dictionary using fromkeys():", dict_from_keys)

# Creating an Empty Dictionary
empty_dict = {}
print("Empty Dictionary:", empty_dict)

# ADDED: Empty Set vs Empty Dictionary
# {} always creates an empty dictionary, never an empty set, so their types are compared here
print("\nEmpty Set vs Empty Dictionary:")
empty_set_check = set()
empty_dict_check = {}
print("Type of empty_set_check:", type(empty_set_check))
print("Type of empty_dict_check:", type(empty_dict_check))

# Dictionary with Mixed Data Types
# Values can be of any data type; keys must be immutable (numbers, strings, tuples)
mixed_dict = {"number": 10, "pi": 3.14, "language": "Python", "is_active": True}
print("Mixed Dictionary:", mixed_dict)

# ADDED: Dictionary Keys Must Be Immutable
# Keys can be numbers, strings, or tuples (all immutable types); a list cannot be used as a key
print("\nDictionary Keys Must Be Immutable:")
immutable_keys_dict = {
    1: "Integer",
    "Python": "String",
    (10, 20): "Tuple"
}
print("Dictionary with Immutable Keys:", immutable_keys_dict)

# Nested Dictionary (Dictionary inside another dictionary)
# Useful for representing structured data, like a record with sub-details
nested_dict = {
    "name": "Python",
    "details": {"year": 1991, "creator": "Guido van Rossum"},
    "type": "Programming Language"
}
print("Nested Dictionary:", nested_dict)

# Accessing values inside a Nested Dictionary
print("\nAccessing Nested Dictionary Values:")
print("Value at key 'details':", nested_dict["details"])
print("Value of 'year' inside 'details':", nested_dict["details"]["year"])

# Accessing Values
print("\nAccessing Dictionary Values:")
# Using square brackets raises a KeyError if the key does not exist
print("Accessing 'name' with []:", student_dict["name"])

# Using get() is safer since it returns None (or a default value) instead of raising an error
print("Accessing 'age' with get():", student_dict.get("age"))
print("Accessing missing key with get() and default:", student_dict.get("grade", "Not Found"))

# Adding Items
print("\nAdding Dictionary Items:")
# A new key-value pair is added simply by assigning a value to a new key
student_dict["grade"] = "A"
print("After Adding 'grade':", student_dict)

# Updating Items
print("\nUpdating Dictionary Items:")
# Assigning a value to an existing key overwrites its previous value
student_dict["age"] = 21
print("After Updating 'age':", student_dict)

# update() can add or update multiple key-value pairs at once
student_dict.update({"city": "Chennai", "country": "India"})
print("After update():", student_dict)

# ADDED: update() using another dictionary
# update() can merge in all key-value pairs from a separate dictionary as well
print("\nupdate() Using Another Dictionary:")
update_demo_student = {"name": "Kishore"}
update_demo_student.update({"age": 20, "city": "Bengaluru"})
print("After update():", update_demo_student)

# Removing Items
print("\nRemoving Dictionary Items:")
# pop() removes the specified key and returns its value
removed_value = student_dict.pop("grade")
print("Popped Value:", removed_value)
print("After pop():", student_dict)

# popitem() removes and returns the last inserted key-value pair as a tuple
last_item = student_dict.popitem()
print("Popped Item (last inserted):", last_item)
print("After popitem():", student_dict)

# del removes a specific key-value pair permanently
del student_dict["city"]
print("After del:", student_dict)

# clear() removes all key-value pairs from the dictionary
copy_dict = student_dict.copy()
copy_dict.clear()
print("After clear():", copy_dict)

# Dictionary Methods
print("\nDictionary Methods:")
sample_dict = {"a": 1, "b": 2, "c": 3}

# keys() returns a view of all the keys in the dictionary
print("keys():", sample_dict.keys())

# values() returns a view of all the values in the dictionary
print("values():", sample_dict.values())

# items() returns a view of all key-value pairs as tuples
print("items():", sample_dict.items())

# get() safely retrieves a value for a given key (shown earlier as well)
print("get('b'):", sample_dict.get("b"))

# setdefault() returns the value of a key if it exists; otherwise it inserts the key with a
# default value and then returns that default value
print("setdefault('d', 4):", sample_dict.setdefault("d", 4))
print("Dictionary after setdefault():", sample_dict)

# Membership Operators
# The 'in' and 'not in' operators check for the presence of a KEY, not a value, by default
print("\nMembership Operators:")
print("'a' in sample_dict:", "a" in sample_dict)
print("'z' not in sample_dict:", "z" not in sample_dict)

# Built-in Functions
print("\nBuilt-in Functions for Dictionaries:")
marks_dict = {"Math": 85, "Science": 92, "English": 78}

print("Length (number of key-value pairs):", len(marks_dict))
print("Maximum value:", max(marks_dict.values()))
print("Minimum value:", min(marks_dict.values()))
print("Sum of values:", sum(marks_dict.values()))

# Dictionary Comparison
# Dictionaries are equal if they contain the same keys mapped to the same values
print("\nDictionary Comparison:")
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 2, "x": 1}
dict_c = {"x": 1, "y": 99}
print("dict_a == dict_b:", dict_a == dict_b)
print("dict_a == dict_c:", dict_a == dict_c)
print("dict_a != dict_c:", dict_a != dict_c)

# Copying Dictionaries
print("\nCopying Dictionaries:")
original_dict = {"language": "Python", "version": 3}

copy1_dict = original_dict
copy2_dict = original_dict.copy()

print("Original:", original_dict)
print("copy1 (same reference):", copy1_dict)
print("copy2 (independent copy):", copy2_dict)

# Conversion
# Dictionaries can be converted to/from lists of tuples, and their keys/values can be listed
print("\nDictionary Conversion:")
list_of_pairs = [("a", 1), ("b", 2), ("c", 3)]
converted_dict = dict(list_of_pairs)
print("List of Tuples:", list_of_pairs)
print("Converted to Dictionary:", converted_dict)

converted_keys_list = list(converted_dict.keys())
print("Converted Keys to List:", converted_keys_list)

converted_values_list = list(converted_dict.values())
print("Converted Values to List:", converted_values_list)

converted_items_list = list(converted_dict.items())
print("Converted Items to List of Tuples:", converted_items_list)