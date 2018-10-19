from Tkinter import *
import Tkinter

top=Tk()
checkvar1=IntVar()
checkvar2=IntVar()
t="Music On"
c1=Checkbutton(top,text=t,variable=checkvar1,onvalue=1,offvalue=0,height=5,width=20)
c2=Checkbutton(top,text="video",variable=checkvar2,onvalue=1,offvalue=0,height=5,width=20)

def chkstate():
	print(checkvar1.get())
	print(checkvar2.get())

B=Button(top,text="OK",command=chkstate)
c1.pack()
c2.pack()
B.pack()
top.mainloop()
