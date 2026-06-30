from db_connection import get_connection
from datetime import datetime
def deposit():
    conn = get_connection()
    cur = conn.cursor()
    dep_acc_no = int(input("Enter Account Number:"))
    cur.execute('select balance from accounts where acc_no = %s',(dep_acc_no,))
    result = cur.fetchone()
    if result is None:
        print("Invalid Account Number")
    else:
        amount = float(input("Enter Deposit Amount:"))
        if amount <= 0:
            print('Invalid Amount')
        else:
            current_balance = result[0]
            new_balance = current_balance + amount
            cur.execute('update accounts set balance = %s where acc_no = %s',(new_balance,dep_acc_no,))
            transaction_date = datetime.now()
            cur.execute('insert into transactions(acc_no,transaction_type,amount,transaction_date) values(%s,%s,%s,%s)',(dep_acc_no,'Deposit',amount,transaction_date))
            conn.commit()
            print("Deposit Successful")
            print("Updated Balance:",new_balance)