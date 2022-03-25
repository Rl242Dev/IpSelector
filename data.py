import mysql.connector

IpAvailable = ['Gabin', 'Loan', 'Theo', 'Lucien', 'Timeo']

db = mysql.connector.connect(host='localhost',
                             database='IpData',
                             user='rl242',
                             password='31#Nigi2'
                             )

mycursor = db.cursor()

sql = "INSERT INTO IpList (name, ip) VALUES (%s, %s)"
val = [
  ('Gabin', '90.66.86.54'),
  ('Loan', '31.36.137.199'),
  ('Theo', '86.207.6.135'),
  ('Lucien', '86.202.140.97'),
  ('Timeo', '36.31.176.47'),
]

mycursor.executemany(sql, val)

db.commit()                             

# Code SQL Injection data in the table