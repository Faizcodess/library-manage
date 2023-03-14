from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from count import Count
import datetime
import tkinter
  
class lib:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768")
        self.root.title("Libraray Management App")

        #variables
        self.member=StringVar()
        self.IDno=StringVar()
        self.fname=StringVar()
        self.lname=StringVar()
        self.phoneno=StringVar()
        self.address=StringVar()
        self.sem=StringVar()
        self.bookid=StringVar()
        self.booktitle=StringVar()
        self.aname=StringVar()
        self.bdate=StringVar()
        self.ddate=StringVar()
        self.fine=StringVar()
        self.price=StringVar()

        #header
        headtitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="seagreen",fg="black",bd=15,relief=RIDGE,font="verdana 45 bold",padx=2,pady=4)
        headtitle.pack(side=TOP,fill=X)

        #frame1
        frame1=Frame(self.root,bd=7,relief=RIDGE,padx=5,bg="seagreen")
        frame1.place(x=0,y=110,width=1360,height=380)

        #leftdataframe
        DataFrameLeft=LabelFrame(frame1,text="LIBRARY MEMBERSHIP INFO",bg="seagreen",fg="black",bd=7,relief=RIDGE,font="verdana 14 bold",padx=2,pady=4)
        DataFrameLeft.place(x=0,y=5,width=750,height=280)

        lblmem1=Label(DataFrameLeft,text="Member Type",font="verdana 10 bold",padx=2,pady=5,bg="seagreen")
        lblmem1.grid(row=0,column=0,sticky=W)

        commem1=ttk.Combobox(DataFrameLeft,font="verdana 10 bold",width=27,state="readonly",textvariable=self.member)
        commem1["value"]=("Admin","Student")
        commem1.grid(row=0,column=1)

        lblid=Label(DataFrameLeft,text="ID Number",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lblid.grid(row=1,column=0,sticky=W)
        txtid=Entry(DataFrameLeft,font="verdana 10 bold",width=29,textvariable=self.IDno)
        txtid.grid(row=1,column=1)

        lblfname=Label(DataFrameLeft,text="First Name",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lblfname.grid(row=2,column=0,sticky=W)
        self.txtfname=Entry(DataFrameLeft,font="verdana 10 bold",width=29,textvariable=self.fname)
        self.txtfname.grid(row=2,column=1)

        lbllname=Label(DataFrameLeft,text="Last Name",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lbllname.grid(row=3,column=0,sticky=W)
        txtlname=Entry(DataFrameLeft,font="verdana 10 bold",width=29,textvariable=self.lname)
        txtlname.grid(row=3,column=1)

        lbladd=Label(DataFrameLeft,text="Address",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lbladd.grid(row=4,column=0,sticky=W)
        txtadd=Entry(DataFrameLeft,font="verdana 10 bold",width=29,textvariable=self.address)
        txtadd.grid(row=4,column=1)

        lblno=Label(DataFrameLeft,text="Phone Number",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lblno.grid(row=5,column=0,sticky=W)
        txtno=Entry(DataFrameLeft,font="verdana 10 bold",width=29,textvariable=self.phoneno)
        txtno.grid(row=5,column=1)

        lblsem=Label(DataFrameLeft,text="Sem",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lblsem.grid(row=6,column=0,sticky=W)
        txtsem=Entry(DataFrameLeft,font="verdana 10 bold",width=29,textvariable=self.sem)
        txtsem.grid(row=6,column=1)
         
        lblbid=Label(DataFrameLeft,text="Book ID",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lblbid.grid(row=0,column=2,sticky=W)
        txtbid=Entry(DataFrameLeft,font="verdana 10 bold",width=26,textvariable=self.bookid)
        txtbid.grid(row=0,column=3)

        lblbtit=Label(DataFrameLeft,text="Book Title",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lblbtit.grid(row=1,column=2,sticky=W)
        txtbtit=Entry(DataFrameLeft,font="verdana 10 bold",width=26,textvariable=self.booktitle)
        txtbtit.grid(row=1,column=3)

        lblaname=Label(DataFrameLeft,text="Author Name",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lblaname.grid(row=2,column=2,sticky=W)
        txtaname=Entry(DataFrameLeft,font="verdana 10 bold",width=26,textvariable=self.aname)
        txtaname.grid(row=2,column=3)

        lbldb=Label(DataFrameLeft,text="Date Borrowed",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lbldb.grid(row=3,column=2,sticky=W)
        txtdb=Entry(DataFrameLeft,font="verdana 10 bold",width=26,textvariable=self.bdate)
        txtdb.grid(row=3,column=3)

        lbldd=Label(DataFrameLeft,text="Due Date",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lbldd.grid(row=4,column=2,sticky=W)
        txtdd=Entry(DataFrameLeft,font="verdana 10 bold",width=26,textvariable=self.ddate)
        txtdd.grid(row=4,column=3)

        lblfine=Label(DataFrameLeft,text="Over Due Fine",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lblfine.grid(row=5,column=2,sticky=W)
        txtfine=Entry(DataFrameLeft,font="verdana 10 bold",width=26,textvariable=self.fine)
        txtfine.grid(row=5,column=3)

        lblp=Label(DataFrameLeft,text="Price",bg="seagreen",fg="black",font="verdana 10 bold",padx=2,pady=4)
        lblp.grid(row=6,column=2,sticky=W)
        txtp=Entry(DataFrameLeft,font="verdana 10 bold",width=26,textvariable=self.price)
        txtp.grid(row=6,column=3)

        #rightdataframe
        DataFrameRight=LabelFrame(frame1,text="BOOK DETAILS",bg="seagreen",fg="black",bd=7,relief=RIDGE,font="verdana 14 bold")
        DataFrameRight.place(x=760,y=5,width=565,height=280)

        self.txtBox=Text(DataFrameRight,font="verdana 14 bold",width=22,height=10,padx=2,pady=5)
        self.txtBox.grid(row=0,column=2)

        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky=NS)

        listBook=['Learn Python The Hard Way','Python Programming','Into The Machine Learning',"Fluent Python","Think Python","Python Cookbook","Deep Learning","Machine Learning For Hackers","Database Management System","Database System Concepts","Artificial Intelligence"]

        def selectbook(event="e"):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if x=="Learn Python The Hard Way":
                self.bookid.set("10")
                self.booktitle.set("Learn Python The Hard Way")
                self.aname.set("Guiddo Van Rossum")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:999")

            elif x=="Python Programming":
                self.bookid.set("20")
                self.booktitle.set("Python Programming")
                self.aname.set("Mark Lutz")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:899")

            elif x=="Into The Machine Learning":
                self.bookid.set("30")
                self.booktitle.set("Into The Machine Learning")
                self.aname.set("Andriy Burkov")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:1299")

            elif x=="Fluent Python":
                self.bookid.set("40")
                self.booktitle.set("Fluent Python")
                self.aname.set("Luciano Ramalho")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:899")

            elif x=="Think Python":
                self.bookid.set("50")
                self.booktitle.set("Think Python")
                self.aname.set("Allen B Downey")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:799")

            elif x=="Python Cookbook":
                self.bookid.set("60")
                self.booktitle.set("Python Cookbook")
                self.aname.set("Allex Martelli")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:1199")

            elif x=="Deep Learning":
                self.bookid.set("70")
                self.booktitle.set("Deep Learning")
                self.aname.set("Yoshua Bengio")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:999")

            elif x=="Machine Learning For Hackers":
                self.bookid.set("80")
                self.booktitle.set("Machine Learning For Hackers")
                self.aname.set("John Myles White")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:1699")

            elif x=="Database Management System":
                self.bookid.set("90")
                self.booktitle.set("Database Management System")
                self.aname.set("Raghu Ramakrishnan")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:1399")

            elif x=="Database System Concepts":
                self.bookid.set("100")
                self.booktitle.set("Database Management Concepts")
                self.aname.set("Avi Silberschatz")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:899")

            elif x=="Artificial Intelligence":
                self.bookid.set("110")
                self.booktitle.set("Artificial Intelligence")
                self.aname.set("Peter Norvig")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.bdate.set(d1)
                self.ddate.set(d3)
                self.fine.set("Rs:20")
                self.price.set("Rs:1799")


                

        listBox=Listbox(DataFrameRight,font="verdana 14 bold",width=15,height=10)
        listBox.bind("<<ListboxSelect>>",selectbook)
        listBox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=listBox.yview)

        for item in listBook:
            listBox.insert(END,item)
        
        #buttons
        frame2=Frame(self.root,bd=7,relief=RIDGE,padx=17,pady=5,bg="seagreen")
        frame2.place(x=0,y=420,width=1360,height=70)

        btnadddata=Button(frame2,text="Add Data",font="verdana 14 bold",width=13,bg="orangered2",fg="black",command=self.add_data)
        btnadddata.grid(row=0,column=0)

        btnshowdata=Button(frame2,text="Show Data",font="verdana 14 bold",width=13,bg="orangered2",fg="black",command=self.show_data)
        btnshowdata.grid(row=0,column=1)

        btnupdate=Button(frame2,text="Update",font="verdana 14 bold",width=13,bg="orangered2",fg="black",command=self.update)
        btnupdate.grid(row=0,column=2)

        btndel=Button(frame2,text="Delete",font="verdana 14 bold",width=13,bg="orangered2",fg="black",command=self.delete)
        btndel.grid(row=0,column=3)

        btnreset=Button(frame2,text="Reset",font="verdana 14 bold",width=13,bg="orangered2",fg="black",command=self.reset)
        btnreset.grid(row=0,column=4)

        btnexit=Button(frame2,text="Exit",font="verdana 14 bold",width=13,bg="orangered2",fg="black",command=self.iExit)
        btnexit.grid(row=0,column=5)

        btncount=Button(frame2,text="Issue Count",font="verdana 14 bold",width=13,bg="orangered2",fg="black",command=self.countbks)
        btncount.grid(row=0,column=6)

        #infoframe
        frame3=Frame(self.root,bd=7,relief=RIDGE,padx=8,bg="seagreen")
        frame3.place(x=0,y=490,width=1360,height=210)

        Table_frame=Frame(frame3,bd=6,relief=RIDGE,bg="seagreen")
        Table_frame.place(x=0,y=2,width=1330,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.librarytable=ttk.Treeview(Table_frame,column=("1","2","3",'4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.librarytable.xview)
        yscroll.config(command=self.librarytable.yview)

        self.librarytable.heading('1',text='Member Type')
        self.librarytable.heading('2',text='ID Number')
        self.librarytable.heading('3',text='First Name')
        self.librarytable.heading('4',text='Last Name')
        self.librarytable.heading('5',text='Address')
        self.librarytable.heading('6',text='Phone No')
        self.librarytable.heading('7',text='Sem')
        self.librarytable.heading('8',text='Book ID')
        self.librarytable.heading('9',text='Book Title')
        self.librarytable.heading('10',text='Author Name')
        self.librarytable.heading('11',text='Date Borrowed')
        self.librarytable.heading('12',text='Due Date')
        self.librarytable.heading('13',text='Fine')
        self.librarytable.heading('14',text='Price')

        self.librarytable["show"]="headings"
        self.librarytable.pack(fill=BOTH,expand=1)

        #adjustingwidth
        self.librarytable.column('1',width=100)
        self.librarytable.column('2',width=100)
        self.librarytable.column('3',width=100)
        self.librarytable.column('4',width=100)
        self.librarytable.column('5',width=100)
        self.librarytable.column('6',width=100)
        self.librarytable.column('7',width=100)
        self.librarytable.column('8',width=100)
        self.librarytable.column('9',width=100)
        self.librarytable.column('10',width=100)
        self.librarytable.column('11',width=100)
        self.librarytable.column('12',width=100)
        self.librarytable.column('13',width=100)
        self.librarytable.column('14',width=100)
        
        self.fetch_data()
        self.librarytable.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        print("sdfg")
        conn=mysql.connector.connect(host='localhost',user='root',password='Leg12345',database='librarymanagement',auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.member.get(),
                                                                                                   self.IDno.get(),
                                                                                                   self.fname.get(),
                                                                                                   self.lname.get(),
                                                                                                   self.address.get(),
                                                                                                   self.phoneno.get(),
                                                                                                   self.sem.get(),
                                                                                                   self.bookid.get(),
                                                                                                   self.booktitle.get(),
                                                                                                   self.aname.get(),
                                                                                                   self.bdate.get(),
                                                                                                   self.ddate.get(),
                                                                                                   self.fine.get(),
                                                                                                   self.price.get(),
                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member Added")


    def update(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='Leg12345',database='librarymanagement',auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,First_Name=%s,Last_Name=%s,Address=%s,Phone_No=%s,Sem=%s,Book_ID=%s,Book_Title=%s,Author_Name=%s,Date_Borrowed=%s,Due_Date=%s,Fine=%s,Price=%s where ID_Number=%s",(
                                                                            self.member.get(),
                                                                            self.fname.get(),
                                                                            self.lname.get(),
                                                                            self.address.get(),
                                                                            self.phoneno.get(),
                                                                            self.sem.get(),
                                                                            self.bookid.get(),
                                                                            self.booktitle.get(),
                                                                            self.aname.get(),
                                                                            self.bdate.get(),
                                                                            self.ddate.get(),
                                                                            self.fine.get(),
                                                                            self.price.get(),
                                                                            self.IDno.get()
                                                                    ))

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success!","Details Updated")

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='Leg12345',database='librarymanagement',auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("select *from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.librarytable.delete(*self.librarytable.get_children())
            for i in rows:
                self.librarytable.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event="e"):
        cursor_row=self.librarytable.focus()
        content=self.librarytable.item(cursor_row)
        row=content["values"]

        self.member.set(row[0]),
        self.IDno.set(row[1]),
        self.fname.set(row[2]),
        self.lname.set(row[3]),
        self.address.set(row[4]),
        self.phoneno.set(row[5]),
        self.sem.set(row[6]),
        self.bookid.set(row[7]),
        self.booktitle.set(row[8]),
        self.aname.set(row[9]),
        self.bdate.set(row[10]),
        self.ddate.set(row[11]),
        self.fine.set(row[12]),
        self.price.set(row[13])

    def show_data(self,event=""):
        self.txtBox.insert(END,'Member Type:\t'+self.member.get()+'\n')
        self.txtBox.insert(END,'ID No:\t'+self.IDno.get()+'\n')
        self.txtBox.insert(END,'First Name:\t'+self.fname.get()+'\n')
        self.txtBox.insert(END,'Last Name:\t'+self.lname.get()+'\n')
        self.txtBox.insert(END,'Address:\t'+self.address.get()+'\n')
        self.txtBox.insert(END,'Phone No:\t'+self.phoneno.get()+'\n')
        self.txtBox.insert(END,'Sem:\t'+self.sem.get()+'\n')
        self.txtBox.insert(END,'Book ID:\t'+self.bookid.get()+'\n')
        self.txtBox.insert(END,'Book Title:\t'+self.booktitle.get()+'\n')
        self.txtBox.insert(END,'Author Name:\t'+self.aname.get()+'\n')
        self.txtBox.insert(END,'Borrow Date:\t'+self.bdate.get()+'\n')
        self.txtBox.insert(END,'Due Date:\t'+self.ddate.get()+'\n')
        self.txtBox.insert(END,'Fine:\t'+self.fine.get()+'\n')
        self.txtBox.insert(END,'Price:\t'+self.price.get()+'\n')

    def reset(self):
        self.member.set(""),
        self.IDno.set(''),
        self.fname.set(''),
        self.lname.set(''),
        self.address.set(''),
        self.phoneno.set(''),
        self.sem.set(''),
        self.bookid.set(''),
        self.booktitle.set(''),
        self.aname.set(''),
        self.bdate.set(''),
        self.ddate.set(''),
        self.fine.set(''),
        self.price.set('')
        self.txtBox.delete(1.0,END)
        self.txtfname.delete(0,END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.IDno.get()=="":
            messagebox.showerror("Error","Select a member")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='Leg12345',database='librarymanagement',auth_plugin='mysql_native_password')
            my_cursor=conn.cursor()
            query="delete from library where ID_Number=%s"
            value=(self.IDno.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            messagebox.showinfo("Success!","Member Deleted")
            conn.close()
    
    def countbks(self):
        root = Tk()
        obj = Count(root)
        root.mainloop()

if __name__=="__main__":
    root=Tk()
    obj=lib(root)
    root.mainloop()