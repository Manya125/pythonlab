class Student:
    def __init__(self,rollno,name,course):
        self.rollno = rollno
        self.name = name
        self.course = course

    def display(self):
        print("name of the student is:",self.name)
        print("roll no of the student is:",self.rollno)
        print("class of the student is:",self.course)


n = int(input("enter total number of students:"))

obj = []

for i in range(0,n,1):
    print("enter the roll number of student",i+1,":")
    rollno = int(input())
    print("enter the name of student",i+1,":")
    name = input()
    print("enter the course of student",i+1,":")
    course = input()
    obj.append(Student(rollno,name,course))

print("******student details******")

for i in obj:
    i.display()
