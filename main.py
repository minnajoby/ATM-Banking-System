import pymysql
conn = pymysql.connect(host = 'localhost',user = 'root',password = '1215',database = 'atm_system')
cur = conn.cursor()
cur.execute('select * from accounts')
conn.commit()
res = cur.fetchmany(size = 10)
for col in res:
    print(col)
conn.close()

