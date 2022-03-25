# IpSelector 📶

## Setup 🔩

### Requirements :

 #### Linux/WSL 📟
 #### Mysql 🔐
 #### Python 📊
 #### Git 📂

### How clone this repo ?

1. In your Linux create a folder : "mkdir folder_name" and go in : "cd folder_name"
2. Clone this repo "git clone https://github.com/Rl242Dev/IpSelector";

### How to set it up ?

#### If you aren't familiar with mysql dont worry everything is explained.

1. In your sql shell create a database : "CREATE DATABASE db_name;" and use it : "USE db_name;"
2. Create a table : "CREATE TABLE table_name (name CHAR(20), ip CHAR(20));"

### Insert data in the database/table ?

![image](https://user-images.githubusercontent.com/74558778/160200802-4cfc0aea-a4b7-46e0-a596-f9e56031ffa1.png)

   1. Set database="" as the name of your database created earlier.
   2. Set user="" as your name in mysql, can be root.
   3. Set password="" as your password to connect in mysql.
   
   ![image](https://user-images.githubusercontent.com/74558778/160201896-f9b850aa-0538-466e-8899-0c1c15666720.png)

  4. Change IpAvailable to : ['Tim', 'Tom', 'Tam',]
   
 ![image](https://user-images.githubusercontent.com/74558778/160201163-bd7e0ead-c60d-4d87-9932-a0dbc7f267f1.png)

   1. Change start to "USE db_name;"
   2. Change sql to "INSTERT INTO table_name (name, ip) VALUES (%s, %s)"
   3. Change val to your values ('Name of person', 'ip of person')
   4. Do the same in main.py

### How to search data in the database the python script ?

1. To search in the database type at end in main.py : "search_ip('Name of person')
