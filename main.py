import mysql.connector
from mysql.connector import Error
from data import IpAvailable

db = mysql.connector.connect(host='localhost',
                             database='IpData',
                             user='rl242',
                             password='31#Nigi2'
                             )

mycursor = db.cursor()

mycursor.execute("USE IpData;")
    
def search_ip(string):
    if string in (IpAvailable):
        mycursor.execute("SELECT ip FROM IpList WHERE name = '"+string+"' LIMIT 1;" )
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    else:
        print('Error 404, Ip not available')