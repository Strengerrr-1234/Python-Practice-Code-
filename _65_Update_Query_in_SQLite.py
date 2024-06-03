import sqlite3
conn=sqlite3.connect("Sqlite.db")
conn.execute('''
    update student set st_name='ram1',st_class = '10th' where st_id=1
    
    ''')

conn.commit()
conn.close()