import pymysql as mq

mysql=mq.connect("localhost","root","","school")
mycursor=mysql.cursor()

print("{:<15}{:<20}{:<20}".format("State id","State Name",'Country Name'))

sql="Select state.state_id,state.state_name,country.country_name from state left join country on state.country_id=country.country_id"
mycursor.execute(sql)
sdata=mycursor.fetchall()
for s in sdata:
        print("{:<15}{:<20}{:<20}".format(s[0],s[1],s[2]))
