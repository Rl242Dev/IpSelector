import mysql.connector # pip install mysql-connector-python

IpAvailable = ['***', '***', '***', '****', '****'] # Since your gonna search by the name the ips you have, put the names you have in here

db = mysql.connector.connect(host='localhost',
                             database='******', # Your Database Name
                             user='rl242', # The user who created the database, can be root
                             password='******' # The password
                             )

mycursor = db.cursor()

sql = "INSERT INTO ** (column_1, column_2) VALUES (%s, %s)"
val = [
  ('****', '***'),
  ('****', '***'),
]

mycursor.executemany(sql, val)

db.commit()                             

# Code SQL Injection data in the table
