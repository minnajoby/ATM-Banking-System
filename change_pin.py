from db_connection import get_connection

def change_pin():
    conn = get_connection()
    cur = conn.cursor()
    acc_no = int(input("Enter Account Number:"))
    current_pin = int(input("Enter Your Current Pin:"))
    cur.execute('select pin from accounts where acc_no = %s and pin = %s',(acc_no,current_pin,))
    result = cur.fetchone()
    if result is None:
        print("Invalid Account Number or PIN")
    else:
        new_pin = int(input("Enter New PIN:"))
        confirm_pin = int(input("Confirm New PIN:"))
        if new_pin!=confirm_pin:
            print("PINs do not match")
        elif new_pin==current_pin:
            print("New PIN cannot be same as old PIN")
        else:
            cur.execute('update accounts set pin = %s where acc_no = %s',(new_pin,acc_no,))
            conn.commit()
            print("PIN Changed Successfully")