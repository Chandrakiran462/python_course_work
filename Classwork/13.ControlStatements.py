#For loop
#while loop
# when ever iterating statements
# list,tuple,set,string,dictionary

# n = int(input("Enter Table Number: "))
# for i in range(1,21):           # iterate the statement for 1 to 20 
#     print(f'{n} * {i} = {n*i}')

# s = 'sri sai chandra kiran'
# ch = input("enter charatcer: ")
# for i in range(len(s)):         # iterate the loop for length of s
#     if s[i] == ch:              # checks if the value at index is equal to the charater
#         print(s[i],i)           # prints the value and index of the character occur in the s.

# products = ['laptop','pods','mobile','shirt','case']
# item = input('enter items').split()

# for i in item:                          # i will get value from item
#     if i in product:                    # checks if i value in product
#         print(products.index(i),i)      # prints index of item i from products 
#     else:
#         print(f"{i} not found")         # if item not found 


email,pwd = 'xyz@gmail.com','xyz@1234'

max_attempts = 5

while max_attempts > 0:
    useremail = input("Enter Username: ")
    password = input("Enter Password: ")
    if useremail == email and password == pwd:
        print("Login Successful")
    else:
        print("Invalid Login")
    max_attempts -= 1
else:
    print('Try after sometime')