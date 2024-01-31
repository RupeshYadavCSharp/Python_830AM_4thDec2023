class Rectangle:
    def __init__(self,length,breadth)->None:
        self.__length=length
        self.__breadth=breadth
    def area(self):
        a=self.__length*self.__breadth
        print("area is",a)
    def perimeter(self):
        p=2*(self.__length+self.__breadth)
        print("perimeter is",p)
if __name__=="__main__":
    length=int(input("enter length"))
    breadth=int(input("enter breadth"))
    r=Rectangle(length,breadth)
    r.area()
    r.perimeter()