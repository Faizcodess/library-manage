from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from libmanage import lib

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("626x581")
        self.window.config(bg = "white")

        self.bg_img = ImageTk.PhotoImage(file="signpage.jpg")
        background = Label(self.window,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)

        title1 = Label(self.window, text="Sign Up", font=("times new roman",25,"bold"),bg="orchid3").place(x=230, y=90)

        name = Label(self.window, text="Name", font=("helvetica",15,"bold")).place(x=140, y=170)
        self.namevar=StringVar()
        self.name_txt = Entry(self.window,font=("arial"),textvariable=self.namevar)
        self.name_txt.place(x=270, y=170, width=200,height=30)

        username = Label(self.window, text="Username", font=("helvetica",15,"bold")).place(x=140, y=280)
        self.unamevar=StringVar()
        self.uname_txt = Entry(self.window,font=("arial"),textvariable=self.unamevar)
        self.uname_txt.place(x=270, y=280, width=200,height=30)

        password =  Label(self.window, text="Password", font=("helvetica",15,"bold")).place(x=140, y=390)
        self.passvar=StringVar()
        self.password_txt = Entry(self.window,font=("arial"),textvariable=self.passvar)
        self.password_txt.place(x=270, y=390, width=200,height=30)

        self.subbtn=Button(self.window,font=("times new roman",25,"bold"),command=self.signup_func,text="Create",bd=0,cursor="hand2",bg="orchid3").place(x=230,y=470)

    def signup_func(self):
        if self.namevar.get()=="" or self.unamevar.get()=="" or self.passvar.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        else:
            conn=mysql.connector.connect(host='localhost', user='root', password='Leg12345', database='librarymanagement',auth_plugin='mysql_native_password')
            cur = conn.cursor()
            cur.execute("select *from login where username=%s",([self.unamevar.get()]))
            row=cur.fetchone()

            # Check if th entered email id is already exists or not.
            if row!=None:
                messagebox.showerror("Error!","The email id is already exists, please try again with another email id",parent=self.window)
            else:
                query="insert into login values(%s,%s,%s)"
                value=(self.namevar.get(),self.unamevar.get(),self.passvar.get())
                cur.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                self.reset_fields()
                self.redirect_window()

    def reset_fields(self):
        self.name_txt.delete(0, END)
        self.uname_txt.delete(0, END)
        self.password_txt.delete(0, END)

    def redirect_window(self):
        self.window.destroy()
        root = Tk()
        obj = lib(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()