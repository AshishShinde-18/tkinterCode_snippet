from tkinter import *
from tkinter import messagebox

root = Tk()


def val():
    s1 = e1.get()
    s2 = e2.get()

    if s1 == "  " or s2 == "  ":
        messagebox.showinfo(root, "Email Id Valid")
    elif s1 != s2:
        messagebox.showinfo(root, "Email Id not Match")
    else:
        messagebox.showinfo(root, "Email Id Valid")


l1 = Label(root, text="Email")
l2 = Label(root, text="Re-enterEmail")

e1 = Entry(root)
e2 = Entry(root)
btn = Button(root, text="Valid or invalid", command=val)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
btn.grid(row=2, column=0)

root.mainloop()
