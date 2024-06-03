# import sqlite3
# conn=sqlite3.connect("Sqlite.db")
# data=conn.execute("SELECT *FROM student where st_name='Yoganshi'")
# for n in data:
#     print(n[0],"   ",n[1],"  ",n[2],n[3])
#

import sqlite3
conn=sqlite3.connect("Sqlite.db")
st_name = input("Enter the name=")
# "SELECT *FROM student where st_name='"+st_name"'
# data=conn.execute("SELECT * FROM student where st_name like '%"+st_name+"%'")
#and
#or


data=conn.execute("SELECT * FROM student where st_name like '%"+st_name+"%' and st_class '"+ st_Class +"' " )
for n in data:
    print(n[0],"   ",n[1],"  ",n[2],n[3])