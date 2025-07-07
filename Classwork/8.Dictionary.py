'''
Dictionary

A dictionary in Python is an ordered, mutable collection that stores key-value pairs.
Unlike lists or tuples, which are indexed by position, dictionaries are indexed by unique keys.

1. Introduction to Dictionary

A dictionary is defined using curly braces {}, where each key is followed by a colon :, and
the key-value pairs are separated by commas.

'''

data = {'name':'kiran','course':'DA','Batch':'14','passed':2025}
print(data) # {'name': 'kiran', 'course': 'DA', 'Batch': '14', 'passed': 2025}

'''Key Features of Dictionaries:
1. Keys must be unique -If you use duplicate keys, the last value will overwrite the
previous one.
2. Keys must be immutable - Strings, numbers, and tuples can be used as keys, but
lists and dictionaries cannot.
3. Values can be of any data type - Integers, floats, lists, tuples, another dictionary,
etc.
4. Dictionaries are mutable - You can modify, add, or remove items after the
dictionary is created.
'''
'''2. Dictionary Operations
These are the basic operations you can perform on dictionaries:
'''

# 2.1 Accessing Values
# Dictionaries allow access to values using keys

# data = {'name':'kiran','course':'DA','Batch':'14','passed':2025}
print(data['name'])                     # kiran
print(data.get('course'))               # DA

'''Difference Between dict[key] and dict.get(key)
● dict[key] will raise a KeyError if the key does not exist.
● dict.get(key, default_value) will return None or the specified
default_value if the key is not found.
'''
# print(data['age]) # gives error
print(data.get('age','age doesnt exist in data'))# age doesnt exist in data

# 2.2 Adding and Updating Items
# You can add a new key-value pair or update an existing value by assigning a new value to a key

data['passed'] = '060604'       # Updating existing key 
data['city'] = 'rajanagram'     # Adding a new key-value pair
print(data)             # {'name': 'kiran', 'course': 'DA', 'Batch': '14', 'passed': '060604', 'city': 'rajanagram'}

'''2.3 Removing Items from a Dictionary
There are several ways to remove elements from a dictionary.
Using pop(key)
Removes the specified key and returns its value.
'''
data.pop('city')        # Removes the specified key and returns its value.
print(data)             # {'name': 'kiran', 'course': 'DA', 'Batch': '14', 'passed': '060604'}
data.popitem()          # Removes and returns the last inserted key-value pair.
print(data)             # {'name': 'kiran', 'course': 'DA', 'Batch': '14'}
del data['Batch']       # Deletes a specific key-value pair or the entire dictionary
print(data)             # {'name': 'kiran', 'course': 'DA'}
data.clear()            # Removes all key-value pairs, making the dictionary empty
print(data)             # {}

# 3. Dictionary Built-in Methods

# 3.1 Dictionary Methods for Accessing Data
d = {'name':'kiran','age':'21','branch':'ECE','passed':'2025'}
print(d.get('dob','Not Found')) # Not Found  **[Returns the value for the given key; returns default if key is not found]
print(d.keys())                 # dict_keys(['name', 'age', 'branch', 'passed']) **[Returns a view object containing all keys]
print(d.values())               # dict_values(['kiran', '21', 'ECE', '2025']) ** [Returns a view object containing all values]
print(d.items())                # dict_items([('name', 'kiran'), ('age', '21'), ('branch', 'ECE'), ('passed', '2025')]) 
'''                               Returns a view object containing all key-value pairs as tuples'''

# 3.2 Dictionary Methods for Adding and Updating Data
d.update({'course':'DA','batch':'14'}) # Merges another dictionary into the current dictionary
print(d)                        # {'name': 'kiran', 'age': '21', 'branch': 'ECE', 'passed': '2025', 'course': 'DA', 'batch': '14'}
d.setdefault('dob','unknown')   # Returns value of key; if key does not exist, inserts it with default value
print(d)                        # {'name': 'kiran', 'age': '21', 'branch': 'ECE', 'passed': '2025', 'course': 'DA', 'batch': '14', 'dob': 'unknown'}

# 3.3 Dictionary Methods for Removing Data
'''
data.pop('city')        # Removes and returns value of the specified key
print(data)             # {'name': 'kiran', 'course': 'DA', 'Batch': '14', 'passed': 2025, 'DOB': '060604'}
data.popitem()          # Removes and returns the last inserted key-value pair
print(data)             # {'name': 'kiran', 'course': 'DA', 'Batch': '14', 'passed': 2025}
del data['passed']      # Deletes a specific key from the dictionary 
print(data)             # {'name': 'kiran', 'course': 'DA', 'Batch': '14', 'passed': 2025}
data.clear()            # Removes all key-value pairs, making the dictionary empty
print(data)             # {}
'''
# 4. Built-in Functions for Dictionaries
print(len(d))           # 7         #Returns the number of items in the dictionary
print(max(d))           # passed    #Returns the maximum key (if keys arecomparable)
print(min(d))           # age       #Returns the minimum key 
print(sorted(d))        # ['age', 'batch', 'branch', 'course', 'dob', 'name', 'passed'] # Returns sorted list of keys 

# 5. Nested Dictionaries
# A dictionary can contain another dictionary as its value.
students = {
"Kiran": {"age": 21, "course": "CS"},
"shannu": {"age": 22, "course": "Math"}
}
print(students["Kiran"]["course"]) # CS
