print("Welcome to Grocery Store".center(50,"-"))
print("Here are available items: ")
grocery_items ={
    1:{'Product':'Rice','Price':60},
    2:{'Product':'Wheat floor','Price':35},
    3:{'Product':'Bread','Price':30},
    4:{'Product':'Eggs','Price':70},
    5:{'Product':'Butter','Price':20},
    6:{'Product':'Cooking oil','Price':120},
    7:{'Product':'Tea Powder','Price':90},
    8:{'Product':'Tooth Paste','Price':50},
    9:{'Product':'Soap','Price':40},
    10:{'Product':'Shampoo','Price':100}
}
print("Index",end = " ")
print("Product".rjust(10," "),end = " ")
print("Price".rjust(10," "))
for i in grocery_items:
    print(f"{i}. \t {grocery_items[i]['Product']}",end = " ")
    print(f"${grocery_items[i]['Price']}".rjust(10," "))

items = list(map(int,input("Enter item index(1 2 3 4..): ").split()))
total = 0
s =set()
for i in items:
    if i not in s:
        c = items.count(i)
        print(f"{grocery_items[i]['Product']} \t {c}*${grocery_items[i]['Price']} = ${c*grocery_items[i]['Price']}")
        total+= grocery_items[i]['Price']*c
        s.add(i)
print(f"total bill: ${total}")
        

