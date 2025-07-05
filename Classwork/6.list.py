'''1. Basic Features of Lists
● Ordered: Lists maintain the order of elements.
● Mutable: Elements can be modified after creation.
● Indexed: Elements can be accessed using an index (starting from 0).
● Allow Duplicates: Lists can contain duplicate values.
● Heterogeneous: Lists can contain different data types (e.g., int, str, float, etc.).
● Dynamic: Size is not fixed; elements can be added or removed dynamically'''

# 2. Creating Lists

l = []
a = list()

# 2.2 List with Elements

num = [1,2,3,4,5,2,4,5,2,4,44,66]
s = ['sri','sai','chandra','kiran']
mix = [1,2,3,4,2.4,5.8,'kiran',True,(1,2,4),{1,3,44},[6,3,4],4+5j]

# 3. Accessing Elements in a List

# 3.1 Using Indexing (Positive & Negative)

print(mix[4])
print(mix[7])
print(mix[-2])
print(mix[-5,-11,-1])

# 3.2 Using Slicing

print(mix[4:9])
print(mix[:4])
print(mix[9:])
print(mix[-5:-1])
print(mix[::-1])

# 4. Modifying Lists

# 4.1 Changing Elements
mix[6] = 100
print("changes element at index 5",mix)

# 4.2 Adding Elements

print(mix.append("chandu"))
print(mix.extend("sri","sai"))
