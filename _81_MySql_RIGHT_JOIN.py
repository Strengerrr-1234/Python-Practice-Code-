import pymysql as mq

mysql=mq.connect("localhost","root","","school")
mycursor=mysql.cursor()

print("{:<15}{:<20}{:<20}".format("User id","User Name","User Address"))
try:
    sql="Select user.user_id,user.user_name,user.user_address,orders.order_id,orders.orders_amount from user right join orders.user_id"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for s in sdata:
        print(s)
        print("{:<20}{:<20}{:<20}".format(s[0],s[1],s[2]))
except:
    print("Error...")