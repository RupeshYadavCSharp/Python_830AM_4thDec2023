class rectangle:
    def read(self):
        self.length=int(input("enter length"))
        self.width=int(input("enter width"))
    def area(self):
        a=self.length*self.width
        print("area of rectangle is",a)
    def perimeter(self):
        p=(self.length+self.width)*2
        print("perimeter of rectangle is",p)
if __name__=="__main__":
    s=rectangle()
    s.read()
    s.area()
    s.perimeter()