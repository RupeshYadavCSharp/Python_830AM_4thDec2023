class Calculator:
    def read(self,n1,n2)->float:
        self.num1=n1
        self.num2=n2
    def add(self)->int:
        a=self.num1+self.num2
        return a
    def sub(self)->int:
        s=self.num1-self.num2
        return s
if __name__=="__main__":
    n1=int(input("enter first number"))
    n2=int(input("enter second number"))
    calulator=Calculator()
    calulator.read(n1,n2)
    a=calulator.add()
    s=calulator.sub()
    print("addition is",a)
    print("subtraction is",s)
