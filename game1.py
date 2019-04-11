import random

a=random.randint(222,999)
print(a)
b=int(input("enter the number you heard."))
p=0
c=3

while(a==b):
 a=a*10+random.randint(1,9)
 print(a)
 b=int(input("enter the number you heard."))
 p+=1
 

  
