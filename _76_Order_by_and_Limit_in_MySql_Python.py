import pymysql as mq

mysql=mq.connect("localhost","root","","school")
mycursor=mysql.cursor()

print("{:<15}{:<20}{:<20}".format("State id ","State Name ", "Country ID"))
try:
    # ASC , DESC
    # sql ="Select * from state order by state_name DESC"
    sql ="Select * from state order by state_id ASC LIMIT 4,2"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()

    for s in sdata:
        print("{:<15}{:<20}{:<20}".format(s[0],s[1],s[2]))
except:
    print("Error...")