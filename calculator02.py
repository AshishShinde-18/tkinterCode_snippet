from tkinter import *

root = Tk()
root.title("Calculator")


def add():
    A = int(e1.get())
    B = int(e2.get())
    C = A + B
    var.set(C)


def sub():
    A = int(e1.get())
    B = int(e2.get())
    C = A - B
    var.set(C)


def mult():
    A = int(e1.get())
    B = int(e2.get())
    C = A * B
    var.set(C)


def div():
    A = int(e1.get())
    B = int(e2.get())
    C = A / B
    var.set(C)


l1 = Label(root, text="A")
l2 = Label(root, text="B")
l4 = Label(root, text="result", textvariable="var")
l4.grid(row=4, column=1)
var = StringVar()
l3 = Label(root, textvariable=var, width="5", bg="white")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=4, column=0)

e1 = Entry(root)
e2 = Entry(root)

b1 = Button(root, text="ADD", command=add)
b2 = Button(root, text="SUB", command=sub)
b3 = Button(root, text="MULT", command=mult)
b4 = Button(root, text="DIV", command=div)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=3, column=0)
b4.grid(row=3, column=1)
root.mainloop()
