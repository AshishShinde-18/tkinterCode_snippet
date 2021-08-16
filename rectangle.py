from tkinter import *

root = Tk()


def rectangle():
    l = int(e1.get())
    b = int(e2.get())
    A = l * b
    var.set(A)


lbl1 = Label(root, text="Length")
lbl2 = Label(root, text="Breadth")
lbl3 = Label(root, text="Result", textvariable="var")

var = StringVar()
lbl4 = Label(root, text="res", textvariable=var, width="10", bg="white")
lbl4.grid(row=2, column=1)

e1 = Entry(root)
e2 = Entry(root)

lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)
lbl3.grid(row=2, column=0)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

btn = Button(root, text="Rectangle", command=rectangle)
btn.grid(row=3, column=1)

root.mainloop()
