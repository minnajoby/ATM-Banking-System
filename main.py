from create_account import create_account
from login import login
from deposit import deposit
from withdraw import withdraw
from balance import balance_enquiry
while True:
    print("===== ATM BANKING SYSTEM =====\n")
    print("1.Create Account\n2.Login\n3.Deposit\n4.Withdraw\n5.Balance Enquiry\n6.Exit\n")
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        create_account()
    elif choice == 2:
        login()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        balance_enquiry()
    elif choice == 6:
        break
    else:
        print("Invalid Choice")
