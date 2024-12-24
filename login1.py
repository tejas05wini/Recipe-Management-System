from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox



class register:
    def __init__(self,root):
        self.root=root
        self.root.title("New Registration")
        self.root.geometry("1550x790+0+0")

        #-----------------------variables--------------------
        self.fname=StringVar()
        self.lname=StringVar()
        self.contact=StringVar()
        self.email=StringVar()
        self.securityQ=StringVar()
        self.securityA=StringVar()
        self.pas=StringVar()
        self.confpas=StringVar()
       

        #----------------------------------REGISTER BACKGROUND IMG--------------------
        img1 = Image.open(r"F:\Recipe Management System\images1\bg.jpg")
        img1 = img1.resize((1550, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img1)
        labelimg = Label(self.root, image = self.photoimg, bd = 4)
        labelimg.place(x=0, y=0, height = 780, width = 1550)

        #------------------------MAIN FRAME--------------------------
        frame=Frame(self.root,bg="Rosybrown")
        frame.place(x=665,y=40,width=800,height=580)

        register_lbl=Label(frame,text="REGISTER HERE ",font=("times new roman",25,"bold"),fg="black",bg="Rosybrown")
        register_lbl.place(x=40,y=20)

        #-----------------------------------LABEL AND ENTRY----------------------
        fname=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="Rosybrown")
        fname.place(x=40,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.fname,font=("times new roman",20,"bold"))
        fname_entry.place(x=40,y=140,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",20,"bold"),bg="Rosybrown")
        lname.place(x=400,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.lname,font=("times new roman",20))
        self.txt_lname.place(x=400,y=140,width=250)

        contact=Label(frame,text="Contact no",font=("times new roman",20,"bold"),bg="Rosybrown")
        contact.place(x=40,y=180)

        self.txt_contact=ttk.Entry(frame,textvariable=self.contact,font=("times new roman",20))
        self.txt_contact.place(x=40,y=220)

        email=Label(frame,text="Email id",font=("times new roman",20,"bold"),bg="Rosybrown")
        email.place(x=400,y=180)

        self.txt_email=ttk.Entry(frame,textvariable=self.email,font=("times new roman",20))
        self.txt_email.place(x=400,y=220)

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",20,"bold"),bg="Rosybrown")
        security_Q.place(x=40,y=260)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.securityQ,font=("times new roman",20,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girld Friend Name","Your Pet Name")
        self.combo_security_Q.place(x=40,y=300,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",20,"bold"),bg="rosybrown")
        security_A.place(x=400,y=260)

        self.txt_security=ttk.Entry(frame,textvariable=self.securityA,font=("times new roman",20))
        self.txt_security.place(x=400,y=300,width=250)

        pswd=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="rosybrown")
        pswd.place(x=40,y=350)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.pas,font=("times new roman",20))
        self.txt_pswd.place(x=40,y=390,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="rosybrown")
        confirm_pswd.place(x=400,y=350)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.confpas,font=("times new roman",20))
        self.txt_confirm_pswd.place(x=400,y=390,width=250)

        self.check=IntVar()
        Checkbtn=Checkbutton(frame,variable=self.check,text="I Agree The Terms and Conditions",font=("times new roman",20,"bold"),bg="rosybrown",onvalue=1,offvalue=0)
        Checkbtn.place(x=40,y=440)

#-----------------------------------------Buttons ---------------------------------------
        b1=Button(frame,text="Register Now",command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",20,"bold"),bg="white")
        b1.place(x=50,y=500,width=200)

        b2=Button(frame,borderwidth=0,text="Login", command=self.login1,cursor="hand2",font=("times new roman",20,"bold"),bg="white")
        b2.place(x=370,y=500,width=170)

    #------------------------FUNCTION DECLARATION--------------------------------
    def login1(self):
        self.new_window = Toplevel(self.root)
        self.obj = login_win(self.new_window)


    def register_data(self):
        if self.fname.get()=="" or self.email.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.pas.get() != self.confpas.get():
            messagebox.showerror("Error","Password and Confirm Password must be same ")
        elif self.check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions ")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="aish@123",database="management")
            mycursor=conn.cursor()
            
            mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.fname.get(),
                                                                                        self.lname.get(),
                                                                                        self.contact.get(),
                                                                                        self.email.get(),
                                                                                        self.securityQ.get(),
                                                                                        self.securityA.get(),
                                                                                        self.pas.get()
                                                                
                                                                                ))


            conn.commit()
            conn.close()
            messagebox.showinfo("Success ","Register successfully!")


