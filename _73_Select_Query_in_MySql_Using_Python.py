import pymysql as mq
#Server connection or database connection

mysql=mq.connect(host="localhost",
                 user="root",
                 passwd="",
                 database="school")

mycursor = mysql.cursor()

print("{:<15} {:<20} {:<20} {:<20}".format("Student Id","Student Name","Student Email","Student Class"))

try:
    sql="Select * from student"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()

    for s in sdata:
        print("{:<15} {:<20} {:<20} {:<20}".format(s[0],s[1],s[3],s[4]))

except:
    print("Error...")