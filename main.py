while True:
    print("===== ATM BANKING SYSTEM =====\n")
    print("1.Create Account\n2.Login\n3.Deposit\n4.Withdraw\n5.Balance Enquiry\n6.Exit\n")
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        print("Create Account selected")
    elif choice == 2:
        print("Login selected")
    elif choice == 3:
        print("Deposit selected")
    elif choice == 4:
        print("Withdraw selected")
    elif choice == 5:
        print("Balance selected")
    elif choice == 6:
        break
    else:
        print("Invalid Choice")
