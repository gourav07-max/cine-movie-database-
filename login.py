from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql
 
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOG-IN")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #bg image

        self.bg=ImageTk.PhotoImage(file="C:/Users/gourav rudrawar/Downloads/Cinema.png") 
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        #login frame

        frame1=Frame(self.root,bg="white")
        frame1.place(x=400,y=150,width=700,height=500)
                                                                                                                                                                            
        title=Label(frame1,text="LOGIN HERE",font=("times new roman",30,"bold"),fg="blue").place(x=200,y=30)

        email=Label(frame1,text="EMAIL ADDRESS",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=50,y=150,width=350,height=35)
        

        password=Label(frame1,text="PASSWORD",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=200)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=250,width=350,height=35)
        

        btn_new=Button(frame1,text="Register new account",font=("times new roman",12),bg="lightgray",cursor="hand2",command=self.reg).place(x=50,y=300)
        

        self.btn_img=ImageTk.PhotoImage(file="C:/Users/gourav rudrawar/Downloads/log.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.login).place(x=250,y=370)


    def reg(self):
        self.root.destroy()
        import Register
        
        

    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="register")
                cur=con.cursor()
                cur.execute("select * from reg where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","INVALID,email & password",parent=self.root)

                else:
                    messagebox.showinfo("Success","WELCOME",parent=self.root)
                    self.root.destroy()
                    import Student
                con.close()



            except Exception as es:
                messagebox.showerror("Error",f"error due to:{str(es)}",parent=self.root)
        

                        




root=Tk()
obj=login(root)
root.mainloop()
