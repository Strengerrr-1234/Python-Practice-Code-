import pymysql as mq
mysql=mq.connect(host="localhost",
                 user="root",
                 passwd="",
                 database="school")
mycursor=mysql.cursor()
try:
    #st_id,st_name,st_class,st_email
    ins="INSERT INTO student (st_name,st_class,st_email) values(%s,%s,%s)"
    t = ("aaryan",'12th','aaryanashakyawar@gmail.com')
    mycursor.execute(ins,t)
    mysql.commit();
    print("Insert Data")
except:
    print("Error...")