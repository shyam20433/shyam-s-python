#removing words in dictionary
d={}
n=int(input("enter the range "))
for i in range (1,n+1):
    customercode=int(input("enter customer code"))
    name=input("enter the name")
    d[name]=customercode
print("dictionary",d)
m=int(input("enter how many name you want to remove"))
for j in range (0,m+1):
    remove=input("enter the name you need to remove ")
    d.pop(remove)
print(d)
#factorial
n=int(input("enter the number"))
product=1
for i in range(5):
    product=product*i
print(product)
#showing top 5 ranks
d={}
n=int(input("enter the totall"))
for i in range (1,n+1):
    roll_no=int(input("student roll no ="))
    mark=int(input("student mark ="))
    d[roll_no]=mark
print(d)
m=int(input("enter the top marks you want to see"))
new=[]
for j in range(1,m+1):
    maxi=max(d,key=d.get)
    d.pop(maxi)
    new.append(maxi)
print(new)
#display patner
for i in range (1,6):
    for j in range (1,i+1):
        print("*",end=" ")
    print()
    
#while loop
i=100
while(i<=1000):
    print(i)
    i=i+100
#while for reverse the number
i=200
while(i>0):
    print(i)
    i=i-1
#while loop for factorial
n=int(input())
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print(fact)
#finding odd or even usins def function
def evenorodd(num):
    if num%2==0 :
        print(num,"it is even")
    else:
        print(num,"it is odd")
evenorodd(int(input("enter the number")))
#range for num in def function
def printrange(a):
    for i in range (1,a+1):
        print(i,end=",")
printrange(int(input("enter the number")))
#if statement in def funtion
username="shyam"
password="123"

user=input()
passw=(input())

def validate():
    if (username==user) and (password==passw) :
        print("valid")
    else:
        print("invalid")
validate()







