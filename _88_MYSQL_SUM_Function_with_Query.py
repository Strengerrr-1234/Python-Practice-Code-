import pymysql as mq

mysql=mq.connect("localhost","root","","school")
mycursor=mysql.cursor()

print("{:<5}".format("Order Amount"))
try:
    sql="Select sum(order_amount) from orders"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for s in sdata:

        print("{:<15}".format(s[0]))
except:
    print("Error...")