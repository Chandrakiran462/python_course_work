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
def Welcome():
    print('Welcome to ATM'.center(50,'*'))
def Menu():
    print('\n[C]heck_Balance')
    print('[D]eposite')
    print('[W]itdraw')
    print('[T]ransection_History')  
    print('[E]xit\n')
def Login():
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
def Check_balance():
    if login_status and acc_num:
        print(f'\nCurrent Balance: {data[acc_num]["balance"]}')
    else:
        print("You need to login again")


def Deposit():
    if login_status and acc_num:
        amount=int(input("Enter the amount to deposit: "))
        data[acc_num]['balance']+=amount
        data[acc_num]['history'].append(f'Deposited - ${amount}')
        print(f'${amount} is successfully desposited')
    else:
        print("You need to login again")

def Withdraw():
    if login_status and acc_num:
        amount=int(input("Enter the amount to withdraw: "))
        if data[acc_num]['balance']>=amount:
            data[acc_num]['balance']-=amount
            data[acc_num]['history'].append(f'Withdraw - ${amount}')
            print(f'${amount} is successfully Withdraw')
        else:
            print("Insufficient Balance")
    else:
        print("You need to login again")

def View_transaction():
    if login_status and acc_num:
        if data[acc_num]['history']:
            print("Transactions History".center(50,'-'))
            for i in data[acc_num]['history']:
                print(i)
            else:
                print("End of the history".center(50,'-'))

        else:
            print("No Transactions")
    else:
        print("You need to login again")