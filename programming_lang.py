# This code snippet contains only GUI design part.

from tkinter import *

root = Tk()
root.title("Languages")

l1 = Label(root, text="LANGUAGES")
l2 = Label(root, text="Java")
l3 = Label(root, text="C")
l4 = Label(root, text="C++")
l5 = Label(root, text="Python")
l6 = Label(root, text="PHP")
l7 = Label(root, text="Asp.NET")
l8 = Label(root, text="Ruby")
l9 = Label(root, text="Percentage")

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)
l5.grid(row=4, column=0)
l6.grid(row=5, column=0)
l7.grid(row=6, column=0)
l8.grid(row=7, column=0)
l9.grid(row=0, column=1)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)

root.mainloop()
