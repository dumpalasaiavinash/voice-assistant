
import pymysql

db=pymysql.connect("sql12.freemysqlhosting.net","sql12225454","ZhjfPu9eAU","sql12225454")
a=0;k=0
p=db.cursor()

u=input("Enter your name:");
p.execute("SELECT name1,name2 FROM contacts")
c=p.fetchall()
for i,j in c:
 if(u==i):
  v=j
  break
p.close()

p=db.cursor()
p.execute("SELECT text1,text2 FROM contacts")
c=p.fetchall()
for i,j in c:
 if(i==''):
  print(j)
 if(j==''):
  print(' '*40,end='')
  print(i)
p.close()
while(a!=1):
 c=db.cursor()
 c.execute("SELECT * FROM contacts")
 if(k!=0):
  c.execute("INSERT INTO contacts (name1,name2,text1,text2) VALUES('" + u + "','" + v + "','" + q + "',' ');")
  c.execute("SELECT text1,text2 FROM contacts")
  z=c.fetchall()
  for i,j in z:
   x=i
  print(' '*40,end='')
  print(x)
 c.close()
 db.commit()
 q=input("\n\nEnter the text , It should be like a placeholder butnot like a value to solve a problem:")
 k+=1

db.close()










