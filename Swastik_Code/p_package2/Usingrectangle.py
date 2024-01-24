from Swastik_Code.p_package1.Rectangle import *

def main():
    l = float(input("enter length"))
    w = float(input("enter width"))
    a=area(l,w)
    p=paramter(l, w)
    print("area is",a)
    print("perimeter is",p)
main()