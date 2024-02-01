class Person:
    def readper(self):
        self.__age=int(input("enter age"))
        self.__name=str(input("enter name"))

    def showper(self):
        print("age is",self.__age)
        print("name is",self.__name)
class Student(Person):
    def readstud1(self):
        self.__rno=int(input("enter roll no"))
        self.__sem=int(input("enter sem"))
        self.__per=int(input("enter percentile"))

    def showstud(self):
        print("roll no is",self.__rno)
        print("sem is",self.__sem)
        print("percentile is",self.__per)
class Faculty(Person):
    def readfaculty(self):
        self.__exp=int(input("enter experience"))
        self.__sal=float(input("enter salary"))
    def showfaculty(self):
        print("experience is",self.__exp)
        print("salary is",self.__sal)
if __name__=="__main__":
    choice=int(input("1.student 2.faculty"))
if(choice==1):
    student=Student()
    student.readper()
    student.showper()
    student.readstud1()
    student.showstud()
elif(choice==2):
    faculty=Faculty()
    faculty.readper()
    faculty.showper()
    faculty.showfaculty()
    faculty.readfaculty()
