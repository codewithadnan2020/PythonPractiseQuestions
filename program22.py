import mysql.connector

db=mysql.connector.connect(host="localhost", user="root", password="", database="pythonMysql")

cursor=db.cursor()

cursor.execute("SELECT * FROM `employee`")
for records in cursor:
   print(records)