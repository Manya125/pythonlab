class publisher:
   
    def __init__(self,name):
        self.name=name;
    def display(self):
        print("publisher :",self.name);
class  book(publisher):
    def __init__(self,name,title,author):
        publisher.__init__(self,name)
        self.title=title
        self.author=author
    def display(self):
        print("publisher :",self.name,",""title :",self.title,",""author :",self.author)
class  python(book):
    def __init__(self,name,title,author,price,page):
        book.__init__(self,name,title,author)
        self.price=price
        self.page=page
    def display(self):
        print("publisher :",self.name,",""title :",self.title,",""author :",self.author,",""price :",self.price,",""pages :",self.page)
a=publisher("Anu")
b=book("Anu","CPP","ram")
c=python("Anu","Py","X","100","10")
a.display()
b.display()
c.display()
