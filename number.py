from tkinter import *
from tkinter import messagebox

root = Tk()


def ok():
    s = int(e1.get())

    if s < 0:
        messagebox.showinfo(root, "no is negative")
    else:
        messagebox.showinfo(root, "no is positive")


l1 = Label(root, text="No")
e1 = Entry(root)
b1 = Button(root, text="B", command=ok)
l1.grid(row=0, column=0)
b1.grid(row=1, column=0)
e1.grid(row=0, column=1)

root.mainloop()
