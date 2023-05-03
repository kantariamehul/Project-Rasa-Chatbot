import sqlite3

def insert_email(email, enrollment):
 conn = sqlite3.connect("mu_students.db") 
 cursor = conn.cursor()
 
 #sql="CREATE TABLE mu_stu (Email NVARCHAR(50),Enrollment NVARCHAR(50));"
 #cursor.execute(sql)

 sql="INSERT INTO mu_stu (Email, Enrollment) VALUES (?, ?);"
 cursor.execute(sql,(email, enrollment))
   
 #print("sql=",sql)

 # Commit your changes in the database
 conn.commit()

 #print(cursor.rowcount,"Record Inserted")
 cursor.execute("SELECT * FROM mu_stu;")

 conn.close()