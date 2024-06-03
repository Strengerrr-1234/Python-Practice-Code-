import  pymysql as mq

mysql=mq.connect("localhost","root","","school")
mycursor=mysql.cursor()

print("{:<15}{:<20}{:<20}{:<20}".format("Student Id","Student Name","Student Class","Student Email"))


try:
    name=input("Enter the student Name = ")
    sql="Select * from student where student '"+ name +"'"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for s in sdata:

        print("{:<15}{:<20}{:<20}{:<20}".format(s[0],s[1],s[2],s[3]))
except:
    print("Error...")