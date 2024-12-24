from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Maha_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Management System")
        self.root.geometry("1750x790+0+0")

        #---------------variables---------
        self.ID = StringVar()
        self.Name = StringVar()
        self.Category = StringVar()
        self.Ingredients = StringVar()
        self.RecipeDetails = StringVar()
        self.Time = StringVar()        


        #---------------title-----------------
        titlebar = Label(self.root, text = "Add Recipe Details", font = ("times new roman", 40, "bold"), fg = "white", bg = "rosybrown")
        titlebar.place(x=0, y=0, width = 1550, height = 60)

        #---------------logo------------------
        logo = Image.open(r"F:\Recipe Management System\images\chef3.jpeg")
        logo = logo.resize((50, 50),Image.Resampling.LANCZOS)
        self.photologo = ImageTk.PhotoImage(logo)
        lbl_logo = Label(self.root, image = self.photologo, bd = 0)
        lbl_logo.place(x= 5 , y = 5, width = 50, height = 50)

        #---------------label left frame-------
        left_frame = LabelFrame(self.root, text = "Recipe Details", font = ("times new roman", 20, "bold"), bg = "rosybrown", fg = "white")
        left_frame.place(x=0, y=50, width = 500,height = 735)

        #---------------entries inside the left frame--------
        id = Label(left_frame, text = "RecipeID", font = ("times new roman", 15, "bold"), bg = "rosybrown", fg = "black", padx = 4, pady = 10)
        id.grid(row = 0, column = 0, sticky = W)

        id_entry = ttk.Entry(left_frame, width=29, textvariable = self.ID, font = ("times new roman", 15, "bold"))
        id_entry.grid(row = 0, column = 1)

        name = Label(left_frame, text = "RecipeName",  font = ("times new roman", 15, "bold"), bg = "rosybrown", fg = "black", padx = 2, pady = 10)
        name.grid(row = 2, column = 0, sticky = W)

        name_entry = ttk.Entry(left_frame, width=29, textvariable = self.Name, font = ("times new roman", 15, "bold"))
        name_entry.grid(row = 2, column = 1)

        categ = Label(left_frame, text = "Category", font = ("times new roman", 15, "bold"), bg = "rosybrown", fg = "black", padx = 4, pady = 10)
        categ.grid(row = 3, column = 0, sticky = W)

        combo_categ = ttk.Combobox(left_frame, font = ("times new roman", 15, "bold"), textvariable = self.Category, state = DISABLED)
        combo_categ["values"] = ("Italian", "Chinese", "North Indian", "South Indian", "Gujarati", "Maharashtra")
        combo_categ.current(5)
        combo_categ.grid(row = 3, column = 1)

        ingredients = Label(left_frame, text = "Ingredients", font = ("times new roman", 15, "bold"), bg = "rosybrown", fg = "black", padx = 4, pady = 10)
        ingredients.grid(row = 4, column = 0, sticky = W)

        ing_entry = ttk.Entry(left_frame, width=29, textvariable = self.Ingredients, font = ("times new roman", 15, "bold"))
        ing_entry.grid(row = 4, column = 1)

        procedure = Label(left_frame, text = "RecipeDetails", font = ("times new roman", 15, "bold"), bg = "rosybrown", fg = "black", padx = 4, pady = 10)
        procedure.grid(row = 5, column = 0, sticky = W)

        procedure_entry = ttk.Entry(left_frame, width=29, textvariable = self.RecipeDetails, font = ("times new roman", 15, "bold"))
        procedure_entry.grid(row = 5, column = 1)

        time = Label(left_frame, text = "Time", font = ("times new roman", 15, "bold"), bg = "rosybrown", fg = "black", padx = 4, pady = 10)
        time.grid(row = 6, column = 0, sticky = W)

        time_entry = ttk.Entry(left_frame, width=29, textvariable = self.Time, font = ("times new roman", 15, "bold"))
        time_entry.grid(row = 6, column = 1)

        #----------------btnframe---------------------
        btn_frame = Frame(left_frame, bd = 2)
        btn_frame.place(x = 30, y = 600, width = 420, height = 50)

        add = Button(btn_frame, text = "ADD", command = self.add_data, font = ("times new roman", 14, "bold"), bg = "green", fg = "white", width = 8 )
        add.grid(row = 0, column = 0, padx = 3, pady=2)

        delete = Button(btn_frame, text = "DELETE", command = self.delete, font = ("times new roman", 14, "bold"), bg = "green", fg = "white", width = 8 )
        delete.grid(row = 0, column = 1, padx = 3, pady=2)

        update = Button(btn_frame, text = "UPDATE", command = self.update, font = ("times new roman", 14, "bold"), bg = "green", fg = "white", width = 8 )
        update.grid(row = 0, column = 2, padx = 3, pady=2)

        reset = Button(btn_frame, text = "RESET", command=self.reset, font = ("times new roman", 14, "bold"), bg = "green", fg = "white", width = 8 )
        reset.grid(row = 0, column = 3, padx = 3, pady=2)

        #------------------tableframe----------------------
        table_frame = LabelFrame(self.root, text="View Details and Search System", font = ("times new roman", 14, "bold"), fg = "black", bg = "white")
        table_frame.place(x=500,y=60, width = 1020, height = 725)

        search = Label(table_frame, text = "Search By : ", font = ("times new roman", 14, "bold"), fg = "white", bg = "rosybrown")
        search.grid(row = 0, column = 0, padx = 4, pady = 4)

        combo_search = ttk.Combobox(table_frame, font = ("times new roman", 14, "bold"))
        combo_search["values"] = ("Recipe ID", "RecipeName", "Ingredients", "Time", "Category", "Recipe")
        combo_search.grid(row = 0, column = 1, padx = 4, pady = 4)

        search_entry = ttk.Entry(table_frame, width=29, font = ("times new roman", 15, "bold"))
        search_entry.grid(row = 0, column = 2)

        search = Button(table_frame, text = "Search", font = ("times new roman", 14, "bold"), bg = "green", fg = "white", width = 8 )
        search.grid(row = 0, column = 3, padx = 15, pady=2)

        showall = Button(table_frame, text = "Show All", font = ("times new roman", 14, "bold"), bg = "green", fg = "white", width = 8 )
        showall.grid(row = 0, column = 4, padx = 7, pady=2)


        #----------------data table----------------------
        data_frame = Frame(table_frame, bd = 2 )
        data_frame.place(x=10, y=70, width = 990, height = 600)

        scrollx = ttk.Scrollbar(data_frame, orient= HORIZONTAL)
        scrolly = ttk.Scrollbar(data_frame, orient= VERTICAL)

        self.details = ttk.Treeview(data_frame, column = ("id", "name", "category", "ingredients", "procedure", "time"), xscrollcommand = scrollx.set, yscrollcommand = scrolly.set)

        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)

        scrollx.config(command = self.details.xview)
        scrolly.config(command = self.details.yview)

        self.details.heading("id", text = "RecipeID")
        self.details.heading("name", text = "RecipeName")
        self.details.heading("category", text = "Category")
        self.details.heading("ingredients", text = "Ingredients")
        self.details.heading("procedure", text = "RecipeDetails")
        self.details.heading("time", text = "Time")

        self.details["show"] = "headings"

        self.details.column("id", width = 100)
        self.details.column("name", width = 100)
        self.details.column("category", width = 100)
        self.details.column("ingredients", width = 100)
        self.details.column("procedure", width = 100)
        self.details.column("time", width = 100)

       
        self.details.pack(fill = BOTH, expand = 1)
        self.details.bind("<ButtonRelease-1>", self.getcursor)
        self.fetchdata()

    def add_data(self):
        if self.ID.get() == "" or self.Name.get() == "":
            messagebox.showerror(title="Error!", message= "Error, all fields are required.")
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "aish@123", database = "management")
                mycursor = conn.cursor()
                mycursor.execute("Insert into maha values(%s,%s,%s,%s,%s,%s)", (self.ID.get(), 
                                                                                self.Name.get(),
                                                                                self.Category.get(),
                                                                                self.Ingredients.get(),
                                                                                self.RecipeDetails.get(),
                                                                                self.Time.get())
                                )

                messagebox.showinfo(title = "Successful", message = "Success, customer has been added", parent  = self.root)
                conn.commit()
                self.fetchdata()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong : {str(es)}", parent = self.root)

    def fetchdata(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "aish@123", database = "management")
        mycursor = conn.cursor()
        mycursor.execute("select * from maha")
        rows = mycursor.fetchall() #fetch all rows of a query data set
        if len(rows) != 0:
            self.details.delete(*self.details.get_children())
            for i in rows:
                self.details.insert("", END, values = i)
            conn.commit()
        conn.close()

    def getcursor(self, event = ""):
        cursor_row = self.details.focus()
        content = self.details.item(cursor_row) 
        row = content["values"]

        self.ID.set(row[0])
        self.Name.set(row[1])
        self.Category.set(row[2])
        self.Ingredients.set(row[3])
        self.RecipeDetails.set(row[4])
        self.Time.set(row[5])
        

    def update(self):
        if self.Category.get() == "":
            messagebox.showerror(message = "Error, all fields are mandatory.")
        else:    
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "aish@123", database = "management")
            mycursor = conn.cursor()
            mycursor.execute("update maha set RecipeName = %s, Category = %s, Ingredients = %s, RecipeDetails = %s, Time = %s where RecipeId = %s",(
                                                                                                                                                    self.Name.get(),
                                                                                                                                                    self.Category.get(),
                                                                                                                                                    self.Ingredients.get(),
                                                                                                                                                    self.RecipeDetails.get(),
                                                                                                                                                    self.Time.get(),
                                                                                                                                                    self.ID.get()) )
            conn.commit()
            self.fetchdata()
            conn.close()
            messagebox.showinfo(title = "Successful", message = "Recipe Details have been added successfully.", parent = self.root)

    def delete(self):
        mdelete = messagebox.askyesno(title = "Recipe Management system", message = "Do you want to delete this recipe ? ", parent = self.root)
        if mdelete > 0: 
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "aish@123", database = "management")
            mycursor = conn.cursor()
            query = "delete from maha where RecipeId = %s"
            value = (self.ID.get(),)
            mycursor.execute(query, value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetchdata()
        conn.close()
                
    def reset(self):
        self.ID.set("")
        self.Name.set("")
        #self.Category.set("")
        self.Ingredients.set("")
        self.RecipeDetails.set("")
        self.Time.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Maha_Window(root)
    root.mainloop()