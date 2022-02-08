l=[1,2,3,4,5,6,7,8,9,10]
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print("even",e)
print("odd",o)
