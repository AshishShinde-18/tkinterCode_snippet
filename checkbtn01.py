from tkinter import *

root = Tk()
root.title("Checkbutton Demo")

C1 = IntVar()
C2 = IntVar()
C3 = IntVar()

c1 = Checkbutton(root, text="Audio", variable=C1, onvalue=1, offvalue=0, height=5, width=20)

c2 = Checkbutton(root, text="Video", variable=C2, onvalue=1, offvalue=0, height=5, width=20)

c3 = Checkbutton(root, text="Image", variable=C3, onvalue=1, offvalue=0, height=5, width=20)

c1.pack()
c2.pack()
c3.pack()
root.mainloop()
