# def show(name,sub1,sub2,sub3):
#     print(name,"interested in")
#     print(sub1,sub2,sub3)
# def main():
#     show("Ramesh","science","History","Maths","Geography")
#
# main()
# def show(name,*subject):
#     print(name,"is interested in")
#     print(subject)
# def main():
#     show("Monali","ML","Python","Sql","Advanceexcel","statistics")
#
# main()

def show(name,*games):
    print(name,"is keen in")
    print(games)
def main():
    show('Monali',"CRICKET","BASEBALL","BADMINTON","HOCKEY")
main()