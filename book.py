# This code snippet contains only GUI design part.

from tkinter import *

root = Tk()
root.title("BOOK")

l1 = Label(root, text="Book Name")
l2 = Label(root, text="Author Name")
l3 = Label(root, text="PRICE")
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
btn = Button(root, text="SUBMIT")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
btn.grid(columnspan=2)

root.mainloop()
