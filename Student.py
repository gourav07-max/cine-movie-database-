from tkinter import*
from tkinter import ttk
import tkinter as t
import pymysql




class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("CINEPHILE")
        self.root.geometry("1350x700+0+0")



        #all variables

        self.act_id_var=StringVar()
        self.act_name_var=StringVar()
        self.dir_id_var=StringVar()
        self.dir_name_var=StringVar()
        self.gen_id_var=StringVar()
        self.gen_name_var=StringVar()
        self.title_var=StringVar()
        self.mov_id_var=StringVar()
        self.release_date_var=StringVar()
        self.mov_time_var=StringVar()
        self.pro_id_var=StringVar()
        self.banner_var=StringVar()
        self.rev_id_var=StringVar()
        self.collections_var=StringVar()
        self.verdict_var=StringVar()
        self.r_id_var=StringVar()
        self.rate_var=StringVar()

        self.movie_by=StringVar()
        self.search_txt=StringVar()
        


        #Manage frame
   
        Manage_Frame=Frame(self.root, bd=4,relief=RIDGE)
        Manage_Frame.place(x=0,y=10,width=700,height=1000)


       

        #movie

        m_title=Label(Manage_Frame,text="MOVIE",font=("times new roman", 10, "bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        #m.title

        lbl_title=Label(Manage_Frame, text="Title",font=("times new roman",10,"bold"))
        lbl_title.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_title=Entry(Manage_Frame,textvariable=self.title_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_title.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        #mov_id
        
        lbl_movid=Label(Manage_Frame, text="Mov_id",font=("times new roman",10,"bold"))
        lbl_movid.grid(row=1,column=2,pady=10,padx=20,sticky="w")

        txt_movid=Entry(Manage_Frame,textvariable=self.mov_id_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_movid.grid(row=1,column=3,pady=10,padx=20,sticky="w")

        #m.realease

        lbl_rel=Label(Manage_Frame, text="Rel_date",font=("times new roman",10,"bold"))
        lbl_rel.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_rel=Entry(Manage_Frame,textvariable=self.release_date_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_rel.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        #m.time

        lbl_time=Label(Manage_Frame, text="R_time",font=("times new roman",10,"bold"))
        lbl_time.grid(row=2,column=2,pady=10,padx=20,sticky="w")

        txt_time=Entry(Manage_Frame,textvariable=self.mov_time_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_time.grid(row=2,column=3,pady=10,padx=20,sticky="w")

        #actor

        a_title=Label(Manage_Frame,text="ACTOR",font=("times new roman", 10, "bold"))
        a_title.grid(row=3,columnspan=2,pady=20)

        #a_id

        lbl_aid=Label(Manage_Frame, text="A_id",font=("times new roman",10,"bold"))
        lbl_aid.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_aid=Entry(Manage_Frame,textvariable=self.act_id_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_aid.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #a_name

        lbl_aname=Label(Manage_Frame, text="A_name",font=("times new roman",10,"bold"))
        lbl_aname.grid(row=4,column=2,pady=10,padx=20,sticky="w")

        txt_aname=Entry(Manage_Frame,textvariable=self.act_name_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_aname.grid(row=4,column=3,pady=10,padx=20,sticky="w")

        #director
        d_title=Label(Manage_Frame,text="DIRECTOR",font=("times new roman", 10, "bold"))
        d_title.grid(row=5,columnspan=2,pady=20)

        #d_id
        lbl_did=Label(Manage_Frame, text="D_id",font=("times new roman",10,"bold"))
        lbl_did.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_did=Entry(Manage_Frame,textvariable=self.dir_id_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_did.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        #d_name
        lbl_dname=Label(Manage_Frame, text="D_name",font=("times new roman",10,"bold"))
        lbl_dname.grid(row=6,column=2,pady=10,padx=20,sticky="w")

        txt_dname=Entry(Manage_Frame,textvariable=self.dir_name_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_dname.grid(row=6,column=3,pady=10,padx=20,sticky="w")

        #genre

        g_title=Label(Manage_Frame,text="GENRE",font=("times new roman", 10, "bold"))
        g_title.grid(row=7,columnspan=2,pady=20)

        #g_id
        lbl_gid=Label(Manage_Frame, text="G_id",font=("times new roman",10,"bold"))
        lbl_gid.grid(row=8,column=0,pady=10,padx=20,sticky="w")

        txt_gid=Entry(Manage_Frame,textvariable=self.gen_id_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_gid.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        #g_name
        lbl_gname=Label(Manage_Frame, text="G_name",font=("times new roman",10,"bold"))
        lbl_gname.grid(row=8,column=2,pady=10,padx=20,sticky="w")

        txt_gname=Entry(Manage_Frame,textvariable=self.gen_name_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_gname.grid(row=8,column=3,pady=10,padx=20,sticky="w")


        #producer

        p_title=Label(Manage_Frame,text="PRODUCER",font=("times new roman", 10, "bold"))
        p_title.grid(row=9,columnspan=2,pady=20)


        #p_id
        lbl_pid=Label(Manage_Frame, text="P_id",font=("times new roman",10,"bold"))
        lbl_pid.grid(row=10,column=0,pady=10,padx=20,sticky="w")

        txt_pid=Entry(Manage_Frame,textvariable=self.pro_id_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_pid.grid(row=10,column=1,pady=10,padx=20,sticky="w")

        #p_name
        lbl_pname=Label(Manage_Frame, text="P_name",font=("times new roman",10,"bold"))
        lbl_pname.grid(row=10,column=2,pady=10,padx=20,sticky="w")

        txt_pname=Entry(Manage_Frame,textvariable=self.banner_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_pname.grid(row=10,column=3,pady=10,padx=20,sticky="w")


         #revenue

        r_title=Label(Manage_Frame,text="REVENUE",font=("times new roman", 10, "bold"))
        r_title.grid(row=11,columnspan=2,pady=20)


        #rev_id
        lbl_revid=Label(Manage_Frame, text="Rev_id",font=("times new roman",10,"bold"))
        lbl_revid.grid(row=12,column=0,pady=10,padx=20,sticky="w")

        txt_revid=Entry(Manage_Frame,textvariable=self.rev_id_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_revid.grid(row=12,column=1,pady=10,padx=20,sticky="w")

        #collections
        lbl_revname=Label(Manage_Frame, text="collection",font=("times new roman",10,"bold"))
        lbl_revname.grid(row=12,column=2,pady=10,padx=20,sticky="w")

        txt_revname=Entry(Manage_Frame,textvariable=self.collections_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_revname.grid(row=12,column=3,pady=10,padx=20,sticky="w")


        #verdict

        lbl_ver=Label(Manage_Frame, text="Verdict",font=("times new roman",10,"bold"))
        lbl_ver.grid(row=11,column=2,pady=10,padx=20,sticky="w")

        txt_ver=Entry(Manage_Frame,textvariable=self.verdict_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_ver.grid(row=11,column=3,pady=5,padx=20,sticky="w")



         #Rating

        ra_title=Label(Manage_Frame,text="RATING",font=("times new roman", 10, "bold"))
        ra_title.grid(row=13,columnspan=2,pady=20)


        #R_id
        lbl_rid=Label(Manage_Frame, text="R_id",font=("times new roman",10,"bold"))
        lbl_rid.grid(row=14,column=0,pady=10,padx=20,sticky="w")

        txt_rid=Entry(Manage_Frame,textvariable=self.r_id_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_rid.grid(row=14,column=1,pady=10,padx=20,sticky="w")

        #rating
        lbl_rname=Label(Manage_Frame, text="Rate",font=("times new roman",10,"bold"))
        lbl_rname.grid(row=14,column=2,pady=10,padx=20,sticky="w")

        txt_rname=Entry(Manage_Frame,textvariable=self.rate_var,font=("times new roman",8,"bold"), bd=5,relief=GROOVE)
        txt_rname.grid(row=14,column=3,pady=10,padx=20,sticky="w")

        #button frame movie

        btn_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn_Frame.place(x=550,y=70,width=60)
        Addbtn=Button(btn_Frame,text="Add",width=5,command=self.add_movie).grid(row=0,column=4,padx=5,pady=5)



        btn1_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn1_Frame.place(x=620,y=70,width=60)
        updatebtn=Button(btn1_Frame,text="Update",width=5,command=self.update_data).grid(row=1,column=4,padx=5,pady=5)

        #button1 actor
        btn2_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn2_Frame.place(x=550,y=200,width=60)
        Addbtn=Button(btn2_Frame,text="Add",width=5,command=self.add_actor).grid(row=0,column=4,padx=5,pady=5)



        btn3_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn3_Frame.place(x=620,y=200,width=60)
        updatebtn=Button(btn3_Frame,text="Update",width=5,command=self.update_actor).grid(row=1,column=4,padx=5,pady=5)

        #button2 director


        btn4_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn4_Frame.place(x=550,y=300,width=60)
        Addbtn=Button(btn4_Frame,text="Add",width=5,command=self.add_director).grid(row=0,column=4,padx=5,pady=5)



        btn5_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn5_Frame.place(x=620,y=300,width=60)
        updatebtn=Button(btn5_Frame,text="Update",width=5,command=self.update_director).grid(row=1,column=4,padx=5,pady=5)

        #button3 genre

        btn6_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn6_Frame.place(x=550,y=400,width=60)
        Addbtn=Button(btn6_Frame,text="Add",width=5,command=self.add_genre).grid(row=0,column=4,padx=5,pady=5)



        btn7_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn7_Frame.place(x=620,y=400,width=60)
        updatebtn=Button(btn7_Frame,text="Update",width=5,command=self.update_genre).grid(row=1,column=4,padx=5,pady=5)


        #button4 producer

        btn8_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn8_Frame.place(x=550,y=500,width=60)
        Addbtn=Button(btn8_Frame,text="Add",width=5,command=self.add_producer).grid(row=0,column=4,padx=5,pady=5)



        btn9_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn9_Frame.place(x=620,y=500,width=60)
        updatebtn=Button(btn9_Frame,text="Update",width=5,command=self.update_producer).grid(row=1,column=4,padx=5,pady=5)


        #button5 revenue

        btn10_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn10_Frame.place(x=550,y=600,width=60)
        Addbtn=Button(btn10_Frame,text="Add",width=5,command=self.add_revenue).grid(row=0,column=4,padx=5,pady=5)



        btn11_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn11_Frame.place(x=620,y=600,width=60)
        updatebtn=Button(btn11_Frame,text="Update",width=5,command=self.update_revenue).grid(row=1,column=4,padx=5,pady=5)


        #button6 rating

        btn12_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn12_Frame.place(x=550,y=710,width=60)
        Addbtn=Button(btn12_Frame,text="Add",width=5,command=self.add_rating).grid(row=0,column=4,padx=5,pady=5)



        btn13_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn13_Frame.place(x=620,y=710,width=60)
        updatebtn=Button(btn13_Frame,text="Update",width=5,command=self.update_rating).grid(row=1,column=4,padx=5,pady=5)

        #clear
        
        btn14_Frame=Frame(Manage_Frame, bd=4,relief=RIDGE)
        btn14_Frame.place(x=550,y=10,width=100)
        Addbtn=Button(btn14_Frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=4,padx=5,pady=5)


    #Deatail frame

        Detail_Frame=Frame(self.root, bd=4,relief=RIDGE)
        Detail_Frame.place(x=700,y=10,width=1000,height=800)

        #movie_by
 
        lbl_search=Label(Detail_Frame, text="MOVIE BY",font=("times new roman",15,"bold"))
        lbl_search.grid(row=7,column=0,pady=10,padx=20,sticky="w")


        #combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",10),state='readonly')
        #combo_search['values']=('All')
        #combo_search.grid(row=1,column=0,padx=20,pady=10)

        
        


        #search

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=("times new roman",12),relief=GROOVE)
        txt_search.grid(row=9,column=0,pady=10,padx=20,sticky="w")

        #button

        searchbtn=Button(Detail_Frame,text="SEARCH TITLE",width=15,command=self.search1_data).grid(row=8,column=0,padx=10,pady=10)


        searchbtn=Button(Detail_Frame,text="S_ACTOR" ,width=15,command=self.search2_data).grid(row=8,column=1,padx=10,pady=10)

        searchbtn=Button(Detail_Frame,text="S_DIRECTOR",width=15,command=self.search3_data).grid(row=8,column=2,padx=10,pady=10)


        searchbtn=Button(Detail_Frame,text="S_GENRE",width=15,command=self.search4_data).grid(row=8,column=3,padx=10,pady=10)

        searchbtn=Button(Detail_Frame,text="S_PRODUCER",width=15,command=self.search5_data).grid(row=8,column=4,padx=10,pady=10)

        searchbtn=Button(Detail_Frame,text="S_VERDICT",width=15,command=self.search6_data).grid(row=8,column=5,padx=10,pady=10)

        

        searchbtn=Button(Detail_Frame,text="SHOW ALL",width=15,command=self.search_data).grid(row=9,column=1,padx=10,pady=10)





    #TABLE FRAME

        Table_Frame=Frame(Detail_Frame, bd=4,relief=RIDGE)
        Table_Frame.place(x=10,y=200,width=800,height=500)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("mov_id","title","release_date","mov_time","act_id","act_name","dir_id" ,"dir_name", "gen_id" ,"gen_name","pro_id","banner","rev_id","collections","verdict","r_id","rate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)  
        scroll_y.pack(side=RIGHT,fill=Y)
       
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("act_id", text="A_id")
        self.Student_table.heading("act_name", text="A_Name")
        self.Student_table.heading("dir_id", text="D_id")
        self.Student_table.heading("dir_name", text="D_name")
        self.Student_table.heading("gen_id", text="G_id")
        self.Student_table.heading("gen_name", text="G_name")
        self.Student_table.heading("title", text="TITLE")
        self.Student_table.heading("mov_id", text="M_id")
        self.Student_table.heading("release_date", text="R_date")
        self.Student_table.heading("mov_time", text=" M_time")
        self.Student_table.heading("pro_id", text="P_id")
        self.Student_table.heading("banner", text="Banner")
        self.Student_table.heading("rev_id", text="Rev_id")
        self.Student_table.heading("collections", text="COLLECTION")
        self.Student_table.heading("verdict", text="VERDICT")
        self.Student_table.heading("r_id", text="R_id")
        self.Student_table.heading("rate", text="RATE")

        self.Student_table['show']='headings'

       


        self.Student_table.pack(fill=BOTH,expand=1)

        
        
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        #self.fetch_data()
        #self.actor_data()


         #addbutton function

    def add_movie(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("insert into movie values(%s,%s,%s,%s)",(self.mov_id_var.get(),
                                                             self.title_var.get(),
                                                             self.release_date_var.get(),
                                                             self.mov_time_var.get()
                                                             ))

        con.commit()
        #self.fetch_data()
        
        con.close()

    def add_actor(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("insert into actor values(%s,%s,%s)",(self.mov_id_var.get(),
                                                          self.act_id_var.get(),
                                                          self.act_name_var.get()
                                                          ))

        con.commit()
        #self.actor_data()
        self.clear()
        con.close()

    def add_director(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("insert into director values(%s,%s,%s)",(self.mov_id_var.get(),
                                                             self.dir_id_var.get(),
                                                             self.dir_name_var.get()
                                                             ))

        con.commit()
        #self.director_data()
        self.clear()
        con.close()


    def add_genre(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("insert into genre values(%s,%s,%s)",(self.mov_id_var.get(),
                                                          self.gen_id_var.get(),
                                                          self.gen_name_var.get()
                                                          ))

        con.commit()
        #self.genre_data()
        self.clear()
        con.close()


    def add_producer(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("insert into producer values(%s,%s,%s)",(self.mov_id_var.get(),
                                                             self.pro_id_var.get(),
                                                             self.banner_var.get()
                                                             ))

        con.commit()
        #self.producer_data()
        self.clear()
        con.close()


    def add_revenue(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("insert into revenue values(%s,%s,%s,%s)",(self.mov_id_var.get(),
                                                               self.rev_id_var.get(),
                                                               self.collections_var.get(),
                                                               self.verdict_var.get()
                                                               ))

        con.commit()
        #self.revenue_data()
        self.clear()
        con.close()

    def add_rating(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("insert into rating values(%s,%s,%s)",(self.mov_id_var.get(),
                                                           self.r_id_var.get(),
                                                           self.rate_var.get()
                                                           ))

        con.commit()
        #self.rating_data()
        self.clear()
        con.close()

 

        #update

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("update movie set title=%s,release_date=%s,mov_time=%s where mov_id=%s",(
            self.title_var.get(),
            self.release_date_var.get(),
            self.mov_time_var.get(),
            self.mov_id_var.get()
            ))

        con.commit()
        self.clear()
        con.close()

    def update_actor(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("update actor set mov_id=%s,act_name=%s where act_id=%s",(
            self.mov_id_var.get(),
            self.act_name_var.get(),
            self.act_id_var.get()
            ))

        con.commit()
        self.clear()
        con.close()


    def update_director(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("update director set mov_id=%s,dir_name=%s where dir_id=%s",(
            self.mov_id_var.get(),
            self.dir_name_var.get(),
            self.dir_id_var.get()
            ))

        con.commit()
        self.clear()
        con.close()


    def update_genre(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("update genre set mov_id=%s,gen_name=%s where gen_id=%s",(
            self.mov_id_var.get(),
            self.gen_name_var.get(),
            self.gen_id_var.get()
            ))

        con.commit()
        self.clear()
        con.close()

    def update_producer(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("update producer set mov_id=%s,banner=%s where pro_id=%s",(
            self.mov_id_var.get(),
            self.banner_var.get(),
            self.pro_id_var.get()
            ))

        con.commit()
        self.clear()
        con.close()

    def update_revenue(self):
        con=pymysql.connect(host="localhost",user="root",password="gppgkr",database="cine")
        cur=con.cursor()
        cur.execute("update revenue set mov_id=%s,collections=%s,verdict=%s where rev_id=%s",(
            self.mov_id_var.get(),
            self.collections_var.get(),
            self.verdict_var.get(),
            self.rev_id_var.get()
            ))

        con.commit()
        self.clear()
        con.close()

    def update_rating(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("update rating set mov_id=%s,rate=%s where r_id=%s",(
            self.mov_id_var.get(),
            self.rate_var.get(),
            self.r_id_var.get()
            ))

        con.commit()
        self.clear()
        con.close()
 

    #clear

    def clear(self):
        
        self.act_id_var.set("")
        self.act_name_var.set("")
        self.dir_id_var.set("")
        self.dir_name_var.set("")
        self.gen_id_var.set("")
        self.gen_name_var.set("")
        self.title_var.set("")
        self.mov_id_var.set("")
        self.release_date_var.set("")
        self.mov_time_var.set("")
        self.pro_id_var.set("")
        self.banner_var.set("")
        self.rev_id_var.set("")
        self.collections_var.set("")
        self.verdict_var.set("")
        self.r_id_var.set("")
        self.rate_var.set("")


        #cursor

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']

        
        self.mov_id_var.set(row[0])
        self.title_var.set(row[1])
        self.release_date_var.set(row[2])
        self.mov_time_var.set(row[3])
        self.act_id_var.set(row[4])
        self.act_name_var.set(row[5])
        self.dir_id_var.set(row[6])
        self.dir_name_var.set(row[7])
        self.gen_id_var.set(row[8])
        self.gen_name_var.set(row[9])
        self.pro_id_var.set(row[10])
        self.banner_var.set(row[11])
        self.rev_id_var.set(row[12])
        self.collections_var.set(row[13])
        self.verdict_var.set(row[14])
        self.r_id_var.set(row[15])
        self.rate_var.set(row[16])

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("select movie.mov_id,title,release_date,mov_time,act_id,act_name,dir_id,dir_name,gen_id,gen_name,pro_id,banner,rev_id,collections,verdict,r_id,rate from movie,actor,director,genre,producer,revenue,rating where movie.mov_id=actor.mov_id and movie.mov_id=director.mov_id and movie.mov_id=director.mov_id and movie.mov_id=genre.mov_id and movie.mov_id=producer.mov_id and movie.mov_id=revenue.mov_id and movie.mov_id=rating.mov_id;")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
                
        con.close()

    def search1_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        
        cur.execute(" select movie.mov_id,title,release_date,mov_time,act_id,act_name,dir_id,dir_name,gen_id,gen_name,pro_id,banner,rev_id,collections,verdict,r_id,rate from movie,actor,director,genre,producer,revenue,rating where movie.mov_id=actor.mov_id and movie.mov_id=director.mov_id and movie.mov_id=director.mov_id and movie.mov_id=genre.mov_id and movie.mov_id=producer.mov_id and movie.mov_id=revenue.mov_id and movie.mov_id=rating.mov_id and title"+" like '%"+str(self.search_txt.get())+"%'")
        
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                
            con.commit()
                
            
        con.close()

    def search2_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute(" select movie.mov_id,title,release_date,mov_time,act_id,act_name,dir_id,dir_name,gen_id,gen_name,pro_id,banner,rev_id,collections,verdict,r_id,rate from movie,actor,director,genre,producer,revenue,rating where movie.mov_id=actor.mov_id and movie.mov_id=director.mov_id and movie.mov_id=director.mov_id and movie.mov_id=genre.mov_id and movie.mov_id=producer.mov_id and movie.mov_id=revenue.mov_id and movie.mov_id=rating.mov_id and act_name"+" like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()

        con.close()

    def search3_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute(" select movie.mov_id,title,release_date,mov_time,act_id,act_name,dir_id,dir_name,gen_id,gen_name,pro_id,banner,rev_id,collections,verdict,r_id,rate from movie,actor,director,genre,producer,revenue,rating where movie.mov_id=actor.mov_id and movie.mov_id=director.mov_id and movie.mov_id=director.mov_id and movie.mov_id=genre.mov_id and movie.mov_id=producer.mov_id and movie.mov_id=revenue.mov_id and movie.mov_id=rating.mov_id and dir_name"+" like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()

        con.close()


    def search4_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("  select movie.mov_id,title,release_date,mov_time,act_id,act_name,dir_id,dir_name,gen_id,gen_name,pro_id,banner,rev_id,collections,verdict,r_id,rate from movie,actor,director,genre,producer,revenue,rating where movie.mov_id=actor.mov_id and movie.mov_id=director.mov_id and movie.mov_id=director.mov_id and movie.mov_id=genre.mov_id and movie.mov_id=producer.mov_id and movie.mov_id=revenue.mov_id and movie.mov_id=rating.mov_id and gen_name"+" like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()

        con.close()


    def search5_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("  select movie.mov_id,title,release_date,mov_time,act_id,act_name,dir_id,dir_name,gen_id,gen_name,pro_id,banner,rev_id,collections,verdict,r_id,rate from movie,actor,director,genre,producer,revenue,rating where movie.mov_id=actor.mov_id and movie.mov_id=director.mov_id and movie.mov_id=director.mov_id and movie.mov_id=genre.mov_id and movie.mov_id=producer.mov_id and movie.mov_id=revenue.mov_id and movie.mov_id=rating.mov_id and banner"+" like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()

        con.close()

    def search6_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="cine")
        cur=con.cursor()
        cur.execute("  select movie.mov_id,title,release_date,mov_time,act_id,act_name,dir_id,dir_name,gen_id,gen_name,pro_id,banner,rev_id,collections,verdict,r_id,rate from movie,actor,director,genre,producer,revenue,rating where movie.mov_id=actor.mov_id and movie.mov_id=director.mov_id and movie.mov_id=director.mov_id and movie.mov_id=genre.mov_id and movie.mov_id=producer.mov_id and movie.mov_id=revenue.mov_id and movie.mov_id=rating.mov_id and verdict"+" like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children()) 
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()

        con.close()



    
        











root=Tk()
ob=Student(root)
root.mainloop()
 

