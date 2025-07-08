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
s = {1,2,3,4,5,6,7,9,10}
print(s)
es = set()
print(es)
sd = {11,12,13,14,2,3,16,17,4,3,3,6}
print(sd)

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
print(es)

'''
3. Operations on Sets
Python provides several set operations that mimic mathematical set theory.

a. Membership Testing
● Check if an element is present using the in or not in keywords'''
# s = {1,2,3,4,5,6,7,9,10}
print(4 in s)
print(12 in s)
print(11 not in s)
print(5 not in s)

# b. Union (| or union() method)
# s = {1,2,3,4,5,6,7,9,10}
# sd = {11,12,13,14,2,3,16,17,4,3,3,6}
print(s | sd)
# c. Intersection (& or intersection() method)
print(s & sd)
# d. Difference (- or difference() method)
print(s - sd)
# e. Symmetric Difference (^ or symmetric_difference() method)
print(s ^ sd)
# f. Subset (<= or issubset() method)
print({1,2,4} <= s)
# g. Superset (>= or issuperset() method)
print(sd >= {12,13})
# h. Disjoint Sets (isdisjoint() method)
print(s.isdisjoint(sd))

# 4. Built-in Methods for Sets
# s = {1,2,3,4,5,6,7,9,10}
se = {11,12,13,14,2,3,16,17,4,3,3,6}
s.add(50)
print(s)
s.remove(10)
print(s)
s.discard(9)
print(s)
print(s.pop())
print(s)
sd.clear()
print(sd)
s.update({62,63,54})
print(s)
