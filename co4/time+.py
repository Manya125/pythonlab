class Time:
    def __init__(self,hour,minute,sec):
        self.hour = hour
        self.minute = minute
        self.sec = sec

    def __add__(self,other):
        return self.hour+other.hour,self.minute+other.minute,self.sec+other.sec

hr1,min1,sec1 = int(input("enter hr 1")),int(input("enter minute 1")),int(input("enter sec 1"))
hr2,min2,sec2 = int(input("enter hr 2")),int(input("enter minute 2")),int(input("enter sec 2"))
time1 = Time(hr1,min1,sec1)
time2 = Time(hr2,min2,sec2)

time3 = time1 + time2

print(time3)