class login_win:

    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")



        #----------------------------------LOGIN BACKGROUND IMG--------------------
        img1 = Image.open(r"F:\Recipe Management System\images1\bg.jpg")
        img1 = img1.resize((1550, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img1)
        labelimg = Label(self.root, image = self.photoimg, bd = 4)
        labelimg.place(x=0, y=0, height = 800, width = 1550)

        #--------------------------------LOGIN FRAME---------------------------------
        frame=Frame(self.root,bg="Rosybrown")
        frame.place(x=900,y=50,width=450,height=500)

        #----------------------------CHEF LOGO-------------------------------------
        img2 = Image.open(r"F:\Recipe Management System\images\chef3.jpeg")
        img2 = img2.resize((160, 160), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img2)
        labelimg1 = Label(self.root, image = self.photoimg1, bd = 0)
        labelimg1.place(x=1070, y=60, height = 140, width = 120)

        #--------------------------GET STARTED------------------------------------
        get_str=Label(frame,text="Get Started",font=("times new roman",22,"bold"),fg="White",bg="Rosybrown")
        get_str.place(x=150,y=150,)
   
        #-------------------------USER NAME LABEL-----------------------------------
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="White",bg="Rosybrown")
        username.place(x=80,y=190)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=50,y=220,width=310,height=30)

         #-------------------------PASSWORD LABEL-----------------------------------
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="White",bg="Rosybrown")
        password.place(x=80,y=270,)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=50,y=300,width=310,height=30)

        #-------------------------LABEL LOGO-----------------------------
        img3 = Image.open(r"F:\Recipe Management System\images\username.jpeg")
        img3 = img3.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img3)
        labelimg2 = Label(self.root, image = self.photoimg2, bd = 0,bg="Rosybrown",borderwidth=0)
        labelimg2.place(x=945, y=240, height = 25, width = 25)

        img4 = Image.open(r"F:\Recipe Management System\images\password.jpeg")
        img4 = img4.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img4)
        labelimg3 = Label(self.root, image = self.photoimg3, bd = 0,bg="Rosybrown",borderwidth=0)
        labelimg3.place(x=945, y=320, height = 25, width = 25)

        #----------------------------LOGIN BUTTON---------------------------------
        
        loginbtn=Button(frame,text="Login", command = self.login1, font=("times new roman",15,"bold"),bd=3,fg="Black",relief=RIDGE,bg="White",activeforeground="white")
        loginbtn.place(x=150,y=350,width=120,height=40)

        #----------------------------REGISTRATION BUTTON---------------------------------
        registerbtn=Button(frame,text="New User Register",command=self.register1,font=("times new roman",14,"bold"),borderwidth=0,fg="Black",relief=RIDGE,bg="Rosybrown",activeforeground="white",activebackground="Rosybrown")
        registerbtn.place(x=20,y=400,width=160)

        #----------------------------FORGOT PASSWORD BUTTON---------------------------------
        forgotpassbtn=Button(frame,text="Forgot Password",font=("times new roman",14,"bold"),borderwidth=0,fg="Black",relief=RIDGE,bg="Rosybrown",activeforeground="white",activebackground="Rosybrown")
        forgotpassbtn.place(x=15,y=430,width=160)
    
        
    def login1(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="aish" and self.txtpass.get()=="123":
            messagebox.showinfo("Success","Welcome to Recipe Management System")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="aish@123",database="management")
            mycursor=conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s", (
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
            ))  
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror(message="Invalid username or password")
        else:
            open_main = messagebox.askyesno("YesNo", "Access only admin")
            if open_main > 0:
                self.new_window = Toplevel(self.root)
                self.obj = RecipeManagementSys(self.new_window)
            else:
                if not open_main:
                    return 
        conn.commit()
        conn.close()




    def register1(self):
        self.new_window = Toplevel(self.root)
        self.obj = register(self.new_window)

    def front(self):
        self.new_window = Toplevel(self.root)
        self.obj = RecipeManagementSys(self.new_window)
   
    #def RecipeManagementSys(self):
     #   self.new_window = Toplevel(self.root)
      #  self.obj =RecipeManagementSys(self.new_window)
   
    
if __name__ == "__main__":
    root = Tk()
    app = login_win(root)
    root.mainloop()
