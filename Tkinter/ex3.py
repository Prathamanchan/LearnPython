from Tkinter import *
root=Tk()
b=0

for r in range(6):
	for c in range(6):
		b=b+1
		button=Button(root,text=str(b),borderwidth=1).grid(row=r,column=c)


root.mainloop()
