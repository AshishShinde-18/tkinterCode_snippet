from tkinter import *
from tkinter import messagebox

root = Tk()


def val():
    t1 = e1.get()
    t2 = e2.get()

    if t1 == "  " or t2 == "  ":
        messagebox.showinfo(root, "Email Id InValid")
    elif t1 != t2:
        messagebox.showinfo(root, "Email Id InValid")
    else:
        messagebox.showinfo(root, "Email Id Valid")


l1 = Label(root, text="Email ID")
l2 = Label(root, text="Re-enter Email ID")

e1 = Entry(root)
e2 = Entry(root)

b1 = Button(text="Invalid or Valid", command=val)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1.grid(row=2, columnspan=2)
root.mainloop()
