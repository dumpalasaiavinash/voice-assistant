import pymysql

db=pymysql.connect("den1.mysql2.gear.host","alasya2","alasya2.0","alasya2")


c=db.cursor()
c.execute("SELECT * FROM contacts")
for i,j,k,l in c: 
 print(i)
 print(j)
 print(k)
 print(l)
 print('-'*20)
 

c.close()
db.commit()
db.close()

