from tkinter import *

root = Tk()
root.title("CALCULATOR")


def add():
    a = int(e1.get())
    b = int(e2.get())
    c = a + b
    var.set(c)


def sub():
    a = int(e1.get())
    b = int(e2.get())
    c = a - b
    var.set(c)


def mult():
    a = int(e1.get())
    b = int(e2.get())
    c = a * b
    var.set(c)


def div():
    a = int(e1.get())
    b = int(e2.get())
    c = a / b
    var.set(c)


lbl1 = Label(root, text="N1")
lbl2 = Label(root, text="N2")
lbl3 = Label(root, text="Result")
var = StringVar()
lbl4 = Label(root, text="res", textvariable=var, bg="grey", width="20")

e1 = Entry(root)
e2 = Entry(root)

btn1 = Button(root, text="ADD", command=add)
btn2 = Button(root, text="SUB", command=sub)
btn3 = Button(root, text="MULT", command=mult)
btn4 = Button(root, text="DIV", command=div)

lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)
lbl3.grid(row=2, column=0)
lbl4.grid(row=2, column=1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn4.grid(row=3, column=3)

root.mainloop()
