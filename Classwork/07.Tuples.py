'''Tuples

1. Introduction to Tuples

● A tuple is an immutable, ordered collection of elements.
● Tuples are similar to lists, but once a tuple is created, its contents cannot be
changed.
● Tuples can store any type of data (int, float, string, list, etc.).
● Tuples are faster than lists because they are immutable.
'''

# Tuple Creation Syntax:

et = ()                             #  Empty Tuple
st = (5,)                           #  Single-element Tuple (note the trailing comma)
t = (1,2,3.8,4+5j,'kiran',[1,2,3,4],{1,2,3,4},{'name':'kiran','batch': 'DA'},(1,2,3)) # Multi-element Tuple
wt = 1,2,2,3,2,4,5,4                #   Without parentheses (implicit tuple creation)

# 2. Accessing Tuple Elements

print(t[4])                 # kiran     **[Indexing]
print(t[-3])                # {1, 2, 3, 4} **[-ve indexing]
print(t[4:8])               # ('kiran', [1, 2, 3, 4], {1, 2, 3, 4}, {'name': 'kiran', 'batch': 'DA'})   **[slicing]
print(t[-5:])               # ('kiran', [1, 2, 3, 4], {1, 2, 3, 4}, {'name': 'kiran', 'batch': 'DA'}, (1, 2, 3)) **[-ve slicing]
print(t[::-1])              # ((1, 2, 3), {'name': 'kiran', 'batch': 'DA'}, {1, 2, 3, 4}, [1, 2, 3, 4], 'kiran', (4+5j), 3.8, 2, 1) **[reverse ]

# 3. Operations on Tuples

print("Concatenation(+): ",st + wt)         # Concatenation(+):  (5, 1, 2, 2, 3, 2, 4, 5, 4)
print("Repetition(*): ",wt * 2)             # Repetition(*):  (1, 2, 2, 3, 2, 4, 5, 4, 1, 2, 2, 3, 2, 4, 5, 4)
print("Membership Testing (in): ",4+5j in t)# Membership Testing (in):  True
print("Membership Testing (not in): ",'chandra' not in t )# Membership Testing (not in):  True
a,b,c,d,e,f,g,h = wt  #  Tuple packing
print("Tuple Unpacking",a,b,c,d,e)          # Tuple Unpacking 1 2 2 3 2

# 4. Tuple Methods

print(wt.count(2))              # 3  **[Counts the number of occurrences of 2 in the tuple]
print(wt.index(5))              # 6  **[Returns the first index of 5 in the tuple]

# 5. Built-in Functions for Tuples

print(len(wt))                  # 8 **[Returns the length (number of elements) of the tuple]
print(max(wt))                  # 5 **[Returns the maximum element in the tuple (for comparable types)]
print(min(wt))                  # 1 **[Returns the minimum element in the tuple]
print(sorted(wt))               # [1, 2, 2, 2, 3, 4, 4, 5] **[sorts the tuple]
print(sum(wt))                  # 23 **[Returns the sum of elements (if all are numbers)]

# 6. Immutability and Tuple Behavior
'''Since tuples are immutable:
● You cannot modify elements (tuple[0] = 10 will raise an error).
● However, if a tuple contains mutable objects (e.g., lists), the mutable objects can still
be changed.'''

l = (1,2,4,3,[3,4,5,7])
# l.append(4))   # gives error
# l[4].append(5) # gives error
l[4].append(8)
print(l)         # (1, 2, 4, 3, [3, 4, 5, 7, 8]) 8 is appeded in list.

# Hashable: Tuples can be used as keys in dictionaries (unlike lists).

k = [1,2,3,4]
print(tuple(k))
s = {1,2,3,4}
print(tuple(s))

'''7. Advantages of Tuples
    1. Immutability: Ensures data cannot be accidentally modified.
    2. Faster: Tuples are more memory-efficient and faster than lists.
    3. Hashable: Tuples can be used as keys in dictionaries (unlike lists).
    4. Data Integrity: Ideal for storing constant data.

8. Use Cases of Tuples
    ● Returning multiple values from functions.
    ● Representing fixed collections of items (coordinates, dates, etc.).
    ● Using tuples as dictionary keys or set elements.'''


