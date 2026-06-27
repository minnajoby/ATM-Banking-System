from db_connection import get_connection
def create_account():
    conn = get_connection()
    cur = conn.cursor()
    create_acc_no = int(input('Enter Account Number:'))
    create_name = input('Enter Name:')
    create_pin = int(input('Enter PIN:'))
    create_balance = float(input('Enter Initial Deposit:'))
    cur.execute('select acc_no from accounts where acc_no = %s',(create_acc_no,))
    result = cur.fetchone()
    if result is not None:
        print("Account Already exists")
    else:
        cur.execute('insert into accounts (acc_no,name,pin,balance) values(%s,%s,%s,%s)',(create_acc_no,create_name,create_pin,create_balance,))
        conn.commit()
        print('Account Created Successfully')


