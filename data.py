import mysql.connector # pip install mysql-connector-python

IpAvailable = ['***', '***', '***', '****', '****'] # Since your gonna search by the name the ips you have, put the names you have in here

db = mysql.connector.connect(host='localhost',
                             database='******', # Your Database Name
                             user='rl242', # The user who created the database, can be root
                             password='******' # The password
                             )

mycursor = db.cursor()

start = "USE ***;" # Use your database
sql = "INSERT INTO ** (column_1, column_2) VALUES (%s, %s)" # Insert the data in the database via python
val = [
  ('****', '***'), # Value 1
  ('****', '***'), # Value 2
]

mycursor.executemany(start, sql, val) # Execute Each Command

db.commit()                             

# Code SQL Injection data in the table
