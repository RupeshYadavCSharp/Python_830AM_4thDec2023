class Office:
    def set(self,sal,exp):
        self.sal=sal
        self.exp=exp
    def getbonus(self)->float:
        a=self.exp
        b=self.sal
        if(a>=1 and a<=3):
            bonus=(10/100)*b
        elif(a>=3 and a<=8):
            bonus=(15/100)*b
        elif(a>8):
            bonus=(30/100)*b
        c=bonus

        return c


    def gettotalsal(self)->float:
        ts=c+self.sal
        return ts


if __name__=="__main__":
    sal=int(input("enter salary"))
    exp=int(input("enter experience"))
    office=Office()
    office.set(sal,exp)
    c=office.getbonus()
    ts=office.gettotalsal()
    print("bonus is",c)
    print("total salary is",ts)
