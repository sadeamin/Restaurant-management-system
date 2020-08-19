from tkinter import *
from tkinter import ttk, messagebox
from connection_poll import connection_pool
from psycopg2 import *

class Order_management_system:
    def __init__(self):
        self.top_order = Toplevel()
        self.top_order.title("Order Management")
        self.top_order.geometry("1301x820+250+130")
        self.top_order.resizable(False, False)

        self.heading = ttk.Label(self.top_order, text="Staff Management", foreground="red",
                                 font=("arial", 30, "bold italic"))
        self.heading.pack(padx=300)

        self.treeview = ttk.Treeview(self.top_order, height=32)
        self.treeview.pack()

        self.treeview["columns"] = ("first_name", "last_name", "total_price")
        self.treeview.heading("#0", text="Order Id")
        self.treeview.heading("first_name", text="Staff First Name")
        self.treeview.heading("last_name", text="Staff Last Name")
        self.treeview.heading("total_price", text="Total Price")

        self.treeview.column("#0", width=310)
        self.treeview.column("first_name", width=310)
        self.treeview.column("last_name", width=310)
        self.treeview.column("total_price", width=310)

        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "select id as total, first_name, last_name, total_price from public.order order by total asc")
                for item in list(cursor):
                    self.treeview.insert('', "end", text=f"{item[0]}",
                                         values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        self.treeview.column("#0", anchor="center")
        self.treeview.column("first_name", anchor="center")
        self.treeview.column("last_name", anchor="center")
        self.treeview.column("total_price", anchor="center")

        self.frame_buttons_order = ttk.Frame(self.top_order)
        self.frame_buttons_order.configure(width=1301, height=75)
        self.frame_buttons_order.pack(side="bottom", pady=10)

        self.button_add_order = Button(self.frame_buttons_order, text="Add New Order",
                                       bg="blue",
                                       fg="white", command=self.Add_new_order)
        self.button_add_order.grid(ipadx=30, ipady=20, padx=10)

        self.button_edit_order = Button(self.frame_buttons_order, text="Edit Order", bg="blue", fg="white")
        self.button_edit_order.grid(ipadx=30, ipady=20, row=0, column=1, padx=10)

        self.button_delete_order = Button(self.frame_buttons_order, text="Delete Order", bg="blue", fg="white")
        self.button_delete_order.grid(ipadx=30, ipady=20, row=0, column=2, padx=10)

        self.button_refresh = Button(self.frame_buttons_order, text="   Refresh    ", bg="blue", fg="white",
                                     command=self.refresh)
        self.button_refresh.grid(ipadx=30, ipady=20, row=0, column=3, padx=10)

    def Add_new_order(self):

        self.top_add_new_order = Toplevel()
        self.top_add_new_order.geometry("1301x820+250+130")
        self.top_add_new_order.title("Add New Order")
        self.top_add_new_order.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure("frame.TFrame", background="blue")

        self.heading = ttk.Label(self.top_add_new_order, text="New Order", foreground="red",
                                 font=("arial", 30, "bold italic"))
        self.heading.pack(padx=300)

        self.frame_treeview = ttk.Frame(self.top_add_new_order)
        self.frame_treeview.configure(height=760, width=660)
        self.frame_treeview.pack(side=RIGHT)

        self.treeview_items = ttk.Treeview(self.frame_treeview, height=32)
        self.treeview_items.pack()

        self.treeview_items["columns"] = ("name", "price", "type")
        self.treeview_items.heading("#0", text="Id")
        self.treeview_items.heading("name", text="Name")
        self.treeview_items.heading("price", text="Price")
        self.treeview_items.heading("type", text="Type")

        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu order by total")
                for item in list(cursor):
                    self.treeview_items.insert('', "end", text=f"{item[0]}",
                                               values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        self.treeview_items.column("#0", width=200)
        self.treeview_items.column("name", width=200)
        self.treeview_items.column("price", width=200)
        self.treeview_items.column("type", width=200)

        self.treeview_items.column("#0", anchor="center")
        self.treeview_items.column("name", anchor="center")
        self.treeview_items.column("price", anchor="center")
        self.treeview_items.column("type", anchor="center")

        self.frame_button_a = ttk.Frame(self.frame_treeview)
        self.frame_button_a.configure(height=55, width=660)
        self.frame_button_a.pack()

        self.button_all = Button(self.frame_button_a, bg="blue", text="All", fg="white", command=self.all)
        self.button_all.grid(row=0, column=0, ipady=15, pady=7, padx=10, ipadx=30)

        self.button_main = Button(self.frame_button_a, bg="blue", text="Main", fg="white", command=self.main)
        self.button_main.grid(row=0, column=1, ipady=15, pady=7, padx=10, ipadx=30)

        self.button_drink = Button(self.frame_button_a, bg="blue", text="Drink", fg="white", command=self.drink)
        self.button_drink.grid(row=0, column=2, ipady=15, pady=7, padx=10, ipadx=30)

        self.button_alcohol = Button(self.frame_button_a, bg="blue", text="Alcohol", fg="white", command=self.alcohol)
        self.button_alcohol.grid(row=0, column=3, ipady=15, pady=7, padx=10, ipadx=30)

        self.button_desert = Button(self.frame_button_a, bg="blue", text="Desert", fg="white", command=self.dessert)
        self.button_desert.grid(row=0, column=4, ipady=15, pady=7, padx=10, ipadx=30)

        self.frame_treeview_tow = ttk.Frame(self.top_add_new_order)
        self.frame_treeview_tow.configure(height=760, width=660)
        self.frame_treeview_tow.pack(side=TOP, pady=16)

        self.treeview_order_2 = ttk.Treeview(self.frame_treeview_tow, height=26)
        self.treeview_order_2.pack()

        self.treeview_order_2["columns"] = ("name", "quantity", "price")
        self.treeview_order_2.heading("#0", text="No")
        self.treeview_order_2.heading("name", text="Name")
        self.treeview_order_2.heading("quantity", text="Quantity")
        self.treeview_order_2.heading("price", text="Price")

        self.treeview_order_2.column("#0", width=120)
        self.treeview_order_2.column("name", width=120)
        self.treeview_order_2.column("quantity", width=120)
        self.treeview_order_2.column("price", width=120)

        self.treeview_order_2.column("#0", anchor="center")
        self.treeview_order_2.column("name", anchor="center")
        self.treeview_order_2.column("quantity", anchor="center")
        self.treeview_order_2.column("price", anchor="center")

        self.frame_button_b = ttk.Frame(self.frame_treeview_tow)
        self.frame_button_b.configure(height=300, width=630)
        self.frame_button_b.pack(padx=18)

        self.label_price = ttk.Label(self.frame_button_b, text=f"Total price : {'0'}", font=("arial", 12))
        self.label_price.grid(row=0, column=0, pady=10, sticky=SW)

        self.label_name = ttk.Label(self.frame_button_b, text=f"Staff name : {'Sad eamin'}", font=("arial", 12))
        self.label_name.grid(row=2, column=0, pady=10, sticky=SW)

        self.frame_button_c = ttk.Frame(self.frame_button_b)
        self.frame_button_c.configure(height=55, width=660)
        self.frame_button_c.grid(row=4, column=0, pady=42)

        self.strvar = StringVar()

        self.entry_quantity = ttk.Entry(self.frame_button_c, font=(12), width=10, textvariable=self.strvar)
        self.entry_quantity.grid(row=0, column=0, ipady=20, ipadx=10, padx=10)

        self.button_add = Button(self.frame_button_c, text="Add", bg="blue", fg="white", command=self.Add)
        self.button_add.grid(row=0, column=1, ipady=20, ipadx=25, padx=10)

        self.button_Delete = Button(self.frame_button_c, text="Delete", bg="blue", fg="white",
                                    command=self.Delete_order)
        self.button_Delete.grid(row=0, column=2, ipady=20, ipadx=25, padx=10)

        self.button_Order = Button(self.frame_button_c, text="Order", bg="blue", fg="white", command=self.order)
        self.button_Order.grid(row=0, column=3, ipady=20, ipadx=25, padx=10)

        self.entry_quantity.insert(0, "1")

        self.total_price = 0

    def Delete_order(self):

        self.ci_1 = self.treeview_order_2.focus()

        self.table_value_1 = self.treeview_order_2.item(self.ci_1)

        self.treeview_order_2.detach(self.ci_1)

        self.total_price -= self.table_value_1["values"][2]

        self.label_price = ttk.Label(self.frame_button_b, text=f"Total price : {self.total_price}", font=("arial", 12))
        self.label_price.grid(row=0, column=0, pady=10, sticky=SW)

    def refresh(self):
        self.treeview.delete(*self.treeview.get_children())
        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "select id as total, first_name, last_name, total_price from public.order order by total asc")
                for item in list(cursor):
                    self.treeview.insert('', "end", text=f"{item[0]}",
                                         values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        self.treeview.column("#0", anchor="center")
        self.treeview.column("first_name", anchor="center")
        self.treeview.column("last_name", anchor="center")
        self.treeview.column("total_price", anchor="center")

    def order(self):
        self.msg = messagebox.askyesno("asking", "do you went to place this order ?")

        if self.msg:
            with connection_pool.getconn() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("insert into public.order(first_name, last_name, total_price) values(%s, %s, %s)",
                                   ("Sad", "Eamin", self.total_price))

                    connection.commit()
                    cursor.close()
                    messagebox.showinfo(title="success", message="successfully")

    def Add(self):

        if len(self.strvar.get()) <= 0:
            messagebox.showerror("warning", "Invalid quantity")
        else:
            self.ci_1 = self.treeview_items.focus()

            self.table_value_1 = self.treeview_items.item(self.ci_1)

            self.treeview_order_2.insert("", "end", text=self.table_value_1["text"],
                                         values=(
                                             f"{self.table_value_1['values'][0]} {self.strvar.get()} {self.table_value_1['values'][1] * int(self.strvar.get())}"))

            self.total_price += self.table_value_1['values'][1] * int(self.strvar.get())

            self.label_price = ttk.Label(self.frame_button_b, text=f"Total price : {int(self.total_price)}",
                                         font=("arial", 12))
            self.label_price.grid(row=0, column=0, pady=10, sticky=SW)

            # self.label_price = ttk.Label(self.frame_button_b, text=f"Total price : {self.total_price + self.total_price}", font=("arial", 12))
            # self.label_price.grid(row=0, column=0, pady=10, sticky=SW)
            print(USER_INFO)

    def all(self):
        self.treeview_items.delete(*self.treeview_items.get_children())
        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu order by total")
                for item in list(cursor):
                    self.treeview_items.insert('', "end", text=f"{item[0]}",
                                               values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        self.treeview_items.column("#0", anchor="center")
        self.treeview_items.column("name", anchor="center")
        self.treeview_items.column("price", anchor="center")
        self.treeview_items.column("type", anchor="center")

    def main(self):
        self.treeview_items.delete(*self.treeview_items.get_children())
        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu Where type = 'Main' order by total")
                for item in list(cursor):
                    self.treeview_items.insert('', "end", text=f"{item[0]}",
                                               values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        self.treeview_items.column("#0", anchor="center")
        self.treeview_items.column("name", anchor="center")
        self.treeview_items.column("price", anchor="center")
        self.treeview_items.column("type", anchor="center")

    def drink(self):
        self.treeview_items.delete(*self.treeview_items.get_children())

        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu Where type = 'Drink' order by total")
                for item in list(cursor):
                    self.treeview_items.insert('', "end", text=f"{item[0]}",
                                               values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        self.treeview_items.column("#0", anchor="center")
        self.treeview_items.column("name", anchor="center")
        self.treeview_items.column("price", anchor="center")
        self.treeview_items.column("type", anchor="center")

    def alcohol(self):
        self.treeview_items.delete(*self.treeview_items.get_children())

        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu Where type = 'Alcohol' order by total")
                for item in list(cursor):
                    self.treeview_items.insert('', "end", text=f"{item[0]}",
                                               values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        self.treeview_items.column("#0", anchor="center")
        self.treeview_items.column("name", anchor="center")
        self.treeview_items.column("price", anchor="center")
        self.treeview_items.column("type", anchor="center")

    def dessert(self):
        self.treeview_items.delete(*self.treeview_items.get_children())

        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu Where type = 'Dessert' order by total")
                for item in list(cursor):
                    self.treeview_items.insert('', "end", text=f"{item[0]}",
                                               values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        self.treeview_items.column("#0", anchor="center")
        self.treeview_items.column("name", anchor="center")
        self.treeview_items.column("price", anchor="center")
        self.treeview_items.column("type", anchor="center")
