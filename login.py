from tkinter import *
from tkinter import messagebox
import mysql.connector
from signup import SignUp
from PIL import ImageTk
from libmanage import lib

class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("Log In To Library")
        self.window.geometry("626x581")

        self.bg_img = ImageTk.PhotoImage(file="loginpage.jpg")
        background = Label(self.window,image=self.bg_img).place(x=0,y=0)

        self.email_label = Label(self.window,text="Username", font=("helvetica",20,"bold")).place(x=40,y=110)
        self.email_entry = Entry(self.window,font=("times new roman",15,"bold"))
        self.email_entry.place(x=270, y=110, width=300,height=40)

        self.password_label = Label(self.window,text="Password", font=("helvetica",20,"bold")).place(x=40,y=190)
        self.password_entry = Entry(self.window,font=("times new roman",15,"bold"),show="*")
        self.password_entry.place(x=270, y=190, width=300,height=40)

        #================Buttons===================
        self.login_button = Button(self.window,text="Log In",command=self.login_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="brown").place(x=150,y=350,width=300)

        self.create_button = Button(self.window,text="Create New Account",command=self.redirect_window1,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="brown").place(x=175,y=420,width=250)


    def login_func(self):
        if self.email_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)
        else:
            try:
                conn=mysql.connector.connect(host='', user='', password='', database='')
                cur = conn.cursor()
                cur.execute("select * from login where username=%s and password=%s",(self.email_entry.get(),self.password_entry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!","Invalid USERNAME & PASSWORD",parent=self.window)
                else:
                    messagebox.showinfo("Success","Logged In Successfully",parent=self.window)
                    # Clear all the entries
                    self.reset_fields()
                    conn.close()
                    self.redirect_window2()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window) 
            

    def redirect_window1(self):
        self.window.destroy()
        root = Tk()
        obj = SignUp(root)
        root.mainloop()

    def redirect_window2(self):
        self.window.destroy()
        root = Tk()
        obj = lib(root)
        root.mainloop()


    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)

if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()



