from pack_rectangle.rectanglee import *
def main():
    l=float(input("enter l="))
    b=float(input("enter b="))
    a=area(l,b)
    p=parimeter(l,b)
    print("Area of rectangle is",round(a,2))
    print("Perimeter of rectangle is",round(p,2))
main()