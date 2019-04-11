#import sqlite3
import pymysql

#db=sqlite3.connect("data")
db=pymysql.connect("sql12.freemysqlhosting.net","sql12225454","ZhjfPu9eAU","sql12225454")
u = str(input("Enter your name1:"))
v = str(input("Enter your name2:"))

cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS contacts (name1 char(30),name2 char(30),text1 char(60),text2 char(60))")
cur.execute("INSERT INTO contacts (name1,name2,text1,text2) VALUES ('" + u + "','" + v + "',' ',' ');")

db.commit()
db.close()

