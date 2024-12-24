from tkinter import *
from login import login_win
from PIL import Image,ImageTk
from tkinter import ttk
from category import Category_Window
import matplotlib.font_manager



class RecipeManagementSys:
    def __init__(self, root):
        self.root=root
        self.root.title("Recipe Management System")
        self.root.geometry("1750x790+0+0")

        #---------------------------------Upper toolbar  Part------------------------------
        img2 = Image.open(r"F:\Recipe Management System\images\taskbar1.png")
        img2 = img2.resize((1550, 760), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image= self.photoimg2 , bd=4 , relief = RIDGE)
        lblimg2.place(x=0 , y=0, width = 1550 , height = 760)

        #--------------------------------------Background Image ---------------------
        img1 = Image.open(r"F:\Recipe Management System\images\wall1.jpeg")
        img1 = img1.resize((1550, 690), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image= self.photoimg1  , relief = RIDGE)
        lblimg1.place(x=0 , y=100, width = 1550 , height = 690)

        #--------------------------Recipeze block----------------------------
        name_frame = Frame(self.root,  relief = RIDGE, background="rosybrown")
        name_frame.place(x=0, y=0, width= 1550, height=100)

        lbl_name = Label(self.root, text = "Recipeze", font = ("courier",30,"bold") ,bd=4, bg="rosybrown", fg="white")
        lbl_name.place(x=70, y=19, width = 180, height = 70)

        main_frame = Frame(self.root,  relief = RIDGE, background="rosybrown")
        main_frame.place(x=500, y=20, width= 1200, height=60)


        btn_frame = Frame(main_frame,  relief = RIDGE, bg = "rosybrown")
        btn_frame.place(x=410, y=20, height= 120,width= 1200)

        #---------------------------Menu Button----------------------------
        home_btn = Button(btn_frame, text = "Home", command=self.home1,  font = ("times new roman",20,"bold"), bg="salmon", fg="black", cursor="hand1" )
        home_btn.grid(row = 0, column = 1, padx = 8)

        #---------------------------Recipe  Button----------------------------
        recipes_btn = Button(btn_frame, text = "Recipe", font = ("times new roman",20,"bold"),bg="salmon", fg="black", cursor="hand1" )
        recipes_btn.grid(row = 0, column = 2, padx = 8)

        #---------------------------Details Button----------------------------
        details_btn = Button(btn_frame, text = "Details", font= ("times new roman",20,"bold"), bg="salmon", fg="black", cursor="hand1" )
        details_btn.grid(row = 0, column = 3, padx = 8)

        #---------------------------Report Button----------------------------
        aboutus_btn = Button(btn_frame, text = "About Us", font = ("times new roman",20,"bold"), bg="salmon", fg="black", cursor="hand1" )
        aboutus_btn.grid(row = 0, column = 4, padx = 8)

        #---------------------------Logout Button----------------------------
        logout_btn = Button(btn_frame, text = "Logout", command=self.login_func, font = ("times new roman",20,"bold"), bg="salmon", fg="black", cursor="hand1" )
        logout_btn.grid(row = 0, column = 5, pady = 0)


        img3 = Image.open(r"F:\Recipe Management System\images\logo.jpg")
        img3 = img3.resize((60, 60), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.root, image= self.photoimg3  , relief = RIDGE,bd=0)
        lblimg3.place(x=10 , y=20, width = 60 , height = 60)

        #bigtext = Label(self.root, text = "All In One\n Recipe\n Manager", font = ("verdana", 50, "bold"), fg = "white", bg="rosybrown")
        #bigtext.place(x = 800, y = 300, width = 600, height = 300)

        #-----------------Get started----------------
        start_frame = Frame(self.root, bg = "rosybrown")
        start_frame.place(x= 500, y =200, width = 300, height = 400)

        start_text = Label(start_frame, text = "All In One\n Recipe\n Manager", font = ("Times new roman", 40, "bold"), bg = "rosybrown", fg = "white")
        start_text.grid(row=0, column=0, padx = 30, pady =20)

        #---------------------get started button-----------------------
        getstart=Button(start_frame,text="Get Started",command=self.category,font=("times new roman",14,"bold"),borderwidth=0,fg="black",relief=RIDGE,bg="white",activeforeground="white",activebackground="Red")
        getstart.place(x=65,y=250,width=160, height = 70)

    def category(self):
        self.new_window=Toplevel(self.root)
        self.app=Category_Window(self.new_window)

    def home1(self):
        self.new_window = Toplevel(self.root)
        self.obj = RecipeManagementSys(self.new_window)

    def login_func(self):
        from login import login_win
        self.new_window = Toplevel(self.root)
        self.obj = login_win(self.new_window)

     
       
if __name__ == "__main__":
    root = Tk()
    obj=RecipeManagementSys(root)
    root.mainloop()