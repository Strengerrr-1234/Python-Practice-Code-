import pymysql as mq

mysql=mq.connect("localhost","root","","school")
x = mysql.cursor()
id = input("Enter the student_id ")

sql = "DELETE FROM student WHERE st_id =%s"
try:
    x.execute(sql,id)
    mysql.commit()
    print("Delete Student Detail Succesfully .")
except:
    print("Error...")