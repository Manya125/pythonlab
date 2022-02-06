file_obj=open("file1.txt","r")
#filefull = file_objread()
file_list=[]

condition=True

while condition:
    x = file_obj.readline()
    file_list.append(x)
    if not x:
        condition = False

print("the file covered to list is :")
print(file_list)
