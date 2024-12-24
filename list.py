from tkinter import * 

from PIL import Image, ImageTk


class List:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Management System")
        self.root.geometry("1550x790+0+0")

        msg = Label(self.root, text = "Pick one category!", bd = 0, fg = "black", font = ("Edu Australia VIC WA NT Hand", 20, "bold"))
        msg.place(x = 650, y = 10)

        #----------------background image--------------------
        background = Image.open(r"F:\Recipe Management System\images\bg11.jpg")
        background = background.resize((1550, 1550), Image.Resampling.LANCZOS)
        self.photoback = ImageTk.PhotoImage(background)
        label_background = Label(self.root, image = self.photoback, bd = 0)
        label_background.place(x = 0, y = 60, height = 1550, width = 1550)

        #----------------italian-----------------------------------
        img1 = Image.open(r"F:\Recipe Management System\images1\women.jpg")
        img1 = img1.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        label_img1 = Label(self.root, image = self.photoimg1, bd = 0)
        label_img1.place(x = 110, y = 100, height = 250, width = 350)

        #----------------chinese-------------------------------
        img2 = Image.open(r"F:\Recipe Management System\images1\men.jpg")
        img2 = img2.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        label_img2 = Label(self.root, image = self.photoimg2, bd = 0)
        label_img2.place(x = 570, y = 100, height = 250, width = 350)

        #----------------north-------------------------------
        img3 = Image.open(r"F:\Recipe Management System\images1\kids.jpg")
        img3 = img3.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        label_img3 = Label(self.root, image = self.photoimg3, bd = 0)
        label_img3.place(x = 1030, y = 100, height = 250, width = 350)
        

        #--------------south------------------------------
        img4 = Image.open(r"F:\Recipe Management System\images1\acc.jpg")
        img4 = img4.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        label_img4 = Label(self.root, image = self.photoimg4, bd = 0)
        label_img4.place(x = 110, y = 450, height = 250, width = 350)


        #----------------gujju-------------------------------
        img5 = Image.open(r"F:\Recipe Management System\images1\footwear.jpg")
        img5 = img5.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        label_img5 = Label(self.root, image = self.photoimg5, bd = 0)
        label_img5.place(x = 570, y = 450, height = 250, width = 350)

        #----------------maharashtra-------------------------------
        img6 = Image.open(r"F:\Recipe Management System\images1\beauty.jpg")
        img6 = img6.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        label_img6 = Label(self.root, image = self.photoimg6, bd = 0)
        label_img6.place(x = 1030, y = 450, height = 250, width = 350)


        #----------------buttons------------------------------
        btn1 = Button(self.root, text = "Womens", font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0, fg = "black")
        btn1.place(x  = 200, y = 370, width = 170, height = 40)

        btn2 = Button(self.root, text = "Mens",  font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0, fg = "black")
        btn2.place(x  = 650, y = 370, width = 170, height = 40)

        btn3 = Button(self.root, text = "Kids",  font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0, fg = "black")
        btn3.place(x  = 1090, y = 370, width = 220, height = 40)

        btn4 = Button(self.root, text = "Accessories",  font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0, fg = "black")
        btn4.place(x  = 180, y = 720, width = 220, height = 40)

        btn5 = Button(self.root, text = "Footwear",  font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0, fg = "black")
        btn5.place(x  = 650, y = 720, width = 170, height = 40)

        btn6 = Button(self.root, text = "Beuaty and Care",  font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0,fg = "black")
        btn6.place(x  = 1090, y = 720, width = 220, height = 40)



if __name__ == "__main__":
    root = Tk()
    obj = List(root)
    root.mainloop()