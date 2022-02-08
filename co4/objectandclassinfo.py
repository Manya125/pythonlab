class Student:
    count = 0
    def getdata(self,name,roll,grade):
        self.name1 = name
        self.roll1 = roll
        self.grade1 = grade
       
    def showdetails(self):
        print("name of the student is ",self.name1)
        print("roll number of the student is " ,self.roll1)
        print("class of the student is ",self.grade1)

    def __del__(self):
        class_name =self.__class__.__name__
        print(class_name,"destroyed")

obj1 = Student()
#obj2 = Student('arun',109,'mca')
#obj3 = Student('adarsh',102,'mca')

obj1.getdata('binoy',112,'mca')


obj1.showdetails()
#obj2.showdetails()
#obj3.showdetails()

del obj1



