from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Validation")


def validate():
    str_user = e1.get()
    str_password = e2.get()

    if str_user == "abc@gmail.com" and str_password == "9956764565":
        messagebox.showinfo(root, "password and Id correct")
    else:
        messagebox.showinfo(root, "incorrect")


l1name = Label(root, text="User Name")
l2pwd = Label(root, text="Password")

btn_login = Button(root, text="Login", command=validate)

e1 = Entry(root)
e2 = Entry(root)

l1name.grid(row=0, column=0)
l2pwd.grid(row=1, column=0)

btn_login.grid(row=2, column=1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

root.mainloop()
