from tkinter import *
from random import randint
class Window:
    def __init__(self):
        self.objkt=Tk()
        self.objkt.wm_geometry("{}x{}+0+0".format(self.objkt.winfo_screenwidth(), self.objkt.winfo_screenheight()))
        self.objkt.wm_title("SWASTIK")
        self.img=PhotoImage(file="C:\\Users\\Lenovo\\Downloads\\demo.png")
        self.objkt.iconphoto(False,self.img)
        color="%05x" %randint(0, 0xFFFFFF)
        self.objkt.config(background="#40A2E3")
        self.objkt.after(1000,self.objkt)


        self.objkt.mainloop()
if __name__=="__main__":
    win=Window()