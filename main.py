import mysql.connector
from mysql.connector import Error
from data import IpAvailable # Import the array from Data.py

db = mysql.connector.connect(host='localhost',
                             database='****',
                             user='rl242',
                             password='*****'
                             )

mycursor = db.cursor() # Create a cursor in mysql

mycursor.execute("USE ***;") # Use your database 
    
def search_ip(string): # Name of the person you want to search the ip
    if string in (IpAvailable):
        mycursor.execute("SELECT ip FROM IpList WHERE name = '"+string+"' LIMIT 1;" ) # Search in the database the name of the perseon + ip
        myresult = mycursor.fetchall() # Create a var for the result
        for x in myresult:
            print(x)
    else:
        print('Error 404, Ip not available') # Print error if the name of the person isn't in the database
