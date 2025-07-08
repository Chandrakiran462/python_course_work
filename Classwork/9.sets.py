'''
Sets


1. Introduction to Sets
● A set is an unordered, mutable collection of unique elements.
● Sets automatically remove duplicate elements.
● Sets are similar to mathematical sets and support operations like union, intersection,
and difference.
● They are useful for storing unique elements and performing fast membership tests.

'''
# Set Creation Syntax:
s = {1,2,3,4,5,6,7,9,10}    # Creating a set with unique elements
print(s)                    # {1, 2, 3, 4, 5, 6, 7, 9, 10}
es = set()                  # # Creating an empty set (use set() function, not {})
print(es)                   # set()
sd = {11,12,13,14,2,3,16,17,4,3,3,6} # Set with duplicate elements (duplicates are removed automatically)
print(sd)                   # {2, 3, 4, 6, 11, 12, 13, 14, 16, 17}

'''
2. Set Properties
● Unordered: Sets do not maintain the insertion order.
● Unique Elements: Duplicate elements are not allowed.
● Mutable: Sets can be modified (elements can be added or removed).
● Immutable Elements Only: Elements must be hashable (mutable types like lists
cannot be elements).
'''
# es = {[1,2,3],3,4}  # invalid formate {set only allow immutable data types}
es = {'kiran','shannu','subbu'}
print(es)                   # {'shannu', 'subbu', 'kiran'}

'''
3. Operations on Sets
Python provides several set operations that mimic mathematical set theory.

a. Membership Testing
● Check if an element is present using the 'in' or 'not in' keywords'''
# s = {1,2,3,4,5,6,7,9,10}
print(4 in s)               # True
print(12 in s)              # False
print(11 not in s)          # True
print(5 not in s)           # False

# b. Union (| or union() method)
# s = {1,2,3,4,5,6,7,9,10}
# sd = {11,12,13,14,2,3,16,17,4,3,3,6}
print(s | sd)               # {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17}
'''                         Combines elements from two sets (removes duplicates).'''
# c. Intersection (& or intersection() method)
print(s & sd)               # {2, 3, 4, 6}
'''                         Returns common elements between two sets.'''
# d. Difference (- or difference() method)
print(s - sd)               # {1, 5, 7, 9, 10}
'''                         Returns elements in the first set but not in the second set.'''
# e. Symmetric Difference (^ or symmetric_difference() method)
print(s ^ sd)               # {1, 5, 7, 9, 10, 11, 12, 13, 14, 16, 17}
'''                          Returns elements in either set1 or set2 but not both.'''
# f. Subset (<= or issubset() method)
print({1,2,4} <= s)         # True
'''                         Checks if all elements of one set are present in another'''
# g. Superset (>= or issuperset() method)
print(sd >= {12,13})        # True
'''                         Checks if one set contains all elements of another'''
# h. Disjoint Sets (isdisjoint() method)
print(s.isdisjoint(sd))     # false
'''                         Returns True if two sets have no common elements.'''

# 4. Built-in Methods for Sets
# s = {1,2,3,4,5,6,7,9,10}
se = {11,12,13,14,2,3,16,17,4,3,3,6}
s.add(50)                   # Adds an element to the set
print(s)                    # {1, 2, 3, 4, 5, 6, 7, 9, 10, 50}

s.remove(10)                # Removes an element; raises anerror if the element doesn’t exist
print(s)                    # {1, 2, 3, 4, 5, 6, 7, 9, 50}

s.discard(9)                # Removes an element; does not raise an error if the element doesn’t exist
print(s)                    # {1, 2, 3, 4, 5, 6, 7, 50}

print(s.pop())              # 1   **[Removes and returns an arbitrary element]
print(s)                    # {2, 3, 4, 5, 6, 7, 50}

sd.clear()                  # Removes all elements from the set 
print(sd)                   # set()

sd.update({62,63,54})       # Adds elements from another set to the current set
print(sd)                   # {62, 54, 63}

a={1,2,3}
b={3,4,5}
a.intersection_update(b)    # Updates the set with the intersection of itself and another set
print(a)                    # {3}

b.difference_update(a)      # Updates the set by removingelements found in another set
print(b)                    # {4, 5}

b.symmetric_difference_update(se)# Updates the set with the symmetric difference
print(b)                    # {2, 3, 5, 6, 11, 12, 13, 14, 16, 17}

c =  a.copy()               # Returns a shallow copy of the set 
print(a)                    # {3}

# 5. Built-in Functions for Sets
print(len(b))               # 10    **[Returns the number of elements in the set]
print(max(b))               # 17    **[Returns the maximum element in the set]
print(min(b))               # 2     **[Returns the minimum element in the set]
print(sum(b))               # 99    **[Returns the sum of all elements in the set]
print(sorted(b))            # [2, 3, 5, 6, 11, 12, 13, 14, 16, 17] 
                            #  Returns a sorted list of the set elements
l = [1,2,3,4]               # Converts an iterable (e.g., list, string) to a set
print(set(l))               # {1, 2, 3, 4}



'''
6. Immutability and Frozensets
● Frozensets are immutable versions of sets.
● Once a frozenset is created, its elements cannot be changed.
● Useful for creating hashable, immutable collections.
Example:
# Creating a frozenset
frozen = frozenset([1, 2, 3])
print(frozen)
# Frozenset is immutable
# The following will raise an error
# frozen.add(4)
'''