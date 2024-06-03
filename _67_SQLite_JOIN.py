import sqlite3
conn=sqlite3.connect("Sqlite.db")
print("STUDENT ID","STUDENT Name","STUDENT FEES")
# data=conn.execute("SELECT *FROM fees as f inner join student as s on f.st_id=s.st_id")
data=conn.execute("SELECT f.st_id,s.st_name,f.fees_amount FROM fees as f inner join student as s on f.st_id=s.st_id")
for a in data:
    print(a)
conn.close()