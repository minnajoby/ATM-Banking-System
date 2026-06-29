from db_connection import get_connection
from datetime import datetime
def withdraw():
    conn = get_connection()
    cur = conn.cursor()
    withdraw_acc_no = int(input("Enter Account Number:"))
    cur.execute('select balance from accounts where acc_no = %s',(withdraw_acc_no,))
    result = cur.fetchone()
    if result is None:
        print("Invalid Account Number")
    else:
        amount = float(input("Enter Withdrawal Amount:"))
        if amount <= 0:
            print("Invalid Amount")
        else:
            current_balance = result[0]
            print("Current Balance:",current_balance)
            if current_balance < amount:
                print("Insufficient Balance")
            else:
                new_balance = current_balance - amount
                cur.execute('update accounts set balance = %s where acc_no = %s',(new_balance,withdraw_acc_no,))
                transaction_date = datetime.now()
                cur.execute('insert into transactions(acc_no,transaction_type,amount,transaction_date) values(%s,%s,%s,%s)',(withdraw_acc_no,'withdraw',amount,transaction_date,))
                conn.commit()
                print("Withdrawal Successful")
                print("Updated Balance:",new_balance)