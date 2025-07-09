# Input Formatting
# Python's input() function is used to take input from the user during program execution. By
# default, it returns a string. We often convert the input into int, float, list, tuple, set,
# or dict as needed.

# 1. String Input
# Use case: Entering a name, email, city, etc.
name = input("enter name: ")        # enter name: kiran
print(name)                         # kiran

# 2. Integer Input
# Use case: Age, quantity, mobile number, number of items in cart.
num = int(input("enter integer: ")) # enter integer: 21
print(num)                          # 21

# 3. Float Input
# Use case: Price, temperature, discount, rating.
f = float(input("Enter discount: "))# Enter discount: 89.6
print(f)                            # 89.6

# 4. Input as List (Space-separated)
# Use case: List of names, marks, or product IDs.
std_names = input("enter names space-seperated: ").split() 
                                    # enter names space-seperated: kiran shannu subbu
print(std_names)                    # ['kiran', 'shannu', 'subbu']                     

# 5. Input as List (Comma-separated)
# Use case: Tags, emails, product categories.
uid = input("enter uids comma-seperated : ").split(',')    
                                    # enter uids comma-seperated : 462 472 499
print(uid)                          # ['462', '472', '499']

# 6. List of Integers
# Use case: Marks, product prices, IDs.
prices = list(map(int,input("enter prices: ").split()))    
                                    # enter prices: 399 499 999
print(prices)                       # [399, 499, 999]

# 7. List of Floats
# Use case: Sensor readings, weights, product prices.
sen_readings = list(map(float,input("enter: ").split()))   
                                    # enter: 87.5 77.5 65.8
print(sen_readings)                 # [87.5, 77.5, 65.8]

# 8. Tuple Input
# Use case: Coordinates, dimensions (length, width, height).
t = tuple(map(int,input("enter: ").split()))               
                                    # enter: 4 6 8
print(t)                            # (4, 6, 8)

# 9. Set Input
# Use case: Selected image IDs where duplicates must be removed (e.g., in a photo-sharing
# app).
s = set(map(int,input("enter: ").split()))                 
                                    # enter: 101 102 103
print(s)                            # {101, 102, 103}

# 10. Dictionary Input using eval()
# Use case: When entering structured data like configuration settings or user profiles.

dic = eval(input("enter: "))        # enter: {'name':'kiran','age':'21'}
print(dic)                          # {'name': 'kiran', 'age': '21'}