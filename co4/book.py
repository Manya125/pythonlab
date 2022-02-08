class publisher:
	def __init__(self,p):
		self.pname=p
class book(publisher):
	def __init__(self,t,a,p):
		super().__init__(p)
		self.title=t
		self.author=a
		
class python(book):
	def __init__(self,p,a,t,prize,page):
		super().__init__(t,a,p)
		self.page=page
		self.prize=prize
	def display(self):
		print("Publisher:",self.pname)
		print("Title:",self.title)
		print("Author:",self.author)
		print("Number of pages:",self.page)
		print("Prize:",self.prize)
obj=python(input("Enter the Publisher "),input("Enter author "),input("Enter title "),int(input("Enter prize ")),int(input("Enter pages ")))
obj.display()
