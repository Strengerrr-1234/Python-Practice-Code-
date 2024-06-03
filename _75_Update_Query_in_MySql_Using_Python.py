import pymysql as mq

mysql=mq.connect("localhost","root","school")
cursorobj=mysql.cursor()

name=input("Enter the student name ")
class_name=input("Enter the Class Name ")
st_id=input("Enter The Student Id ")

sql = "UPDATE student set st_name=%s,st_class=%s where st_id=%s"
data=(name,class_name,st_id)

try:
    cursorobj.execute(sql,data)
    mysql.commit()
    print("Data Updated")
except:
    print("Error..")