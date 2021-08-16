# This code snippet contains only GUI design part.

from tkinter import *

root = Tk()
root.title("Book Entry")

lbl1 = Label(root, text="Book Name")
lbl2 = Label(root, text="Author Name")
lbl3 = Label(root, text="Date issue")
lbl4 = Label(root, text="Date Return")

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)
lbl3.grid(row=2, column=0)
lbl4.grid(row=3, column=0)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

btn = Button(root, text="SUBMIT")
btn.grid(columnspan=4)

root.mainloop()
