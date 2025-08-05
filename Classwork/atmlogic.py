data = {
    12345:{'pin': 123,'balance': 56789,'history':[]},
    23456:{'pin': 123,'balance': 56789,'history':[]},
    34568:{'pin': 123,'balance': 56789,'history':[]},
    45678:{'pin': 123,'balance': 56789,'history':[]},
    56789:{'pin': 123,'balance': 56789,'history':[]},
    67894:{'pin': 123,'balance': 56789,'history':[]},
    78912:{'pin': 123,'balance': 56789,'history':[]},
}
acc_num = None
login_status = None
def welcome():
    print('Welcome to ATM'.center(50,'*'))
def menu():
    print('\n[C]heck_Balance')
    print('[D]eposite')
    print('[W]itdraw')
    print('[T]ransection_History')  
    print('[E]xit\n')
def login():
    account_number = int(input("Enter Acctount Number: "))
    pin = int(input('Enter Pin number: '))
    global acc_num
    global login_status
    if account_number in data:
        if data[account_number]['pin']==pin:
            print("Login Successful")
            acc_num=account_number
            login_status=True
            return True
    else:
        print('Invalid Accounnt Number')
        login_status = False
        return False