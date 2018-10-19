from Tkinter import *

root=Tk()
frame=Frame(root)
frame.pack()

bottonframe=Frame(root)
bottonframe.pack(side=BOTTOM)

redbutton=Button(frame,text="RED",fg="red")
redbutton.pack(side=LEFT)

brownbutton=Button(frame,text="Blue",fg="brown")
brownbutton.pack(side=LEFT)

bluebutton=Button(frame,text="Brown",fg="blue")
bluebutton.pack(side=BOTTOM)

greenbutton=Button(frame,text="Brown",fg="green")
greenbutton.pack(side=BOTTOM)

blackbutton=Button(bottonframe,text="Black",fg="white")
blackbutton.pack(side=BOTTOM)

root.mainloop()


