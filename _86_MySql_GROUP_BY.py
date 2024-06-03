import pymysql as mq

mysql=mq.connect("localhost","root","","school")
mycursor=mysql.cursor()

print("{:<15} {:<15}".format("Emp Count","Emp DName"))
try:
    sql="Select count(*),dname from emp group by dname"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for s in sdata:

        print("{:<15}{:<15}".format(s[0],s[1]))
except:
    print("Error...")