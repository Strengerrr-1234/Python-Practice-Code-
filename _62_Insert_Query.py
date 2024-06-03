import sqlite3
conn=sqlite3.connect("Sqlite.db")

ins='''
    insert into student (st_name,st_Class,st_email) VALUES
        ('Yoganshi','10th',"YoganshiDverma@gmail.com")

    '''
conn.execute(ins)
conn.commit()
conn.close()