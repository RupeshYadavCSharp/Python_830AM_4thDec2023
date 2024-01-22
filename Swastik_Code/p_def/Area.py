def rectangle(l,w):
    area=l*w
    parameter=((l+w)*2)
    return area,parameter
def main():
    l=int(input("enter length"))
    w=int(input("enter width"))
    area,parameter=rectangle(l,w)
    print("area of rectangle is ",area)
    print("parameter of rectangle is ",parameter)
main()