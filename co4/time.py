class time:
	def __init__(self,h,m,s):
		self.__hour=h
		self.__minute=m
		self.__second=s
	def display(self):
		print(self.__hour,self.__minute,self.__second)
	def __add__(self,other):
		x=(self.__hour+self.__hour+(self.__minute+other.__minute+(self.__second+other.__second)//60)//60)%24
		y=(self.__minute+other.__minute+(self.__second+other.__second)//60)%60
		z=(self.__second+other.__second)%60
		print(x,y,z)
		
print("Time 1(24 hour format)")
obj1=time(int(input("Enter hours ")),int(input("Enter minutes ")),int(input("Enter the second ")))

print("Time 2(24 hour format)")
obj2=time(int(input("Enter hours ")),int(input("Enter minutes ")),int(input("Enter the second ")))

obj1.display()
obj2.display()
print("Sum")
obj1+obj2
