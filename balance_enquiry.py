from db_connection import get_connection
conn = get_connection()
cur = conn.cursor()
balance_acc_no = int(input('Enter Account Number:'))
cur.execute('select name,balance from accounts where acc_no = %s',(balance_acc_no,))
result = cur.fetchone()
if result is None:
    print("Invalid Account Number")
else:
    name = result[0]
    balance = result[1]
    print('Account Holder:',name)
    print('Current Balance:',balance)