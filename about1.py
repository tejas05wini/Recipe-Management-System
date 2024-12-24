from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from list import List
from login1 import login_win


class Shop:
    def __init__(self, root):
        self.root = root
        self.title = "Shopping"
        self.geometry = "1750x790+0+0"

        #---------------------------------Upper toolbar  Part------------------------------
        img2 = Image.open(r"F:\Recipe Management System\images\taskbar1.png")
        img2 = img2.resize((1550, 760), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image= self.photoimg2 , bd=4 , relief = RIDGE)
        lblimg2.place(x=0 , y=0, width = 1550 , height = 760)

        #--------------------------------------Background Image ---------------------
        img1 = Image.open(r"F:\Recipe Management System\images1\bg.jpg")
        img1 = img1.resize((1550, 690), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image= self.photoimg1  , relief = RIDGE)
        lblimg1.place(x=0 , y=100, width = 1550 , height = 690)

        #--------------------------Recipeze block----------------------------
        name_frame = Frame(self.root,  relief = RIDGE, background="rosybrown")
        name_frame.place(x=0, y=0, width= 1550, height=100)

        lbl_name = Label(self.root, text = "Shopify", font = ("courier",30,"bold") ,bd=4, bg="rosybrown", fg="white")
        lbl_name.place(x=70, y=19, width = 180, height = 70)

        main_frame = Frame(self.root,  relief = RIDGE, background="rosybrown")
        main_frame.place(x=500, y=20, width= 1200, height=60)


        btn_frame = Frame(main_frame,  relief = RIDGE, bg = "rosybrown")
        btn_frame.place(x=410, y=20, height= 120,width= 1200)


        img3 = Image.open(r"F:\Recipe Management System\images\logo.jpg")
        img3 = img3.resize((60, 60), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.root, image= self.photoimg3  , relief = RIDGE,bd=0)
        lblimg3.place(x=10 , y=20, width = 60 , height = 60)

        start_frame = Frame(self.root, bg = "rosybrown")
        start_frame.place(x= 500, y =200, width = 300, height = 400)

        start_text =(self.root, text = "Welcome to our online shopping platform, designed to offer a seamless and enjoyable experience for all users. Browse a wide range of products across various categories with ease. Our intuitive search functionality helps you find exactly what you're looking for, and personalized recommendations ensure you discover new favorites. With detailed product descriptions, user reviews, and high-quality images, making informed purchasing decisions has never been easier. Enjoy secure checkout options, fast shipping, and reliable customer support for any inquiries or concerns. Start shopping now and experience convenience at its best. ", font = ("Times new roman", 40, "bold"), bg = "rosybrown", fg = "white")
        start_text.grid(row=0, column=0, padx = 30, pady =20)




if __name__ == "__main__":
    root = Tk()
    obj = Shop(root)
    root.mainloop()



