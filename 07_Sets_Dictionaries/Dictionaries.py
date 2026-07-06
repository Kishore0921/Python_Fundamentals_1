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