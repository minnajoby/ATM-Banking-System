from create_account import create_account
from login import login
from deposit import deposit
from withdraw import withdraw
from balance import balance_enquiry
from mini_statement import mini_statement
from transfer import transfer
from change_pin import change_pin
while True:
    print("===== ATM BANKING SYSTEM =====\n")
    print("1.Create Account\n2.Login\n3.Deposit\n4.Withdraw\n5.Balance Enquiry\n6.Mini Statement\n7.Transfer Money\n8.Change PIN\n9.Exit\n")
    try:
        choice = int(input("Enter Your Choice:"))
    except ValueError:
        print("Please enter a valid number")
        continue
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
        mini_statement()
    elif choice == 7:
        transfer()
    elif choice == 8:
        change_pin()
    elif choice == 9:
        break
    else:
        print("Invalid Choice")
