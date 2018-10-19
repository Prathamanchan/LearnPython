import Tkinter
from Tkinter import *

root=Tk()

def call_back():
	print("Call_back")

def main():
	print("Main")

def exit():
	root.destroy()

w = Label(root,text="Press the button below if you want to Listen to the instructions.")
w.config(width=75)
w.config(font=("Helvetica", 30))
w.pack()


b1 = Button(root, text="Instructions",command=call_back,bg="lightgreen")
b1.config(font=("Times New Roman", 35,"bold"))
b1.pack()

x = Label(root,text="Press the button below to run the application (Then,press s for sound).")
x.config(width=75)
x.config(font=("Helvetica", 30))
x.pack()


b2 = Button(root, text="Run",command=main,bg="gold1")
b2.config(font=("Times New Roman", 35,"bold"))
b2.pack()



z = Label(root,text="Press ESCAPE and then the button below to exit.")
z.config(width=75)
z.config(font=("Helvetica", 30))
z.pack()


b3 = Button(root, text="Exit",command=exit,bg="salmon")
b3.config(font=("Raavi", 35,"bold"))
b3.pack()







root.mainloop()
