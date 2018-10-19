from Tkinter import *
from Tkinter import messagebox

top=Tk()

top.geometry("100x100")

def hello():
	msg=messagebox.showinfo("Hello Python","Hello World")

B=Button(top,text="Hello")
B.bind('<Button-1>',hello)
B.place(x=40,y=40)
top.mainloop()
