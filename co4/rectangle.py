class rectangle:
	def __init__(self,l,b):
		self.__l=l
		self.__b=b
	def __lt__(self,other):
		if(self.__l * self.__b < other.__l * other.__b):
			return "Second Rectangle have Larger Area"
		else:
			return "First Rectangle have Larger Area"
obj1=rectangle(int(input("Enter the length of first rectangle ")),int(input("Enter the breadth of first rectangle ")))
obj2=rectangle(int(input("Enter the length of second rectangle ")),int(input("Enter the breadth of second rectangle ")))
print(obj1<obj2)
