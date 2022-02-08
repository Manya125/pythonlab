n=int(input("enter a number"))
n1=0
s=0
while(n>0):
    n1=n%10
    s=s+n1
    n=int(n/10)
print("sum of digits",s)
