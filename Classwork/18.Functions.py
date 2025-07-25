'''
Functions
Definition of Functions
A function in Python is a reusable block of code that performs a specific task. It helps in
breaking down large programs into smaller, manageable parts. Functions improve code
reusability, readability, and modularity


function is a block of code. which we can use when we want.
function reduces code complexity,reuse,divide code
'''
'''Features of Functions in Python'''
# 1. Code Reusability - Write once, use multiple times.
# 2. Modularity - Divide code into logical sections.
# 3. Maintainability - Easier to debug and modify.
# 4. Scalability - Helps in handling complex applications.
# 5. Encapsulation - Hides implementation details from users.
# 6. Parameterization - Functions accept arguments to perform operations dynamically.
# 7. Return Values - Functions can return values for further use.
'''Why Do We Need Functions?'''
# 1. Avoid Code Duplication - Instead of writing the same code multiple times, use
# functions.
# 2. Improves Readability - Makes the code more structured and easy to understand.
# 3. Easier Debugging - Errors can be identified in one place.
# 4. Supports DRY Principle - "Don't Repeat Yourself" principle for efficient coding.
# 5. Encourages Modular Programming - Breaking tasks into smaller functions
# improves collaboration and organization.
'''Applications of Functions'''
# Functions are widely used in various domains:
# ● Web Development: Handling user input, data processing, and API requests.
# ● Machine Learning: Implementing mathematical computations and data
# preprocessing.
# ● Game Development: Managing game logic, AI, and graphics rendering.
# ● Finance & Banking: Handling transactions, calculations, and reports.
# ● System Programming: Managing hardware resources and process control.
# Functions are an essential part of Python programming, making the code efficient, reusable,
# and easy to maintain.
'''
data = {'current_balance': 54785,'history':[]}
def check_balance():
    print(data['current_balance'])
def deposit():
    amount = int(input("Enter amount: "))
    data['current_balance'] += amount
    data['history'].append(f"Deposited ${amount}")
    print(f"Deposite successful: {amount}")
def withdraw():
    amount = int(input("Enter amount: "))
    if data['current_balance'] >= amount:
        data['current_balance'] -= amount
        data['history'].append(f"Withdraw ${amount}")
        print(f"Withdraw successful: {amount}")
    else:
        print("Insuffecient Balance")
def history():
    print(data['history'])

while True:
    print("Welcome To ATM".center(30,"="))
    print("1. Check Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. History")
    print("0. Exit")

    ch = int(input("Select your option: "))
    if ch == 0:
        print("Thank You".center(30,"="))
        break
    elif ch == 1:
        check_balance()
    elif ch == 2:
        deposit()
    elif ch == 3:
        withdraw()
    elif ch == 4:
        print("Transactions")
        for i in data['history']:
            print(i)
    else:
        print("Invalid Option. Try again")
'''

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

exp = input("Enter Expression: ")
op = None
for i in exp:
    if not i.isdigit():
        op = i
a,b=exp.split(op)
a,b = int(a),int(b)
if op == '+':
    print(add(a,b))
elif op == '-':
    print(sub(a,b))
elif op == '*':
    print(mul(a,b))
elif op =='/':
    print(div(a,b))
elif op == '%':
    print(mod(a,b)) 