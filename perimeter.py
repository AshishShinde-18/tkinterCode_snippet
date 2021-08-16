from tkinter import *

root = Tk()
root.title("PERIMETER")


def tri():
    a = int(e1.get())
    b = int(e2.get())
    c = int(e3.get())
    P = a + b + c
    var.set(P)


def Atri():
    a = int(e1.get())
    b = int(e2.get())
    P = 1 / 2 * a * b
    var.set(P)


def etri():
    a = int(e1.get())

    PE = 3 * a
    var.set(PE)


def Aetri():
    a = int(e1.get())

    PE = 1.732 / 4 * a * a
    var.set(PE)


def square():
    a = int(e1.get())
    S = 4 * a
    var.set(S)


def Asquare():
    a = int(e1.get())
    S = a * a
    var.set(S)


def rect():
    a = int(e1.get())
    b = int(e2.get())
    R = 2*(a + b)
    var.set(R)


def Arect():
    a = int(e1.get())
    b = int(e2.get())
    R = a * b
    var.set(R)


def trapezium():
    a = int(e1.get())
    b = int(e2.get())
    c = int(e3.get())
    d = int(e4.get())
    T = a + b + c + d
    var.set(T)


def Atrapezium():
    a = int(e1.get())
    b = int(e2.get())
    c = int(e3.get())
    d = int(e4.get())
    T = 1 / 2 * (a + b) * c
    var.set(T)


def rhombus():
    a = int(e1.get())
    RH = 4 * a
    var.set(RH)


def Arhombus():
    a = int(e1.get())
    b = int(e2.get())
    RH = 1 / 2 * (a * b)
    var.set(RH)


def rtri():
    a = int(e1.get())
    b = int(e2.get())
    c = int(e3.get())
    A = a + b + c
    var.set(A)


def Acircle():
    a = int(e1.get())
    C = 3.14 * a * a
    var.set(C)


def pcircle():
    a = int(e1.get())
    C = 2 * 3.14 * a
    var.set(C)


def parallelogram():
    a = int(e1.get())
    b = int(e2.get())
    PL = a + b
    var.set(PL)


def Aparallelogram():
    a = int(e1.get())
    b = int(e2.get())
    PL = a / b
    var.set(PL)


lbl1 = Label(root, text="a")
lbl2 = Label(root, text="b")
lbl3 = Label(root, text="c")
lbl4 = Label(root, text="d")
lbl5 = Label(root, text="AREA")
lbl6 = Label(root, text="PERIMETER")

lbl1.grid(row=0, column=0)
lbl2.grid(row=0, column=2)
lbl3.grid(row=1, column=0)
lbl4.grid(row=1, column=2)
lbl5.grid(row=3, column=0)
lbl6.grid(row=3, column=3)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=0, column=3)
e3.grid(row=1, column=1)
e4.grid(row=1, column=3)

btn1 = Button(root, text="TRIANGLE", command=tri)
btn2 = Button(root, text="E.TRIANGLE", command=etri)
btn3 = Button(root, text="SQUARE", command=square)
btn4 = Button(root, text="RECTANGLE", command=rect)
btn5 = Button(root, text="PARALLELOGRAM", command=parallelogram)
btn6 = Button(root, text="TRAPAZIUM", command=trapezium)
btn7 = Button(root, text="RHOMBUS", command=rhombus)
btn8 = Button(root, text="R.TRIANGLE", command=rtri)
btn9 = Button(root, text="AREA TRIANGLE", command=Atri)
btn10 = Button(root, text="AREA EQ.TRIANGLE", command=Aetri)
btn11 = Button(root, text="AREA SQUARE", command=Asquare)
btn12 = Button(root, text="AREA RECTANGLE", command=Arect)
btn13 = Button(root, text="AREA PARALLELOGRAM", command=Aparallelogram)
btn14 = Button(root, text="AREA TRAPEZIUM", command=Atrapezium)
btn15 = Button(root, text="AREA RHOHMBUS", command=Arhombus)
btn16 = Button(root, text="AREA CIRCLE", command=Acircle)
btn17 = Button(root, text="Perimeter C", command=pcircle)

btn1.grid(row=4, column=0)
btn2.grid(row=5, column=0)
btn3.grid(row=6, column=0)
btn4.grid(row=7, column=0)
btn5.grid(row=8, column=0)
btn6.grid(row=9, column=0)
btn7.grid(row=10, column=0)
btn8.grid(row=11, column=0)
btn9.grid(row=4, column=2)
btn10.grid(row=5, column=2)
btn11.grid(row=6, column=2)
btn12.grid(row=7, column=2)
btn13.grid(row=8, column=2)
btn14.grid(row=9, column=2)
btn15.grid(row=10, column=2)
btn16.grid(row=11, column=2)
btn17.grid(row=12, column=2)

var = StringVar()
lbl7 = Label(root, text="Result", textvariable=var, width=10, bg="white")
lbl7.grid(row=13, column=0)
root.mainloop()