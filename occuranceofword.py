s=input("enter a string")
l=s.split()
d={x:l.count(x)for x in l}
print(d)
