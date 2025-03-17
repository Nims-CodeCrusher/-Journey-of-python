import random

l1=[]
l2=[]
l3=[]

n=int(input("Enter limit =>"))

for i in range(1,n+1):
    a = random.randint(-10,50)
    l1.append(a)
    
print("your random value is:- ",l1)

for i in l1:
    if i%2==0:
        l2.append(i)
    else:
        l3.append(i)
     
print("your even value is:- ",l2)
print("your odd value is:- ",l3)