'''Example Using only IF'''
s =input("Enter the status(R O G):")

if s == 'R':
    print("Stop")
if s == 'O':
    print("Ready")
if s == 'G':
    print("Gooooooooo")

'''if-else Example'''
items = ['phone','airpods','earphones','laptop','watch']
print("Welcome to Amazon Store".center(50,'*'))
search = input('enter the item: ').lower()
if search in items:
    print(f"{search} found. Buy Now.")
else:
    print(f"{search} is out of stock. we will notify you.")


'''if-elif-else example'''
# weekend Budget plan
print("Weekend budget plan".center(50,'*'))
amount = int(input("Enter the amount you can spend: "))
if amount > 20000:
    print("Go to Goa")
elif amount > 15000:
    print("Go for Shopping")
elif amount > 10000:
    print("Clubbinggg")
elif amount > 5000:
    print("Go for Dinner") 
elif amount > 2000:
    print("Go for Box Cricket")
elif amount > 500:
    print("Go for Movie")
elif amount > 100:
    print("Go for street food")
else:
    print("save the money and sleep")


'''Neseted if Example'''
# Grade system
print("Grading System".center(50,'*'))
data = {
    1:{'name':'sri','attempt_status':False,'Python':0,'sql':0,'powerBI':0},
    2:{'name':'chandu','attempt_status':True,'Python':100,'sql':90,'powerBI':80},
    3:{'name':'sai','attempt_status':True,'Python':70,'sql':90,'powerBI':50},
    4:{'name':'kiran','attempt_status':False,'Python':30,'sql':100,'powerBI':25},
    5:{'name':'chandra','attempt_status':True,'Python':60,'sql':40,'powerBI':35}
}

stuid = int(input("Enter the Student ID:"))
print(data[stuid])
if data[stuid]['attempt_status']:
    total = (data[stuid]['Python'] + data[stuid]['sql'] + data[stuid]['powerBI']) / 3
    if total >= 90:
        print(f"Congrats !!!!!\n{data[stuid]['name']} got 'A' grade")
        print("Feedback: Good and keep it up!")
    elif total >= 75:
        print(f"Congrats !!!!!\n{data[stuid]['name']} got 'B' grade")
        print("Feedback: Good and work more!")
    elif total >= 50:
        print(f"Congrats !!!!!\n{data[stuid]['name']} got 'C' grade")
        print("Feedback: Can work hard to achieve more!")
    else:
        print(f"Congrats !!!!!\n{data[stuid]['name']} got 'D' grade")
        print("Feedback: You have to work hard!")
else:
    print("Student has not attempted the test.")