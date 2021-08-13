from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql
 
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("CINEPHILE")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        #===Bg Image===

        self.bg=ImageTk.PhotoImage(file="C:/Users/gourav rudrawar/Downloads/Glowing-Mountain-art-nature-Desktop-Wallpaper-HD-2560x1440.jpg") 
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        self.left=ImageTk.PhotoImage(file="C:/Users/gourav rudrawar/Downloads/cinephile-gift-guide-CA.jpg") 
        left=Label(self.root,image=self.left).place(x=250,y=150,width=400,height=500)

        #cinephile frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=650,y=150,width=700,height=500)
        title=Label(frame1,text="WELCOME TO CINEPHILE",font=("times new roman",20,"bold"),bg="white").place(x=50,y=30)

        #first name frame
        
        f_name=Label(frame1,text="FIRST NAME",font=("times now roman",15,"bold"),bg="white").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        # last name 
        
        l_name=Label(frame1,text="LAST NAME",font=("times now roman",15,"bold"),bg="white").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #contact

        contact=Label(frame1,text="CONTACT NO",font=("times now roman",15,"bold"),bg="white").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        #EMAIL

        email=Label(frame1,text="EMAIL",font=("times now roman",15,"bold"),bg="white").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        #security q

        security=Label(frame1,text="SECURITY QUESTION",font=("times now roman",15,"bold"),bg="white").place(x=50,y=240)

        
        self.cmb_sec=ttk.Combobox(frame1,font=("times new roman",15),state='readonly',justify=CENTER)
        self.cmb_sec['values']=("Select","your nick name","your favorite colour")
        self.cmb_sec.place(x=50,y=270,width=250)
        self.cmb_sec.current(0)
        

        #answer

        answer=Label(frame1,text="ANSWER",font=("times now roman",15,"bold"),bg="white").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)


        #password

        password=Label(frame1,text="PASSWORD",font=("times now roman",15,"bold"),bg="white").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        #CONFIRM

        cpass=Label(frame1,text="CONFIRM PASSWORD",font=("times now roman",15,"bold"),bg="white").place(x=370,y=310)
        self.txt_cpass=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpass.place(x=370,y=340,width=250)



        self.btn_img=ImageTk.PhotoImage(file="C:/Users/gourav rudrawar/Downloads/register.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=370)

        btn_login=Button(self.root,text="LOG-IN",font=("times new roman",20),bd=0,cursor="hand2",command=self.login).place(x=400,y=600)


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpass.delete(0,END)
        self.cmb_sec.current(0)
        self.txt_answer .delete(0,END)


    def login(self):
        self.root.destroy()
        import login
        


    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_sec.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpass.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)

        elif self.txt_password.get()!=self.txt_cpass.get():
            messagebox.showerror("Error","password and confirm password should be same",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="register")
                cur=con.cursor()
                cur.execute("select * from reg where email=%s",self.txt_email.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","user already exist,try another email",parent=self.root)
                else:
                    cur.execute("insert into reg (fname,lname,contact,email,security,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.cmb_sec.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()
                                 ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Successful",parent=self.root)
                    self.clear()



            except Exception as es:
                messagebox.showerror("Error",f"error due to: {str(es)}",parent=self.root)
                

            
            
    
        

root=Tk()
obj=Register(root)
root.mainloop()
 
