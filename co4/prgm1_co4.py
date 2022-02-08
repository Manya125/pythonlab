class Rectangle:
    def __init__(self,length,breadth,a,perimeter):
        self.length=length;
        self.breadth=breadth;
        self.a=a;
        self.perimeter=perimeter;
    def area(self):
        print("Area of the recatngle=",self.a);
        return self.a;
    def perimeter(self):
        print("perimeter=",self.perimeter);
   
print("Enter the length of the first rectangle");
l=int(input());
print("Enter the breadth of the first rectangle");
b=int(input());
print("Enter the length of the second rectangle");
l2=int(input());
print("Enter the breadth of the second rectangle");
b2=int(input());
ar=l*b;
pe=2*(l+b);
ar2=l2*b2;
pe2=2*(l2+b2);
s1=Rectangle(l,b,ar,pe);
s2=Rectangle(l2,b2,ar2,pe2);
e=s1.area();
x=s2.area();
if e>x:
    print(e,"Rectangle1 is big");
else:
    print(x,"Area of rectangle 2 is greater");


