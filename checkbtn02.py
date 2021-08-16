from tkinter import *

root = Tk()
root.title("Checkbutton Demo")

CheckVar1 = IntVar()
CheckVar2 = IntVar()

c1 = Checkbutton(root, text="music", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)
c2 = Checkbutton(root, text="video", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)

c1.pack()
c2.pack()
root.mainloop()
