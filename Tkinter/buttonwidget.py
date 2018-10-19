from Tkinter import *
top=Tk()
top.title("Canvas")
c=Canvas(top,bg="blue",height=250,width=300)
coord=10,50,240,210
arc=c.create_arc(coord,start=0,extent=150,fill="yellow")
c.pack()
line=c.create_line(10,10,200,200,fill="white")
txt=c.create_text(100,200,text="Hello",font=("Arial",20),fill="yellow")
c.pack()
c.mainloop()
