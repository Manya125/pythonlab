class Student:
    def __init__(self,rollno,name,course,mark1,mark2,mark3):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def display(self):
        print("name of the student is:",self.name)
        print("roll no of the student is:",self.rollno)
        print("class of the student is:",self.course)

    def total(self):
        self.total = int(self.mark1+self.mark2+self.mark3)
        self.percent = (self.total/300)*100
        print("percentage of total marks is ",self.percent)


n = int(input("enter total number of students:"))

obj = []

for i in range(0,n,1):
    print("enter the roll number of student",i+1,":")
    rollno = int(input())
    print("enter the name of student",i+1,":")
    name = input()
    print("enter the course of student",i+1,":")
    course = input()
    print("enter the mark1 of student",i+1,":")
    mark1 = int(input())
    print("enter the mark2 of student",i+1,":")
    mark2 = int(input())
    print("enter the mark3 of student",i+1,":")
    mark3 = int(input())
    obj.append(Student(rollno,name,course,mark1,mark2,mark3))

print("******student details******")

for i in obj:
    i.display()
    i.total()
