

myvar=10    #valid var
myVar=10    #valid var
myvar1=10   #valid var
my_var=10   #valid var
# my@var=10   ***[SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?]***
Myvar=10    #valid var
#1myvar=10   ***[SyntaxError: invalid decimal literal]***
_myvar=10   #valid var
#@myvar=10  ***[SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?]***
#my var=10   ***[SyntaxError: invalid syntax]***
a=10 
a,b,c=10,20,30
print(a,b,c)    #10,20,30
a=b=c=10
print(a,b,c) # 10,10,10
a=10
b=20
a,b=b,a
print(a,b) # 20 10