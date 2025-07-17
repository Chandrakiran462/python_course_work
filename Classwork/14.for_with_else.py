# break Statement in Python
# Definition:
# The break statement is used to exit a loop before it has iterated over all the items or before
# the loop condition becomes false. It is commonly used inside for or while loops when a
# specific condition is met and further looping is unnecessary or unwanted.

# continue Statement in Python
# Definition:
# The continue statement is used to skip the rest of the code inside the current iteration of a
# loop and move to the next iteration. It does not terminate the loop entirely like break, but
# rather skips the current cycle



l = ['phone','laptop','pods','earphones']
for i in l:
    if i == 'bag':
        break
    print(i)
else:
    print("End of the list")

'''
phone
laptop
pods
earphones
End of the list
if break does not execute else statement will execute
'''
for i in l:
    if i == 'pods':
        break
    print(i)
else:
    print("End of the list")
'''
phone
laptop
if break statement execute it ends the program and else statement won't execute
'''

for i in l:
    if i == 'pods':
        continue
    print(i)
else:
    print("End of the list")

'''laptop
phone
laptop
earphones
End of the list
'continue' will skip the condition or step and execute all the program
'''
# these break,continue,else works same for while loop


'''
assert Keyword in Python
Definition:
The assert keyword is used to perform debugging checks during development. It tests
whether a given condition is True. If the condition is False, the program raises an
AssertionError. It is mainly used to catch bugs by ensuring certain conditions hold true.
'''

# Syntax
# assert condition, "Error message"

a = 10
b = 2 
assert b > 0, 'b must be graeater than zero'
print(a/b)   # 5.0 if b > 0 it gives out put else it give assert error message
             # this assert mostly used in development to debug 

'''
assert b > 0, 'b must be graeater than zero'
           ^^^^^
AssertionError: b must be graeater than zero
'''