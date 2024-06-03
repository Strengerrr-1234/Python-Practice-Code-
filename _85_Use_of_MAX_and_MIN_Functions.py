import pymysql as mq

mysql=mq.connect("localhost","root","","school")
mycursor=mysql.cursor()

print("{:<15}".format("Order Amount"))
try:
    sql:"Select max(order_amount) from orders "         # min and max
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for s in sdata:

        print("{:<15}".format(s[0]))
except:
    print("Error...")