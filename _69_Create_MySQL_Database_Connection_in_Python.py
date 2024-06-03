import pymysql as mq

# Server Name -> localhost
# Username -> root
# password -> ''

myobj=mq.connect(
    host="localhost",
    user="root",
    passwd=""
)
cursorobj=myobj.cursor()
try:
    db="create database school"
    cursorobj.execute(db)
    print("Databse created")
except:
    print("Database error....")

