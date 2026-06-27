from db_connection import get_connection
def login():
    conn = get_connection()
    cur = conn.cursor()
    acc_login = int(input("Enter Account Number:"))
    pin_login = int(input("Enter PIN:"))
    cur.execute('select acc_no from accounts where acc_no = %s',(acc_login,))
    result = cur.fetchone()
    if result is None:
        print("Invalid Account Number")
    else:
        cur.execute('select name from accounts where acc_no = %s and pin = %s',(acc_login,pin_login,))
        pin_fetch = cur.fetchone()
        if pin_fetch is None:
            print("Invalid PIN")
        else:
            name = pin_fetch[0]
            print("Login Successful")
            print("Welcome",name)
