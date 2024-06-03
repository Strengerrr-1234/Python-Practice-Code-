import pymysql as mq

db = mq.connect(host="localhost",user="root",password="",db="school")
cur= db.cursor()

print("{:<15}".format("Order Avg"))

try:
    sql="SELECT avg(order_amount) from orders"
    cur.execute(sql)
    sdata=cur.fetchall()
    for a in sdata:
        print(a[0])

except:
    pass