import pymysql as mq

mysql=mq.connect("localhost","root","","school")
mycursor=mysql.cursor()

print("{:<15}".format("Emp DName"))
try:
    sql="Select distinct(dname) from emp"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for a in sdata:

        print("{:<15}".format(s[0]))
except:
    print("Error...")