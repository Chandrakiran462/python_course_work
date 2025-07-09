'''Type Conversion (Type Casting)
Type conversion in Python refers to converting the value of one data type to another using
built-in functions such as int(), float(), str(), bool(), list(), tuple(), set(),
and dict().
Each section below explores conversions from a specific data type to others, with
examples and error cases.'''

# 1. Converting from int
a = 30
print(type(a))          # <class 'int'>
print(float(a))         # 30.0
print(complex(a))       # (30+0j)
print(str(a))           # '30'
print(bool(a))          # True
# list(a)
# Traceback (most recent call last):
#   File "<pyshell#36>", line 1, in <module>
#     list(a)
# TypeError: 'int' object is not iterable
# tuple(a)
# Traceback (most recent call last):
#   File "<pyshell#37>", line 1, in <module>
#     tuple(a)
# TypeError: 'int' object is not iterable
# set(a)
# Traceback (most recent call last):
#   File "<pyshell#38>", line 1, in <module>
#     set(a)
# TypeError: 'int' object is not iterable
# dict(a)
# Traceback (most recent call last):
#   File "<pyshell#39>", line 1, in <module>
#     dict(a)
# TypeError: 'int' object is not iterable


# 2. Converting from float
f = 18.5
print(type(f))        # <class 'float'>
print(int(f))         # 18
print(complex(f))     # (18.5+0j)
print(str(f))         # 18.5
print(bool(f))        # True

# print(list(f))      # gives Error  [float is not iterable]
# print(set(f))       # Gives Error  [float is not iterable]
# print(tuple(f))     # Gives Error  [float is not iterable]
# print(dict(f))      # Gives Error  [float is not iterable]

# 3. Converting from str
s = 'kiran'
print(type(s))        # <class 'str'>
print(int('20'))      # 20
print(float('3.5'))   # 3.5
print(bool(s))        # True
print(list(s))        # ['k', 'i', 'r', 'a', 'n']
print(tuple(s))       # ('k', 'i', 'r', 'a', 'n')
print(set(s))         # {'a', 'i', 'k', 'r', 'n'}
# print(dict(s))      # Gives Error [Needs key-value pair structure]

# 4. Converting from list
l = [1,2,3,4,5]
print(type(l))        # <class 'list'>
# print(int(l))       # Not Allowed
# print(float(l))     # Not Allowed
# print(complex(l))   # Not Allowed
print(bool(l))        # True
print(str(l))         # [1, 2, 3, 4, 5]
print(tuple(l))       # (1, 2, 3, 4, 5)
print(set(l))         # {1, 2, 3, 4, 5}
# print(dict(l))      # Not Allowed

# 5. Converting from tuple
t = (1,2,4,5)
print(type(t))        # <class 'tuple'>
# print(int(t))       # Not Allowed
# print(float(t))     # Not Allowed
# print(complex(t))   # Not Allowed
print(bool(t))        # True
print(str(t))         # (1, 2, 4, 5)
print(list(t))        # [1, 2, 4, 5]
print(set(t))         # {1, 2, 4, 5}
# print(dict(t))      # Not Allowed

# 6. Converting from set
se = {1,2,3,4}
print(type(se))        # <class 'set'>
# print(int(se))       # Not Allowed
# print(float(se))     # Not Allowed
# print(complex(se))   # Not Allowed
print(bool(se))        # True
print(str(se))         # {1, 2, 3, 4}
print(tuple(se))       # (1, 2, 3, 4)
print(list(se))        # [1, 2, 3, 4]
# print(dict(se))      # Not Allowed

# 7. Converting from dict
d = {1:2,3:4,5:6}
print(type(d))        # <class 'dict'>
# print(int(d))       # Not Allowed
# print(float(d))     # Not Allowed
# print(complex(d))   # Not Allowed
print(bool(d))        # True
print(str(d))         # {1: 2, 3: 4, 5: 6}
print(tuple(d))       # (1, 3, 5)
print(set(d))         # {1, 3, 5}
print(list(d))        # [1, 3, 5]
# print(dict(d))      # Not Allowed

# 8. Converting from bool
# if any data type is empty or false bool returns False otherwise it give True for all data types

# 9. Dictionary Conversion
# To convert a list to a dictionary, it must be a list of key-value tuples.

di = [('name', 'kiran'), ('batch', '14'), ('subject', 'python')]
print(dict(di))
# Output: {'name': 'kiran', 'batch': '14', 'subject': 'python'}