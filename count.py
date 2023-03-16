from tkinter import *
import mysql.connector
from tkinter import ttk

class Count:
    def __init__(self,root):
        self.root=root
        self.root.title("Issued Books")
        self.root.geometry("400x500")
        
        frame3=Frame(self.root,bd=7,relief=RIDGE,padx=2,bg="burlywood4",pady=3)
        frame3.place(x=0,y=0,width=400,height=500)

        Table_frame=Frame(frame3,bd=6,relief=RIDGE,bg="burlywood4")
        Table_frame.place(x=0,y=0,width=380,height=480)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.issuecount=ttk.Treeview(Table_frame,column=("1","2"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.issuecount.xview)
        yscroll.config(command=self.issuecount.yview)

        self.issuecount.heading('1',text='Book Title')
        self.issuecount.heading('2',text='No of Copies Issued')

        self.issuecount["show"]="headings"
        self.issuecount.pack(fill=BOTH,expand=1)

        #adjustingwidth
        self.issuecount.column('1',width=200)
        self.issuecount.column('2',width=100)

        self.fetch_data()
        # self.issuecount.bind("<ButtonRelease-1>",self.get_cursor)

    def fetch_data(self):
        conn=mysql.connector.connect(host='',user='',password='',database='',auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("select Book_Title, count(*) from library group by Book_Title")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.issuecount.delete(*self.issuecount.get_children())
            for i in rows:
                self.issuecount.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Count(root)
    root.mainloop()
