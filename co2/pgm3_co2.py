l=[]
n=int(input("enter the number of elements:"))
print("enter the elements")
for i in range(0,n):
    a=int(input())
    l.append(a)
print(l)
sum=0
for i in l:
    sum=sum+i
print("sum",sum)
