from tkinter import * 
from italian import Italian_Window
from chinese import Chinese_Window
from north import North_Window
from south import South_Window
from maha import Maha_Window
from gujarati import Gujarati_Window
from PIL import Image, ImageTk


class Category_Window:
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
        img1 = Image.open(r"F:\Recipe Management System\images\italian.jpeg")
        img1 = img1.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        label_img1 = Label(self.root, image = self.photoimg1, bd = 0)
        label_img1.place(x = 110, y = 100, height = 250, width = 350)

        #----------------chinese-------------------------------
        img2 = Image.open(r"F:\Recipe Management System\images\chinese.jpeg")
        img2 = img2.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        label_img2 = Label(self.root, image = self.photoimg2, bd = 0)
        label_img2.place(x = 570, y = 100, height = 250, width = 350)

        #----------------north-------------------------------
        img3 = Image.open(r"F:\Recipe Management System\images\north_indian.jpeg")
        img3 = img3.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        label_img3 = Label(self.root, image = self.photoimg3, bd = 0)
        label_img3.place(x = 1030, y = 100, height = 250, width = 350)
        

        #--------------south------------------------------
        img4 = Image.open(r"F:\Recipe Management System\images\south_indian.jpeg")
        img4 = img4.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        label_img4 = Label(self.root, image = self.photoimg4, bd = 0)
        label_img4.place(x = 110, y = 450, height = 250, width = 350)


        #----------------gujju-------------------------------
        img5 = Image.open(r"F:\Recipe Management System\images\gujarati.jpeg")
        img5 = img5.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        label_img5 = Label(self.root, image = self.photoimg5, bd = 0)
        label_img5.place(x = 570, y = 450, height = 250, width = 350)

        #----------------maharashtra-------------------------------
        img6 = Image.open(r"F:\Recipe Management System\images\maharashtra.jpeg")
        img6 = img6.resize((350, 250), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        label_img6 = Label(self.root, image = self.photoimg6, bd = 0)
        label_img6.place(x = 1030, y = 450, height = 250, width = 350)


        #----------------buttons------------------------------
        btn1 = Button(self.root, text = "Italian", command = self.italian, font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0, fg = "black")
        btn1.place(x  = 200, y = 370, width = 170, height = 40)

        btn2 = Button(self.root, text = "Chinese", command = self.chinese, font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0, fg = "black")
        btn2.place(x  = 650, y = 370, width = 170, height = 40)

        btn3 = Button(self.root, text = "North Indian", command = self.north, font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0, fg = "black")
        btn3.place(x  = 1090, y = 370, width = 220, height = 40)

        btn4 = Button(self.root, text = "South Indian", command = self.south, font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0, fg = "black")
        btn4.place(x  = 180, y = 720, width = 220, height = 40)

        btn5 = Button(self.root, text = "Gujarati", command = self.gujarati, font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0, fg = "black")
        btn5.place(x  = 650, y = 720, width = 170, height = 40)

        btn6 = Button(self.root, text = "Maharashtra", command = self.maha, font = ("Edu Australia VIC WA NT Hand", 18, "bold"), bd = 0,fg = "black")
        btn6.place(x  = 1090, y = 720, width = 220, height = 40)

    def italian(self):
        self.new_window = Toplevel(self.root)
        self.obj = Italian_Window(self.new_window)

    def chinese(self):
        self.new_window = Toplevel(self.root)
        self.obj = Chinese_Window(self.new_window)

    def north(self):
        self.new_window = Toplevel(self.root)
        self.obj = North_Window(self.new_window)

    def south(self):
        self.new_window = Toplevel(self.root)
        self.obj = South_Window(self.new_window)

    def maha(self):
        self.new_window = Toplevel(self.root)
        self.obj = Maha_Window(self.new_window)

    def gujarati(self):
        self.new_window = Toplevel(self.root)
        self.obj = Gujarati_Window(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Category_Window(root)
    root.mainloop()