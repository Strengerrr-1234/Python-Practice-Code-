import pymysql as mq

mysql=mq.connect("localhost","root","","school")
mycursor=mysql.cursor()

print("{:<15}{:<15}{:<15}".format("Order Id","Order Date","Order Amount"))
try:
    sql="Select order_id,order_date,order_amount from orders where order_id i(1,6"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for s in sdata:

        print("{:<15}{:<15}{:<15}".format(s[0],str(s[1]),s[2]))
except:
    print("Eroor...")


