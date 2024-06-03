import pymysql as mq

mysql=mq.connect("localhost","root","","school")
mycursor=mysql.cursor()

print("{:<15}{:<20}{:<20}".format("User id","User Name","User Address"))
try:
    sql="Select state.state_id,state.state_name,country.country_name from state ,country where state.country_id=country.country_id"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for s in sdata:
        print(s)
        print("{:<20}{:<20}{:<20}".format(s[0],s[1],s[2]))
except:
    print("Error...")