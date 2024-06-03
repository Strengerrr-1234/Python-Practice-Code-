# Create Table in MySql Python Using xampp or phpmyadmin

import pymysql as mq
conn=mq.connect(
    host="localhost",
    user="root",
    passwd="",
    database="school"
)
mysqlc=conn.cursor()
# table student(st_id,st_name,st_class,st_email)

tc="create table student(st_id INT primary key auto_increment, st_name varchar(50),st_class varchar(50))"
mysqlc.execute(tc)