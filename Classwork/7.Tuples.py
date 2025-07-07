'''Tuples

1. Introduction to Tuples

● A tuple is an immutable, ordered collection of elements.
● Tuples are similar to lists, but once a tuple is created, its contents cannot be
changed.
● Tuples can store any type of data (int, float, string, list, etc.).
● Tuples are faster than lists because they are immutable.
'''

# Tuple Creation Syntax:

et = ()
st = (5,)
t = (1,2,3.8,4+5j,'kiran',[1,2,3,4],{1,2,3,4},{'name':'kiran','batch': 'DA'},(1,2,3))
wt = 1,2,3,4,[1,2,3]

# 2. Accessing Tuple Elements
# a. Indexing 

print(t[4])
print(t[-3])
print(t[4:8])
print(t[-5:])
print(t[::-1])
