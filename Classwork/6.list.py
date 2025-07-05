'''1. Basic Features of Lists
● Ordered: Lists maintain the order of elements.
● Mutable: Elements can be modified after creation.
● Indexed: Elements can be accessed using an index (starting from 0).
● Allow Duplicates: Lists can contain duplicate values.
● Heterogeneous: Lists can contain different data types (e.g., int, str, float, etc.).
● Dynamic: Size is not fixed; elements can be added or removed dynamically'''

# 2. Creating Lists

l = []                  # Creating Empty list
a = list()              # creating Empty list Using list() constructor

# 2.2 List with Elements

num = [1,2,3,4,5,2,4,5,2,4,44,66]       # List of integers
s = ['sri','sai','chandra','kiran']     # List of strings
mix = [1,2,3,4,2,3,4,3,2.4,5.8,'kiran',True,(1,2,4),{1,3,44},[6,3,4],4+5j]
'''list with Mixed data types'''

# 3. Accessing Elements in a List

# 3.1 Using Indexing (Positive & Negative)

print(mix[4])                       # 2 **[Returns Value at index (4) in the list]**
print(mix[7])                       # 3 **[Returns Value at index (7) in the list]**
print(mix[-2])                      # [6, 3, 4] **[Returns Value at index (-2) in the list]**{-ve Indexing} 
print(mix[-5:-11:-1])               # [True, 'kiran', 5.8, 2.4, 3, 4] **[Returns Values b/w index (-5:-11:-1) in the list]**{-ve Indexing}

# 3.2 Using Slicing

print(mix[4:9])                     # [2, 3, 4, 3, 2.4] {slicing} **[Returns values from index (4 to 9)]**
print(mix[:4])                      # [1, 2, 3, 4] **[Returns values "from start"]**
print(mix[9:])                      # [5.8, 'kiran', True, (1, 2, 4), {1, 3, 44}, [6, 3, 4], (4+5j)] **[Returns Values "to end"]
print(mix[-5:-1])                   # [True, (1, 2, 4), {1, 3, 44}, [6, 3, 4]] {-ve slicing} **[Returns values from index (4 to 9)]**
print(mix[::-1]) #reverse of string # [(4+5j), [6, 3, 4], {1, 3, 44}, (1, 2, 4), True, 'kiran', 5.8, 2.4, 3, 4, 3, 2, 4, 3, 2, 1]

# 4. Modifying Lists

# 4.1 Changing Elements
num[6] = 100             # original num = [1,2,3,4,5,2,4,5,2,4,44,66]                
print("changes element at index 5",num)# changes element at index 5 [1, 2, 3, 4, 5, 2, 100, 5, 2, 4, 44, 66]

# 4.2 Adding Elements
mix.append("chandu")                # Adds "chandu" element to the end of the list
print(mix)                          # [1, 2, 3, 4, 2, 3, 4, 3, 2.4, 5.8, 'kiran', True, (1, 2, 4), {1, 3, 44}, [6, 3, 4], (4+5j), 'chandu']
mix.extend(["sri","sai"])           # Adds multiple elements (e.g., sri,sai) to the end.
print(mix)                          # [1, 2, 3, 4, 2, 3, 4, 3, 2.4, 5.8, 'kiran', True, (1, 2, 4), {1, 3, 44}, [6, 3, 4], (4+5j), 'chandu', 'sri', 'sai']
mix.insert(5,"hello")               # Inserts "hello" at the specified index(5)
print(mix)                          # [1, 2, 3, 4, 2, 'hello', 3, 4, 3, 2.4, 5.8, 'kiran', True, (1, 2, 4), {1, 3, 44}, [6, 3, 4], (4+5j), 'chandu', 'sri', 'sai']

# 4.3 Removing Elements
num.remove(3)                       # Removes the first occurrence of 3
print(num)                          # [1, 2, 4, 5, 2, 100, 5, 2, 4, 44, 66]
num.pop()                           # Removes last element
print(num)                          # [1, 2, 4, 5, 2, 100, 5, 2, 4, 44]
num.pop(8)                          # Removes element at index 8
print(num)                          # [1, 2, 4, 5, 2, 100, 5, 2, 44]
del num[6]                          # Deletes element at index 6
print(num)                          # [1, 2, 4, 5, 2, 100, 2, 44]
s.clear()                           # Clears the entire list 
print(s)                            # [] **[previously s = ['sri','sai','chandra','kiran']]**

#more functions

print(mix.index('kiran'))           # 11 [Returns the index of the first occurrence of 'kiran'.]
print(num.count(2))                 # 3  [Returns the number of times 2 appears in the list.]
print(sorted(num))                  # [1, 2, 2, 2, 4, 5, 44, 100] 
print(num)                          # [1, 2, 4, 5, 2, 100, 2, 44]
num.sort()                          # [Sorts the list (ascending by default)]
print(num)                          # [1, 2, 2, 2, 4, 5, 44, 100]
'''sorted = it sorts the list  and returns a new sorted list, leaving the original list unchanged.
   sort = it sorts the list and modify the originl list directly '''
num.reverse()                       # Reverses the list in place.
print(num)                          # [100, 44, 5, 4, 2, 2, 2, 1]
print(num.copy())                   # [100, 44, 5, 4, 2, 2, 2, 1] **[Returns a shallow copy of the list.]**