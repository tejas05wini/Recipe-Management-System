from tkinter import *
from PIL import Image,ImageTk

class Customer_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Management System")
        self.root.geometry("1550x770+0+0")

        #-----------------title------------------------
        title = Label(self.root, text = "Customer Details", bg = "green", fg="white", font = ("times new roman", 20, "bold"))
        title.place(x = 0, y = 0, width = 1550, height = 50)

        #----------------logo--------------------------
        
    
if __name__ == "__main__":
    root = Tk()
    obj = Customer_window(root)
    root.mainloop()