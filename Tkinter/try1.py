import Tkinter
from Tkinter import *

top=Tk()
top.geometry("500x500")


def send2():
	s2=E2.get()
	print(s2)


def send1():
	s1=E1.get()
	print(s1)

f1=Frame(top)
f1.pack(side=BOTTOM)

f2=Frame(top)
f2.pack(side=BOTTOM)

f3=Frame(top)
f3.pack(side=TOP)

f4=Frame(f3)
f4.pack(side=LEFT)

f5=Frame(f3)
f5.pack(side=LEFT)


B1=Button(f1,text="Send",command=send1)
B1.pack(side=RIGHT)

B2=Button(f2,text="Send",command=send2)
B2.pack(side=RIGHT)

E1=Entry(f1,bd=5,width=50)
E1.pack(side=LEFT)

E2=Entry(f2,bd=5,width=50)
E2.pack(side=LEFT)

top.mainloop()


