# SQLite (DB Create and Connection) & How to Create Table in Python
import sqlite3
conn=sqlite3.connect("Sqlite.db")
conn.execute('''
        Create table student(
            st_id INT AUTO_INCREMENT PRIMARY KEY,
            st_name VARCHAR(50),
            st_Class VARCHAR(30),
            st_email VARCHAR(30)
        )
    ''')
conn.close()