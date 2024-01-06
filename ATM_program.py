# PYTHON ATM PROGRAM BY PYTHONDEX
# Visit https://pythondex.com for more information

user = {
    'pin': 2345,
    'balance':1000
}



def widthdraw_cash():
    while True:
        amount = int(input("Enter the amount of money you want to widthdraw: "))
        if amount > user['balance']:
            print("You don't have sufficient balance to make this widthdrawal")
        else:
            user['balance'] = user['balance'] - amount
            print(f"{amount} Dollars successfully widthdrawn your remaining balance is {user['balance']} Dollars")
            print('')
            return False
        
def debit_cash():
    amount = int(input("Enter the amount of money you want to debit: "))
    user['balance'] = user['balance'] + amount
    print(f"{amount} Dollars successfully debited your remaining balance is {user['balance']} Dollars")
    print('')

def balance_enquiry():
    print(f"Total balance {user['balance']} Dollars")
    print('')


is_quit = False

print('')
print("Welcome to the Pythondex ATM")

# print('\n')
# print("1. Want to login into your account ?\n")
# print("2. Want to register for new account ?")

# choice1 = int(input('Enter your choice :  '))


# if(choice1 == 1):

#     username = input('Please enter your username: ')
pin = int(input('Please enter your four digit pin: '))

    

if pin == user['pin']:
    while is_quit == False:
        print("what do you want to do")
        print(" Enter 1 to Debit Cash \n Enter 2 to Widthdraw Cash \n Enter 3 for Balance Enquiry \n Enter 4 to Quit")

        query = int(input("Enter the number corresponding to the activity you want to do: "))

        if query == 1:
            debit_cash()
        elif query == 2:
            widthdraw_cash()
        elif query == 3:
            balance_enquiry()
        elif query == 4:
            is_quit = True
        else:
            print("Please enter a correct value shown")
else:
    print("Entered wrong pin")



