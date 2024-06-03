import sqlite3
conn=sqlite3.connect("Sqlite.db")
st_id= input("Enter the student Id:- ")
conn.execute("DELETE FROM student where st_id="+st_id )
conn.commit()
conn.close()