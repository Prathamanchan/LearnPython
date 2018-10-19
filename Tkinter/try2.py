import Tkinter as tk
from Tkinter import *

class Sampleapp:
	x=[20,40,60,80,100,120,140,160,180,200]
	

	def __init__(self):
		self.i=20
		
		
		self.root=Tk()
		self.root.geometry("400x600")
		self.f1=Frame(self.root)
		self.f1.pack(side=BOTTOM)

		self.f2=Frame(self.root)
		self.f2.pack(side=BOTTOM)

		self.f3=Frame(self.root)
		self.f3.pack(side=TOP)

		self.photo = PhotoImage(file="giphy.gif")
		self.w = Label(self.root, image=self.photo)
		self.w.photo = self.photo
		self.w.pack()

		self.f4=Frame(self.f3)
		self.f4.pack(side=LEFT)

		self.f5=Frame(self.f3)
		self.f5.pack(side=LEFT)

		self.B1=Button(self.f1,text="Send",command=self.send1)
		self.B1.pack(side=RIGHT)

		self.B2=Button(self.f2,text="Send",command=self.send2)
		self.B2.pack(side=RIGHT)

		self.E1=Entry(self.f1,bd=5,width=50)
		self.E1.pack(side=LEFT)

		self.E2=Entry(self.f2,bd=5,width=50)
		self.E2.pack(side=LEFT)



	def send2(self):
		self.i=self.i+1
		s2=self.E2.get()
		self.E2.delete(0, END)
		print(s2)
		self.l2=Label(self.f4,text=s2,font=("Helvetica", 16),bg="blue",fg="white",justify=LEFT)
		#self.l2.place(x=20,y=20,height=20,width=20)  #self.x[self.i]
		self.l2.pack(fill=X,padx=10,pady=10)
		
	
	def send1(self):
		self.i=self.i+0
		s1=self.E1.get()
		self.E1.delete(0, END)
		print(s1)
		self.l3=Label(self.f5,text=s1,bg="green",font=("Helvetica", 16),fg="white",justify=RIGHT)
		#self.l3.place(x=20,y=10)
		self.l3.pack(fill=X,padx=10,pady=self.i)
		self.i=10
		

w=Sampleapp()
w=mainloop()


