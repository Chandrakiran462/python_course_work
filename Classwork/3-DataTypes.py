a = 10
print(type(a))  #<class 'int'>

a = 10.0
print(type(a))  #<class 'float'>

a = 3 + 4j
print(type(a))  #<class 'complex'>

name = 'kiran'
print(type(name))   #<class 'str'>
name = "kiran"
print(type(name))   #<class 'str'>
name = '''kiran'''
print(type(name))   #<class 'str'>

fav = list()                        # mutable
fav = [1,2.5,3+4j,'kiran',[]]       # hetrogeneous
print(type(fav))    #<class 'list'>

t = (1,4,5,6)
t1 = tuple()   #orderd  #immutable #faster then list
print(type(t))      #<class 'tuple'>

s = {1,2,3,4,1,1,4,3,5}    #unordered   #mutable    #dosen't allow duplicates
s1 = set()          #constructor
print(type(s))      #<class 'set'>

fs = frozenset({2,5,6,6})   #immutable
print(type(fs))     #<class 'frozenset'>

d = {'name':'kiran' , 'course' : 'DA'} # key : value #ordered #key=immutable #value:mutable
print(type(d))      #<class 'dict'>

lockstatus = True
print(type(lockstatus))     #<class 'bool'>
bestseller = False
print(type(bestseller))     #<class 'bool'>

randomvar = None
print(type(randomvar))      #<class 'NoneType'>
