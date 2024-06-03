import pymysql as mq

db = mq.connect(host="localost",user="root",password="",db="school")
cur = db.cursor()

print("{:<15}".format("Total Count"))
try:
    sql="SELECT count(*) from orders"
    cur.execute(sql)
    sdata=cur.fetchall()
    for a in sdata:
        print(a[0])

except:
    pass