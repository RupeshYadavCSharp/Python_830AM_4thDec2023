class person:
    def data(self,age,name):
        self.__age=int(input("enter age"))
        self.__name=int(input("enter name"))

class dept:
    def dept(self,dno,dname):
        self.__dno=int(input("enter dno"))
        self.__dname=int(input("enter name"))
class hod(person,dept):
    def hod(self,exp):
        self.__exp=int(input("enter exp"))
class student(hod,person):
    def student(self,rno,sem,per):
        self.__rno=int(input("enter rno"))
        self.__sem=int(input("enter sem"))
        self.__per=int(input("enter per"))
class subject(student,hod):
    def subject(self,sub1,sub2,sub3):
        self.__sub1=int(input("enter sub1"))
        self.__sub2=int(input("enter sub2"))
        self.__sub3=int(input("enter sub3"))
if __name__=="__main__":
    p=subject()
    p.data()
    p.dept()
    p.hod()
    p.student()
    p.subject()



