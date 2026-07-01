from db_connection import get_connection

def transfer():
    conn = get_connection()
    cur = conn.cursor()
    sender_acc_no = int(input("Enter Sender Account Number:"))
    sender_pin = int(input("Enter Sender PIN:"))
    receiver_acc_no = int(input("Enter Receiver Account Number:"))
    amount = float(input("Enter Transfer Amount:"))
    if sender_acc_no == receiver_acc_no:
        print("Cannot transfer to same account")
        return
    if amount <= 0:
        print("Invalid Amount")
        return
    cur.execute(
        'select balance from accounts where acc_no = %s and pin = %s',
        (sender_acc_no, sender_pin)
    )
    sender = cur.fetchone()
    if sender is None:
        print("Invalid Sender Account or PIN")
        return
    cur.execute(
        'select balance from accounts where acc_no = %s',
        (receiver_acc_no,)
    )
    receiver = cur.fetchone()
    if receiver is None:
        print("Invalid Receiver Account")
        return
    sender_balance = sender[0]
    if sender_balance < amount:
        print("Insufficient Balance")
        return
    receiver_balance = receiver[0]
    new_sender_balance = sender_balance - amount
    new_receiver_balance = receiver_balance + amount
    cur.execute(
        'update accounts set balance = %s where acc_no = %s',
        (new_sender_balance, sender_acc_no)
    )
    cur.execute(
        'update accounts set balance = %s where acc_no = %s',
        (new_receiver_balance, receiver_acc_no)
    )
    conn.commit()
    print("Transfer Successful")
    print("Amount Transferred:", amount)
    print("Sender New Balance:", new_sender_balance)