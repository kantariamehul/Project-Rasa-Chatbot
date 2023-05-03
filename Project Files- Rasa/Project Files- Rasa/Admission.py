import sqlite3

def insert_adm(name, surname, result, city, mobile, course, education, degree, branch):
 conn = sqlite3.connect("adm_students.db") 
 cursor = conn.cursor()

 #sql="CREATE TABLE adm_stu (Name NVARCHAR(50), Surname NVARCHAR(50), Result NVARCHAR(50), City NVARCHAR(50), Mobile NVARCHAR(50), Course NVARCHAR(50), Education NVARCHAR(50), Degree NVARCHAR(50), Branch NVARCHAR(50));"

 sql="INSERT INTO adm_stu (Name, Surname, Result, City, Mobile, Course, Education, Degree, Branch) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
 cursor.execute(sql,(name, surname, result, city, mobile, course, education, degree, branch))
   
 # Commit your changes in the database
 conn.commit()
 conn.close()