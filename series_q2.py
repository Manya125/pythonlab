file_obj = open('prgm2.txt','r+')

condition = True


print("The line that have more than 5 letters and starting with capital letter is:")

while condition:
    line = file_obj.readline()
    words = line.split(" ")
    if(len(words)>5):
        x = words[0]
        if(x[0].isupper()):
            print(line)
    if not line:
        condition = False
        print("end of the file")
