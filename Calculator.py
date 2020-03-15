from Tkinter import *
from ttk import Button, Style

class Calculator(Frame):

    def __init__(self,parent):

        Frame.__init__(self,parent)
        self.parent= parent
        self.initUI()


    def initUI(self):

        Style().configure("TButton",padding=15,width=8,font="serif 10")

        self.screen_var = StringVar()
        self.result_str= " "
        self.result = Label(self, textvariable = self.screen_var)
        self.result.pack()


        self.cls = Button(text="Cls",command=self.clsfun)
        self.back = Button(text="Back",command =self.backfun)
        self.empty = Button(text="Empty")
        self.close = Button(text="Close",command=self.closefun)


        self.but7=Button(text="7",command = self.but7fun)
        self.but8 = Button(text="8",command=self.but8fun)
        self.but9 = Button(text="9",command=self.but8fun)
        self.divide = Button(text="/",command= self.dividefun)

        self.but4 = Button(text="4",command=self.but4fun)
        self.but5 = Button(text="5",command=self.but5fun)
        self.but6 = Button(text="6",command=self.but6fun)
        self.multiply = Button(text="*",command=self.multiplyfun)

        self.but1 = Button(text="1",command=self.but1fun)
        self.but2 = Button(text="2",command=self.but2fun)
        self.but3 = Button(text="3",command=self.but3fun)
        self.sub = Button(text="-",command=self.subfun)

        self.but0 = Button(text="0",command=self.but0fun)
        self.dot = Button(text=".")
        self.equal = Button(text="=",command=self.equalfun)
        self.sum = Button(text="+",command=self.sumfun)

        self.packUI()


    def packUI(self):

        self.Frame1 = Frame(self)
        self.Frame1.pack()


        self.cls.pack(in_ = self.Frame1,side =LEFT)
        self.back.pack(in_=self.Frame1, side =LEFT)
        self.empty.pack(in_=self.Frame1, side =LEFT)
        self.close.pack(in_=self.Frame1,side=LEFT)

        self.Frame2=Frame(self)
        self.Frame2.pack()
        self.but7.pack(in_=self.Frame2,side=LEFT)
        self.but8.pack(in_=self.Frame2,side=LEFT)
        self.but9.pack(in_=self.Frame2,side=LEFT)
        self.divide.pack(in_=self.Frame2,side=LEFT)

        self.Frame3=Frame(self)
        self.Frame3.pack()

        self.but4.pack(in_=self.Frame3,side=LEFT)
        self.but5.pack(in_=self.Frame3, side=LEFT)
        self.but6.pack(in_=self.Frame3, side=LEFT)
        self.multiply.pack(in_=self.Frame3, side=LEFT)

        self.Frame4=Frame(self)
        self.Frame4.pack()
        self.but1.pack(in_=self.Frame4, side=LEFT)
        self.but2.pack(in_=self.Frame4, side=LEFT)
        self.but3.pack(in_=self.Frame4, side=LEFT)
        self.sub.pack(in_=self.Frame4, side=LEFT)

        self.Frame5=Frame(self)
        self.Frame5.pack()
        self.but0.pack(in_=self.Frame5, side = LEFT)
        self.dot.pack(in_=self.Frame5,side=LEFT)
        self.equal.pack(in_=self.Frame5,side=LEFT)
        self.sum.pack(in_=self.Frame5,side=LEFT)



        self.pack()


    def but7fun(self):
        self.result_str += "7"
        self.screen_var.set(self.result_str)

    def but8fun(self):
        self.result_str += "8"
        self.screen_var.set(self.result_str)

    def but9fun(self):
        self.result_str += "9"
        self.screen_var.set(self.result_str)

    def but4fun(self):
        self.result_str += "4"
        self.screen_var.set(self.result_str)

    def but5fun(self):
        self.result_str += "5"
        self.screen_var.set(self.result_str)

    def but6fun(self):
        self.result_str += "6"
        self.screen_var.set(self.result_str)

    def but1fun(self):
        self.result_str += "1"
        self.screen_var.set(self.result_str)

    def but2fun(self):
        self.result_str += "2"
        self.screen_var.set(self.result_str)

    def but3fun(self):
        self.result_str += "3"
        self.screen_var.set(self.result_str)
    def but0fun(self):
        self.result_str += "0"
        self.screen_var.set(self.result_str)

    def sumfun(self):
        self.result_str += "+"
        self.screen_var.set(self.result_str)

    def subfun(self):
        self.result_str +="-"
        self.screen_var.set(self.result_str)


    def multiplyfun(self):
        self.result_str += "*"
        self.screen_var.set(self.result_str)


    def dividefun(self):
        self.result_str += "/"
        self.screen_var.set(self.result_str)


    def equalfun(self):
        self.result_str = str(eval(self.result_str))
        self.screen_var.set(self.result_str)


    def closefun(self):
        self.parent.destroy()

    def clsfun(self):
        self.result_str = ""
        self.screen_var.set(self.result_str)

    def backfun(self):
        self.result_str = self.result_str[:-1]
        self.screen_var.set(self.result_str)

def main():

    root=Tk()

    x=Calculator(root)
    root.geometry("600x600")
    root.mainloop()

main()