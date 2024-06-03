# Select Query - Order By & Limit in Python SQLite
import sqlite3
conn=sqlite3.connect("Sqlite.db")
data = conn.execute("SELECT * FROM student")

print("Student Id","Student Name","Student Class","Student Email")
for n in data:
    # print(n)
    print(n[0],n[1],n[2],n[3])


#  set limit print particular output

# import sqlite3
# conn=sqlite3.connect("Sqlite.db")
# data = conn.execute("SELECT * FROM student limit 0,2" )
#
# print("Student Id","Student Name","Student Class","Student Email")
# for n in data:
#     # print(n)
#     print(n[0],n[1],n[2],n[3])