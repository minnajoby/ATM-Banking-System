from db_connection import get_connection
def mini_statement():
    conn = get_connection()
    cur = conn.cursor()
    mini_acc_no = int(input("Enter Account Number:"))
    cur.execute('select acc_no from accounts where acc_no = %s',(mini_acc_no,))
    result = cur.fetchone()
    if result is None:
        print("Invalid Account")
    else:
        cur.execute('select * from transactions where acc_no = %s',(mini_acc_no,))
        result = cur.fetchall()
        if not result:
            print("No transactions Found")
        else:
            for row in result:
                print(row[2],row[3],row[4])

