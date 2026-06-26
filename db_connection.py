import pymysql

def get_connection():
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = input("Enter DB Password: "),
        database = 'atm_system'
    )
    return conn
