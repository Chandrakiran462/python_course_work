# python operators
'''Operators in Python are special symbols or keywords that perform operations on variables
and values'''
# 1. Arithmetic Operators
'''Arithmetic operators are used for basic mathematical calculations.'''
a = 20
b = 10
print("Addition(+):",a+b)           # Addition(+) : 30
print("Subtraction(-):",a-b)        # Subtraction(-): 10
print("Multiplication(*):",a*b)     # Multiplication(*): 200
print("Division(/):",a/b)           # Division(/): 2.0
print("floor Division(//):",a//b)   # floor Division(//): 2
print("Modulus(%):",a%b)            # Modulus(%): 0
print("Modulus(%):",b%a)            # Modulus(%): 10 [rerurns difference b/w a and b if b>a]
print("Exponentiation(**):",a**b)   # Exponentiation(**): 10240000000000

# 2. Comparison Operators
'''Comparison operators compare two values and return True or False.'''
print("Equal to(==):",a==b)                     # Equal to(==): False [Checks if both values are equal]
print("Not Equal to(!=):",a!=b)                 # Not Equal to(!=): True [Checks if values are not equal]
print("Greater than(>):",a>b)                   # Greater than(>): True [Checks if the first value is greater]
print("Greater than or Equal to(>=):",a>=b)     # Greater than or Equal to(>=): True [Checks if the first value is greater or equal]
print("Less than(<):",a<b)                      # Less than(<): False [Checks if the first value is smaller]
print("Less than or Equal to(<=):",a<=b)        # Less than or Equal to(<=): False [Checks if the first value is smaller or equal]

# 3. Assignment Operators
'''Assignment operators are used to assign or update the value of a variable.'''
c = 6
print("Assign(=):",c)                       # Assign(=): 6
a+=b
print("Add & Assign(+=):",a)                # Add & Assign(+=): 30
a-=b
print("Subtract & Assign(-=):",a)           # Subtract & Assign(-=): 20
a*=b
print("Multiply & Assign(*=):",a)           # Multiply & Assign(*=): 200
a/=b
print("Divide & Assign(/=):",a)             # Divide & Assign(/=): 20.0
a//=b
print("Floor Divide & Assign(//=):",a)      # Floor Divide & Assign(//=): 2.0
a%=c
print("Modulus & Assign(%=):",a)            # Modulus & Assign(%=): 2.0
b**=c
print("Exponentiate & Assign(**=):",b)      # Exponentiate & Assign(**=): 1000000

# 4. Logical Operators (Using Logic Gates)
'''Logical operators are used to combine multiple conditions. They work similarly to AND, OR,
and NOT gates in digital electronics.'''
print("AND(and):",a < 100 and c > 5)        # AND(and): True    [Returns True if both conditions are true]
print("OR(or):",a < 100 or c > 100)         # OR(or): True      [Returns True if at least one condition is true]
print("NOT(not):",not(a < b))               # NOT(not): False   [Reverses the condition (True becomes False)]

# 5. Membership Operators [in, not in]
'''Membership operators check if a value exists within a sequence (like a list, string, or tuple).'''
s = "Kiran"        # str
print('i' in s)         # True [Returns True if the value exists in the sequence]
l = ["kiran","data","analytics"]    # list
print('kiran' in l)     # True
t = (1,4,3,6,7)     # tuple
print(8 not in t)       # True
se = {2,5,3,7}      # set
print(10 not in se)     # True [Returns True if the value does NOT exist in the sequence]
d = {'name':'kiran' , 'course' : 'DA'}  #dict
print('batch' in d)     # False

# 6. Identity Operators [is, is not]
'''Identity operators check whether two variables refer to the same object in memory.'''
j = [1,2,3,4]
k = [1,2,3,4]
j = l
print(j is k)       # False [Different objects with the same content]
print(j is l)       # True  [Both refer to the same object]
print(j is not k)   # True
