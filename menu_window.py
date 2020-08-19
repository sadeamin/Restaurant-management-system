# from login_window import Menu_window
from tkinter import Toplevel, ttk, Button
from psycopg2 import *
from connection_poll import connection_pool

N='n'
S='s'
W='w'
E='e'
# print(USER_INFO)
def Menu_window():
    top = Toplevel()
    top.title("Show Menu")
    top.geometry("1301x840+250+130")
    top.resizable(False, False)

    main_heading = ttk.Label(top, text="Restaurant Management System", foreground="red",
                             font=("arial", 30, "bold italic"))
    main_heading.pack(padx=60, pady=30)

    # creating the treeview

    tv = ttk.Treeview(top, height=30)
    tv.pack()
    tv["columns"] = ("name", "price", "type")
    tv.heading("#0", text="Id")
    tv.heading("name", text="Name")
    tv.heading("price", text="Price")
    tv.heading("type", text="Type")

    tv.column("#0", width=310)
    tv.column("name", width=310)
    tv.column("price", width=310)
    tv.column("type", width=310)

    with connection_pool.getconn() as connection:
        with connection.cursor() as cursor:
            cursor.execute("select id as total, name, price, type from menu order by total")
            for item in list(cursor):
                tv.insert('', "end", text=f"{item[0]}", values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))


    tv.column("#0", anchor="center")
    tv.column("name", anchor="center")
    tv.column("price", anchor="center")
    tv.column("type", anchor="center")

    style = ttk.Style()
    style.configure("1.TFrame")

    frame_buttons = ttk.Frame(top)
    frame_buttons.configure(width=700, height=80, style="1.TFrame")
    frame_buttons.pack(pady=20)


    def all():
        tv.delete(*tv.get_children())
        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu order by total")
                for item in list(cursor):
                    tv.insert('', "end", text=f"{item[0]}", values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        tv.column("#0", anchor="center")
        tv.column("name", anchor="center")
        tv.column("price", anchor="center")
        tv.column("type", anchor="center")

    def main():
        tv.delete(*tv.get_children())
        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu Where type = 'Main' order by total")
                for item in list(cursor):
                    tv.insert('', "end", text=f"{item[0]}", values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        tv.column("#0", anchor="center")
        tv.column("name", anchor="center")
        tv.column("price", anchor="center")
        tv.column("type", anchor="center")


    def drink():
        tv.delete(*tv.get_children())

        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu Where type = 'Drink' order by total")
                for item in list(cursor):
                    tv.insert('', "end", text=f"{item[0]}", values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        tv.column("#0", anchor="center")
        tv.column("name", anchor="center")
        tv.column("price", anchor="center")
        tv.column("type", anchor="center")

    def alcohol():
        tv.delete(*tv.get_children())

        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu Where type = 'Alcohol' order by total")
                for item in list(cursor):
                    tv.insert('', "end", text=f"{item[0]}", values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        tv.column("#0", anchor="center")
        tv.column("name", anchor="center")
        tv.column("price", anchor="center")
        tv.column("type", anchor="center")

    def dessert():
        tv.delete(*tv.get_children())

        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu Where type = 'Dessert' order by total")
                for item in list(cursor):
                    tv.insert('', "end", text=f"{item[0]}", values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        tv.column("#0", anchor="center")
        tv.column("name", anchor="center")
        tv.column("price", anchor="center")
        tv.column("type", anchor="center")


    button_all = Button(frame_buttons, text="All", bg="blue", fg="#FFD5C6", height=3, width=15, command=all)
    button_main = Button(frame_buttons, text="Main", bg="blue", fg="#FFD5C6", height=3, width=15, command=main)
    button_drink = Button(frame_buttons, text="Drink", bg="blue", fg="#FFD5C6", height=3, width=15, command=drink)
    button_alcohol = Button(frame_buttons, text="Alcohol", bg="blue", fg="#FFD5C6", height=3, width=15, command=alcohol)
    button_dessert = Button(frame_buttons, text="Dessert", bg="blue", fg="#FFD5C6", height=3, width=15, command=dessert)

    button_all.grid(row=0, column=0, padx=10, ipadx=10)
    button_main.grid(row=0, column=1, padx=10, ipadx=10)
    button_drink.grid(row=0, column=2, padx=10, ipadx=10)
    button_alcohol.grid(row=0, column=3, padx=10, ipadx=10)
    button_dessert.grid(row=0, column=4, padx=10, ipadx=10)
