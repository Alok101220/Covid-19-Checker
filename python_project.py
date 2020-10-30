#========CORONA VIRUS===============
##----------importing modules------

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import webbrowser

#_______________________Defining class________________________

class covid19:
    def __init__(self,root):
        
        
#---------Connecting to DATABASE----------------------------------------------
    
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="alok91340",
            database="corona_database"
            )

        self.mrcs=self.con.cursor()
        
        self.root=root
        
#---------------tkinter window size-------------------------------------------
        
        self.root.minsize(550,700+0+0)
        self.root.maxsize(550,700+0+0)
        self.root.title("COVID-19 CHECKER")
        self.root.iconphoto(True,PhotoImage(file='logo.png'))
#============================================Working in Frame 1===================================================================================
        
    def Frame1(self):
        
        self.frame_1=Frame(self.root,bd=0)
        self.frame_1.place(x=0,y=0)
        self.m_image=Image.open("front.jpg")
        self.resize=self.m_image.resize((900,700), Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(self.resize)
        self.label=Label(self.frame_1,image=self.photo,bd=0)
        self.label.pack()
        
        
        #-----------------------------Label's of FRAME 1--------------------------------------
        
        self.app_label=Label(self.frame_1,text="Welcome to COVID-19 tester",font=("Courier",23,"bold"),bg="#0A0D24",fg="#F50B0B")
        self.app_label.place(x=30,y=25)
        self.label_frame1=Label(self.frame_1,text=" Each one of us has the power to help prevent the spread of the",bg="#0A0D24",fg="#F0FFA9",font=("Comic Sans MS",11,""))
        self.label_frame1.place(x=60,y=250)
        self.label1_frame1=Label(self.frame_1,text="coronavirus pandemic in India.",bg="#0A0D24",fg="#F0FFA9",font=("Comic Sans MS",11,""))
        self.label1_frame1.place(x=170,y=280)
        #----------------------placing Label's------------------------------------
        self.label1=Label(self.frame_1,text="Follow:-",bg="#0A0D24",fg="#C3FFA9",font=("helvetica",10,"italic"))
        self.label1.place(x=85,y=340)
        self.label1=Label(self.frame_1,text="Wear mask",bg="#0A0D24",fg="#C3FFA9",font=("helvetica",10,"italic"))
        self.label1.place(x=140,y=380)
        self.label1=Label(self.frame_1,text="Use sanitizer",bg="#0A0D24",fg="#C3FFA9",font=("helvetica",10,"italic"))
        self.label1.place(x=140,y=410)
        self.label1=Label(self.frame_1,text="Social distance",bg="#0A0D24",fg="#C3FFA9",font=("helvetica",10,"italic"))
        self.label1.place(x=140,y=440)
        
        #----------------------------Frame 1 BUTTON--------------------------------------------
        self.next=Button(self.frame_1,text="Proceed",font=("B612", 15, "bold"),cursor="hand2",width=10,command=self.Frame2,bg="#0A0D24",activebackground="#0A0D24",bd=0,fg="#E7C831",activeforeground="#E7C831")
        self.next.place(x=220,y=610)
        
        
#===============================================FRAME 2=============================================================================================
        
    def Frame2(self):
        
        self.frame_2=Frame(self.root,bd=0)
        self.frame_2.place(x=0,y=0)
        self.m_image=Image.open("22.jpg")
        self.resize=self.m_image.resize((700,700), Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(self.resize)
        self.label=Label(self.frame_2,image=self.photo,bd=0)
        self.label.pack()
        
        #-----------------------------login button-------------------------
        
        self.login_img=ImageTk.PhotoImage(file="r_l (1).png")
        self._register=Button(self.frame_2,image=self.login_img,activebackground="grey",cursor="hand2",command=self.Frame3,bd=0)
        self._register.place(x=140,y=200)
        
        self.sep_label=Label(self.frame_2,text="-------------------------------------------------------------------",bg="#0c0c27")
        self.sep_label.place(x=120,y=290)
         
        #--------------or label----------------------------
        self.Or_label=Label(self.frame_2,text="OR",bg="#0c0c27")
        self.Or_label.place(x=280,y=290)
        
        #----------------------registration button-----------
        
        self.registration_img=ImageTk.PhotoImage(file="r_l (2).png")
        self._login=Button(self.frame_2,image=self.registration_img,command=self.Frame4,cursor="hand2",activebackground="grey",bd=0)
        self._login.place(x=100,y=350)

#======================================================FRAME 3==============================================================================

    def Frame3(self):
        #--------------allocating background image for login page----------
        
        self.m_image=Image.open("back-login.png")
        self.resize=self.m_image.resize((900,700), Image.ANTIALIAS)
        self.frame_photo=ImageTk.PhotoImage(self.resize)
        self.label=Label(self.root,image=self.frame_photo,bd=0)
        self.label.place(x=0,y=0)
        
        #--------------------now working in login frame----------------------
        self.login_frame=Frame(self.root,width=440,height=600,bd=0,bg="black")
        self.login_frame.place(x=57,y=50)
        
        
        self.login_title=Label(self.login_frame,text="LOGIN",font=("Comic Sans MS",32,"bold"),bg="black",fg="#b3ffff",bd=0,width=10)
        self.login_title.place(x=100,y=75)

        #-------------defining variables for input of usename and password----------------
        self.use=StringVar()
        self.passwd=StringVar()

        #--------------labels and entry widget of login page-------------------

        self.label_user=Label(self.login_frame,text="Username",font=("Perpetua",14,"bold"),bg="black",fg="#fff9e5",bd=0,width=10)
        self.label_passwd=Label(self.login_frame,text="Password",font=("Perpetua",14,"bold"),bg="black",fg="#fff9e5",bd=0,width=10)
        self.entry_user=Entry(self.login_frame,textvariable=self.use)
        self.entry_passwd=Entry(self.login_frame,textvariable=self.passwd,show="*")

        #--------------packing of labels and entries--------------------------
        
        self.label_user.place(x=90,y=160)
        self.entry_user.place(x=240,y=160)
        self.label_passwd.place(x=90,y=197)
        self.entry_passwd.place(x=240,y=197)

        #-----------------login button of login page--------------------------
         
        self.login_button=Button(self.login_frame,text="Log In",font=("Goudy Old Style",13,"bold"),cursor="hand2",command=self.login_action,bg="#707070",fg="#b3ffff",activebackground="#707070",activeforeground="#b3ffff",width=20,height=0)
        self.login_button.place(x=120,y=243)

#========forgot password========
        #self.forgot_pass=Button(self.login_frame,text="Forgot password.?",font=("Goudy Old Style",13,"bold"),cursor="hand2",fg="#b3ffff",activeforeground="#b3ffff",bg="black",activebackground="black",width=20,bd=0)
        #self.forgot_pass.place(x=120,y=300)
        
        
        #----------------register button of login page-----------------------
        
        self.not_registered=Label(self.login_frame,text="Not a member?",bg="black",fg="#fff9e5",width=20)
        self.not_registered.place(x=90,y=315)
        self.not_registered=Button(self.login_frame,text="Register now!",font=("Goudy Old Style",11,"bold"),cursor="hand2",bg="black",bd=0,fg="#b3ffff",activeforeground="#b3ffff",activebackground="black",command=self.Frame4)
        self.not_registered.place(x=230,y=310)
        
        #--------foloow us button-------------------------------------------
        
        self.follow=Label(self.login_frame,text="Follow us here!",bg="black",fg="#fff9e5",font=("Perpetua",15,""),width=20)
        self.follow.place(x=115,y=360)
        
        #-----1. INSTAGRAM-----------
        
        self.insta=Image.open("insta.jpg")
        self.resize=self.insta.resize((30,30), Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(self.resize)
        self.follow_insta=Button(self.login_frame,image=self.photo,command=self.instagram_,cursor="hand2",bg="black",bd=0,activebackground="black",)
        self.follow_insta.place(x=150,y=400)
        
        #------------2. Facebook----------------
        
        self.facebook=Image.open("facebook.png")
        self.resize=self.facebook.resize((30,30), Image.ANTIALIAS)
        self.face=ImageTk.PhotoImage(self.resize)
        self.follow_facebook=Button(self.login_frame,image=self.face,command=self.facebook_,cursor="hand2",bg="black",bd=0,activebackground="black",)
        self.follow_facebook.place(x=200,y=400)
        
        #------------3. Twitter--------------------
        
        self.linkedin=Image.open("linkedin.png")
        self.resize=self.linkedin.resize((35,35), Image.ANTIALIAS)
        self.linkd=ImageTk.PhotoImage(self.resize)
        self.follow_linkd=Button(self.login_frame,image=self.linkd,command=self.linkedin_,cursor="hand2",bg="black",bd=0,activebackground="black",)
        self.follow_linkd.place(x=250,y=398)
        
        
        #-------------------LOGIN ACTION Area---------------------------------
        
    def login_action(self):
        self.x=self.use.get()
        self.y=self.passwd.get()
        
        if (self.x==""):
            messagebox.showerror("Fill","Username missing!")
        elif (self.y==""):
            messagebox.showerror("Fill","Password missing!")
        else:
            self.mrcs.execute("select * from register where email=%s and passw=%s",(self.x,self.y))
            self.result=self.mrcs.fetchone()
            if self.result==None:
                messagebox.showerror("Error", "You are not registered!!")
                self.entry_user.delete(0,END)
                self.entry_passwd.delete(0,END)
            
            else:
                self.Frame5()
                self.entry_user.delete(0,END)
                self.entry_passwd.delete(0,END)
                
                
                    
#=================================FRAME 4============================================================================================
            
    def Frame4(self):
        
        self.m_image=Image.open("back-login.png")
        self.resize=self.m_image.resize((900,700),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(self.resize)
        self.label=Label(self.root,image=self.photo,bd=0)
        self.label.place(x=0,y=0)
        
        #---------------------REGISTRATION PAGE working----------------------------------------------------------------------
        
        self.register_frame=Frame(self.root,width=450,height=600,bg="black",bd=0)
        self.register_frame.place(x=50,y=50)
       
        #--------------------------------Defining labels ------------------------------------------------------------------
        
        self.register=Label(self.register_frame,text="Register Here!",font=("Comic Sans MS",32,"bold"),bg="black",fg="#b3ffff",bd=0,width=17)
        self.f_label=Label(self.register_frame,text="First name:",font=("Perpetua",14,"bold"),bg="black",fg="#fff9e5",bd=0,)
        self.l_label=Label(self.register_frame, text="Last name:",font=("Perpetua",14,"bold"),bg="black",fg="#fff9e5",bd=0,)
        self.E_label=Label(self.register_frame,text="E-mail:",font=("Perpetua",14,"bold"),bg="black",fg="#fff9e5",bd=0,)
        self.p_label=Label(self.register_frame,text="Phone number:",font=("Perpetua",14,"bold"),bg="black",fg="#fff9e5",bd=0,)
        self.fpasswd=Label(self.register_frame,text="Password",font=("Perpetua",14,"bold"),bg="black",fg="#fff9e5",bd=0,)
        self.confirmpasswd=Label(self.register_frame,text="Confirm password",font=("Perpetua",14,"bold"),bg="black",fg="#fff9e5",bd=0,)

        #---------------------------packing labels---------------------------------------------------------------------------
        
        self.register.place(x=10,y=20)
        self.f_label.place(x=50,y=110)
        self.l_label.place(x=295,y=110)
        self.E_label.place(x=50,y=175)
        self.p_label.place(x=295,y=175)
        self.fpasswd.place(x=50,y=230)
        self.confirmpasswd.place(x=295,y=230)  

        #-----------------------------------Defining Entries------------------------------------------------------------------
        
        self.f_entry=Entry(self.register_frame)
        self.l_entry=Entry(self.register_frame)
        self.e_entry=Entry(self.register_frame)
        self.p_entry=Entry(self.register_frame)
        self.pass_entry=Entry(self.register_frame,show="*")
        self.cnfirm_entry=Entry(self.register_frame,show="*")
        
        #----------------------------packing entries---------------------------------
        
        self.f_entry.place(x=50,y=135)
        self.l_entry.place(x=295,y=135)
        self.e_entry.place(x=50,y=200)
        self.p_entry.place(x=295,y=200)
        self.pass_entry.place(x=50,y=255)
        self.cnfirm_entry.place(x=295,y=255)

        #-----------------------------packing entries--------------------------------------------------------------------------
        
        self.register_button=Button(self.register_frame,text="Register",font=("Goudy Old Style",13,"bold"),cursor="hand2",bg="#707070",fg="#b3ffff",activebackground="#707070",activeforeground="#b3ffff",width=20,height=0,command=self.getvalue)
        self.register_button.place(x=130,y=340)
        
        #------------------------------------login here if already member--------------------------------------------------------------------
        
        self.register_button=Button(self.register_frame,text="Please login here",font=("Goudy Old Style",11,"bold"),cursor="hand2",bg="black",bd=0,fg="#b3ffff",activeforeground="#b3ffff",activebackground="black",width=20,command=self.Frame3)
        self.register_button.place(x=210,y=395)
        self.register_button=Label(self.register_frame,text="Already member?",bg="black",fg="#fff9e5")
        self.register_button.place(x=120,y=400)
        
        #-------------------------CHECKBUTTON-------------------------------------------------------------------------------------------
        
        self.var=IntVar()
        
        self.check=Checkbutton(self.register_frame,text="Please confirm our term & conditions!",variable=self.var,onvalue=1,offvalue=0,font=("Goudy Old Style",11,"bold"),bg="black",fg="#ecb3ff",bd=0,activeforeground="#00134d",activebackground="black",width=40)
        self.check.place(x=60,y=290)

        #------------------Getting values and INSERTing to database------------------------------------------------------------------------
        
    def getvalue(self):
        self.a=self.f_entry.get() 
        self.b=self.l_entry.get() 
        self.c=self.e_entry.get()
        self.d=self.p_entry.get()
        self.e=self.pass_entry.get()
        self.f=self.cnfirm_entry.get()
        self.g=self.var.get()
        if (self.a=="" or self.b=="" or self.c=="" or self.d=="" or self.e=="" or self.f==""):
            messagebox.showerror("Error", "Sorry...please fill all detailes")
        elif (self.e==self.f):
            if self.g==0:
                messagebox.showwarning("Warning","Please agree with terms & conditions")
            else:
                try:
                    self.mrcs.execute("insert into register values (%s,%s,%s,%s,%s,%s)",(self.a,self.b,self.c,self.d,self.e,self.f))
                    self.con.commit()
    
                    messagebox.showinfo("Done", "Your registration is successfull")
                    self.f_entry.delete(0,END)
                    self.l_entry.delete(0,END)
                    self.e_entry.delete(0,END)
                    self.p_entry.delete(0,END)
                    self.pass_entry.delete(0,END)
                    self.cnfirm_entry.delete(0,END)
                
                except Exception as es:
                    messagebox.showerror("Error",f" Error is:{str(es)}")
        else:
            messagebox.showwarning("Warning","Password not matched!!!")
            pass    
       
#==========================================MAIN WINDOW OF APPLICATION==============================================================================        
       
    def Frame5(self):
        self.frame=Frame(self.root,width=550,height=700,bg="#0c0c27")
        self.frame.place(x=0,y=0)
        
        
        #-------------------------------------------------Testing area------------------------------------------------------------------------
        
        self.button1=Button(self.frame,text="Check Yourself",bd=0,fg="#ffff99",activeforeground="#ffff99",bg="#0c0c27",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.check,cursor="hand2")
        self.button1.place(x=130,y=130)
        
        #------------------------------------------------About things you should do in this pandemic------------------------------------------
        
        self.button2=Button(self.frame,text="What to do?",bd=0,fg="#ffff99",bg="#0c0c27",activeforeground="#ffff99",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.what_to_do,cursor="hand2")
        self.button2.place(x=150,y=220)
        
        #----------------------------------------------Go to COVID-19 updater--------------------------------------------------------------
        
        self.button2=Button(self.frame,text="COVID_19 updates",bd=0,fg="#ffff99",bg="#0c0c27",activeforeground="#ffff99",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.covid_update,cursor="hand2")
        self.button2.place(x=110,y=320)
        
        #---------------------------------------------GO ot helplines number----------------------------------------------------------------------
        
        self.button3=Button(self.frame,text="COVID-19\n Helpline number's",bd=0,fg="#ffff99",activeforeground="#ffff99",bg="#0c0c27",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.helpline,cursor="hand2")
        self.button3.place(x=70,y=420)
        
        
        
      
#==============================================COVID-19 TESTING AREA===========================================================================        
    def check(self):
        #------------- defining variable
        
        self.cough=IntVar()
        self.fever=IntVar()
        self.d_in_breath=IntVar()
        self.smell_taste=IntVar()
        self.none=IntVar()
        
        
        #------------------label frame and all the frames involved in the testing questions-------------------------------------------------------------------------------------------
        
        
        self.check_frame=ttk.Labelframe(self.root,text="Covid19 testing Question's", width=550,height=700)
        self.check_frame.place(x=0,y=0)
        
        #--------------frame 1 of testing questions
        
        self.frame=Frame(self.check_frame,bg="#ff471a", width=550,height=700)
        self.frame.place(x=0,y=0)
        self.que1=Label(self.frame,text="Are you experiencing any of the\n following symptoms?",fg="#000d33",activebackground="#00134d",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.que1.place(x=20,y=20)
        self.opt1=Checkbutton(self.frame,text="Cough",variable=self.cough,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",12,"bold"))
        self.opt1.place(x=20,y=70)
        self.opt2=Checkbutton(self.frame,text="Fever",variable=self.fever,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",12,"bold"))
        self.opt2.place(x=140,y=70)
        self.opt3=Checkbutton(self.frame,text="Difficulty in \nBreathing",variable=self.d_in_breath,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",12,"bold"))
        self.opt3.place(x=20,y=140)
        self.opt4=Checkbutton(self.frame,text="Loss of senses of \n smell and taste",variable=self.smell_taste,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",12,"bold"))
        self.opt4.place(x=200,y=140)
        self.opt5=Checkbutton(self.frame,text="None of the above",variable=self.none,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",12,"bold"))
        self.opt5.place(x=20,y=210)
        
        #     Next frame button
        
        self.next_button=Button(self.frame,text="Next",command=self.next_que2,width=18,bd=0,fg="#ffff99",activeforeground="#ffff99",bg="#ff471a",activebackground="#ff471a",font=("Courier New",26,"bold"),cursor="hand2")
        self.next_button.place(x=60,y=310)
        
    def next_que2(self):
        
        #--------------Defining variable
        
        self.diabetes=IntVar()
        self.hypert=IntVar()
        self.lung=IntVar()
        self.heartd=IntVar()
        self.kidneyd=IntVar()
        self.none1=IntVar()
        
        
        self.check_frame=ttk.Labelframe(self.root,text="Covid19 testing Question's", width=550,height=700)
        self.check_frame.place(x=0,y=0)
        
        #___________frame 2 of testing questions
        
        self.frame1=Frame(self.check_frame,bg="#ff471a", width=550,height=700)
        self.frame1.place(x=0,y=0)
        self.que2=Label(self.frame1,text="Have you ever had any of the following?",fg="#000d33",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.que2.place(x=20,y=20)
        self.opt1=Checkbutton(self.frame1,text="Diabetes",variable=self.diabetes,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",15,"bold"))
        self.opt1.place(x=20,y=70)
        self.opt2=Checkbutton(self.frame1,text="Hypertension",variable=self.hypert,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",15,"bold"))
        self.opt2.place(x=140,y=70)
        self.opt3=Checkbutton(self.frame1,text="Lung Disease",variable=self.lung,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",15,"bold"))
        self.opt3.place(x=20,y=140)
        self.opt4=Checkbutton(self.frame1,text="Kideny Disorder",variable=self.kidneyd,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",15,"bold"))
        self.opt4.place(x=200,y=140)
        self.opt5=Checkbutton(self.frame1,text="None of the above",variable=self.none1,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",15,"bold"))
        self.opt5.place(x=20,y=210)
        
        #     -----Next frame button
        
        self.next_button=Button(self.frame1,text="Next",command=self.next_que3,width=18,bd=0,fg="#ffff99",activeforeground="#ffff99",bg="#ff471a",activebackground="#ff471a",font=("Courier New",26,"bold"),cursor="hand2")
        self.next_button.place(x=60,y=310)
        


    def next_que3(self):
        
        #-------------defining variables
        
        self.yes=IntVar()
        self.no=IntVar()
        self.check_frame=ttk.Labelframe(self.root,text="Covid19 testing Question's", width=550,height=700)
        self.check_frame.place(x=0,y=0)
        
        #__________________frame 3 of testing questions
        
        self.frame2=Frame(self.check_frame,bg="#ff471a", width=550,height=700)
        self.frame2.place(x=0,y=0)
        self.que3=Label(self.frame2,text="Have you ever traveled anywhere \n internationally in the last 28-45 days?",fg="#000d33",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.que3.place(x=20,y=20)
        self.opt1=Checkbutton(self.frame2,text="Yes",variable=self.yes,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",15,"bold"))
        self.opt1.place(x=20,y=100)
        self.opt2=Checkbutton(self.frame2,text="No",variable=self.no,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",15,"bold"))
        self.opt2.place(x=20,y=200)
        
        #     --------Next frame button
        
        self.next_button=Button(self.frame2,text="Next",command=self.next_que4,width=18,bd=0,fg="#ffff99",activeforeground="#ffff99",bg="#ff471a",activebackground="#ff471a",font=("Courier New",26,"bold"),cursor="hand2")
        self.next_button.place(x=60,y=300)
        
    def next_que4(self):
        
        #-----------defining variables
        
        self.recent_int=IntVar()
        self.health_care=IntVar()
        self.none2=IntVar()
        
        self.check_frame=ttk.Labelframe(self.root,text="Covid19 testing Question's", width=550,height=700)
        self.check_frame.place(x=0,y=0)
        
        #______________frame 4 of testing questions
        
        self.frame3=Frame(self.check_frame,bg="#ff471a", width=550,height=700)
        self.frame3.place(x=0,y=0)
        self.que3=Label(self.frame3,text="Which of the following apply to you?",fg="#000d33",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.que3.place(x=20,y=20)
        self.opt1=Checkbutton(self.frame3,text="I have recently interacted or lived with\n someone who has tested positive\n for COVID-19.",variable=self.recent_int,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",15,"bold"))
        self.opt1.place(x=20,y=80)
        self.opt2=Checkbutton(self.frame3,text="I am healthcare worker and examined a \nCOVID-19 confirmed case without \nprotective gear",variable=self.health_care,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",15,"bold"))
        self.opt2.place(x=20,y=210)
        self.opt3=Checkbutton(self.frame3,text="None of the above",variable=self.none2,onvalue=1,offvalue=0,fg="#00134d",activebackground="#00134d",bg="#ff471a",font=("Courier New",15,"bold"))
        self.opt3.place(x=20,y=330)
    
        #     _________________________SUBMIT answer BUTTON______________-
        
        self.next_button=Button(self.frame3,text="Submit",command=self.function,width=18,bd=0,fg="#ffff99",activeforeground="#ffff99",bg="#ff471a",activebackground="#ff471a",font=("Courier New",26,"bold"),cursor="hand2")
        self.next_button.place(x=60,y=400)        
        
         #_____________Calculating about your health ststus according to answer given by you_________________________

    def function(self):
        if self.none.get()==1 and self.none1.get()==1 and self.none2.get()==1:
            messagebox.showinfo("Health status", "YOU ARE SAFE")
            messagebox.showinfo("Advice","Please stay safe!")
            self.Frame9()
        elif self.none.get()==1 and (self.diabetes.get()==1 or self.hypert.get()==1 or self.lung.get()==1 or self.heartd.get()==1 or self.kidneyd.get()==1):
            messagebox.showwarning("Health status", "You are not safe")
            self.Frame10()
            
        elif self.none.get() and self.none1.get() and self.yes.get():
            messagebox.showwarning("Health status", "You are not safe")
            self.Frame10()
        
        elif (self.cough.get()==1 or self.fever.get==1 or self.d_in_breath.get()==1 or self.smell_taste.get()==1) and (self.diabetes.get()==1 or self.hypert.get()==1 or self.lung.get()==1 or self.kidneyd.get()==1):
            messagebox.showwarning("Health status","COVID-19 chances")
            self.Frame11()
        elif self.cough.get()==0 and self.fever.get==0 and self.d_in_breath.get()==0 and self.smell_taste.get()==0 and self.none.get()==0 and self.diabetes.get()==0 and self.hypert.get()==0 and self.lung.get()==0 and self.kidneyd.get()==0 and self.none1.get():
            messagebox.showerror("Error", "Sorry, you have not selected any option")
            messagebox.showwarning("Suggestion alert","Try again!")
        elif self.recent_int.get()==1 or self.health_care.get()==1:
             messagebox.showwarning("Health status", "You are not safe")
             self.Frame10()    
        else:
            messagebox.showerror("Error", "Sorry, you have not selected any option")
        
        
    #_______________________--Your health status windows         ===============================================================   
        
    def Frame9(self):
        self.frame=Frame(self.root,width=550,height=700,bg="#0c0c27")
        self.frame.place(x=0,y=0)
        
        self.button1=Button(self.frame,text="Congrats, You are safe!",bd=0,fg="#ffff99",activeforeground="#ffff99",bg="green",activebackground="#0c0c27",font=("Courier New",26,"bold"),cursor="hand2")
        self.button1.place(x=20,y=150)
        
        self.button2=Button(self.frame,text="What to do?",bd=0,fg="#ffff99",bg="#0c0c27",activeforeground="#ffff99",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.what_to_do,cursor="hand2")
        self.button2.place(x=150,y=220)
        
        self.button2=Button(self.frame,text="COVID_19 updates",bd=0,fg="#ffff99",bg="#0c0c27",activeforeground="#ffff99",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.covid_update,cursor="hand2")
        self.button2.place(x=110,y=320)
        
        self.button3=Button(self.frame,text="COVID-19\n Helpline number's",bd=0,fg="#ffff99",activeforeground="#ffff99",bg="#0c0c27",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.helpline,cursor="hand2")
        self.button3.place(x=70,y=420)
        
        
    def Frame10(self):
        self.frame=Frame(self.root,width=550,height=700,bg="#0c0c27")
        self.frame.place(x=0,y=0)
        
        self.button1=Button(self.frame,text="Risk of infection!",bd=0,fg="#ffff99",activeforeground="#ffff99",bg="orange",activebackground="#0c0c27",font=("Courier New",26,"bold"),cursor="hand2")
        self.button1.place(x=70,y=150)
        
        self.button2=Button(self.frame,text="What to do?",bd=0,fg="#ffff99",bg="#0c0c27",activeforeground="#ffff99",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.what_to_do,cursor="hand2")
        self.button2.place(x=150,y=220)
        
        self.button2=Button(self.frame,text="COVID_19 updates",bd=0,fg="#ffff99",bg="#0c0c27",activeforeground="#ffff99",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.covid_update,cursor="hand2")
        self.button2.place(x=110,y=320)
        
        self.button3=Button(self.frame,text="COVID-19\n Helpline number's",bd=0,fg="#ffff99",activeforeground="#ffff99",bg="#0c0c27",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.helpline,cursor="hand2")
        self.button3.place(x=70,y=420)


    def Frame11(self):
        self.frame=Frame(self.root,width=550,height=700,bg="#0c0c27")
        self.frame.place(x=0,y=0)
        
        self.button1=Button(self.frame,text="High risk of infection\n COVID-19 chances",bd=0,fg="#ffff99",activeforeground="#ffff99",bg="red",activebackground="#0c0c27",font=("Courier New",26,"bold"),cursor="hand2")
        self.button1.place(x=40,y=150)
        
        self.button2=Button(self.frame,text="What to do?",bd=0,fg="#ffff99",bg="#0c0c27",activeforeground="#ffff99",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.what_to_do,cursor="hand2")
        self.button2.place(x=150,y=260)
        
        self.button2=Button(self.frame,text="COVID_19 updates",bd=0,fg="#ffff99",bg="#0c0c27",activeforeground="#ffff99",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.covid_update,cursor="hand2")
        self.button2.place(x=110,y=360)
        
        self.button3=Button(self.frame,text="COVID-19\n Helpline number's",bd=0,fg="#ffff99",activeforeground="#ffff99",bg="#0c0c27",activebackground="#0c0c27",font=("Courier New",26,"bold"),command=self.helpline,cursor="hand2")
        self.button3.place(x=70,y=460)   
                
        
        
    
    #---------------------------REDIRECTING TO WEB PAGES----------------------------------------------------------    
        
    #_________________helpline numbers___________________________________________________________________________________
    def helpline(self):
        self.new=1
        url="https://cdnbbsr.s3waas.gov.in/s3850af92f8d9903e7a4e0559a98ecc857/uploads/2020/05/2020050658.pdf"
        webbrowser.open(url,new=self.new)
      
        
      #_________________COVID-19 updater___________________________________________________________________________________
    def covid_update(self):
        self.new=1
        url="https://www.worldometers.info/coronavirus/"
        webbrowser.open(url,new=self.new)
        
        
     #_________________FOLLOW US REDIRECTING AREA___________________________________________________________________________________
        
    def instagram_(self):
        self.new=1
        url="https://www.instagram.com/i_m_s_i_n_g_h_s_a_l_o_k_/"
        webbrowser.open(url,new=self.new)
        
    def facebook_(self):
        self.new=1
        url="https://www.facebook.com/profile.php?id=100004522005722"
        webbrowser.open(url,new=self.new)        
        
    def linkedin_(self):
        self.new=1
        url="https://www.linkedin.com/in/alok-singh-b77a79191/"
        webbrowser.open(url,new=self.new)            
        
    #_____________________________ Working in "What to do" option of main page of application__________________________    
    def what_to_do(self): 
        self.what_to_do_frame=Frame(self.root,width=550,height=700,bg="#ff471a")
        self.what_to_do_frame.place(x=0,y=0)
        self.step1=Label(self.what_to_do_frame,text="What to do in this pandemic situation of \n COVID-19",fg="#000d33",bg="#ff471a",font=("Comic Sans MS",18,"bold"))
        self.step1.place(x=20,y=35)
        self.step1=Label(self.what_to_do_frame,text="1.  Wear face mask",fg="#000d33",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.step1.place(x=20,y=140)
        self.step1=Label(self.what_to_do_frame,text="2.  Do not share towel and utencils",fg="#000d33",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.step1.place(x=20,y=200)        
        self.step1=Label(self.what_to_do_frame,text="3.  Limit contact with others",fg="#000d33",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.step1.place(x=20,y=260)
        self.step1=Label(self.what_to_do_frame,text="4.  Stay in a seperate room",fg="#000d33",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.step1.place(x=20,y=320)
        self.step1=Label(self.what_to_do_frame,text="5.  Isolate yourself",fg="#000d33",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.step1.place(x=20,y=380)
        self.step1=Label(self.what_to_do_frame,text="6.  Log temperature every two hours",fg="#000d33",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.step1.place(x=20,y=440)
        self.step1=Label(self.what_to_do_frame,text="7.  Get youself tested immediately",fg="#000d33",bg="#ff471a",font=("Lucida Console",15,"bold"))
        self.step1.place(x=20,y=500)
        
         #---------------Back to home button----------------------------------
        
        self.back_to_home=Button(self.what_to_do_frame,text="Back to home",width=18,bd=0,fg="#ffff99",activeforeground="#ffff99",bg="#ff471a",activebackground="#ff471a",font=("Courier New",22,"bold"),command=self.Frame5,cursor="hand2")
        self.back_to_home.place(x=120,y=560)
        
        
root=Tk()        
obj=covid19(root)
obj.Frame1()
root.mainloop()
