# from login_window import Menu_window
from tkinter import Toplevel, ttk, Text
from connection_poll import connection_pool
from tkinter import messagebox
from psycopg2 import *
from tkinter import *



def Manage_menu_window():
    top = Toplevel()
    top.title("Show Menu")
    top.geometry("1301x820+250+130")
    top.resizable(False, False)

    main_heading = ttk.Label(top, text="Restaurant Management System", foreground="red",
                             font=("arial", 30, "bold italic"))
    main_heading.pack(padx=300)

    tv = ttk.Treeview(top, height=32)
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
            cursor.execute("select id as total, name, price, type from menu order by total asc")
            for item in list(cursor):
                tv.insert('', "end", text=f"{item[0]}", values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

    tv.column("#0", anchor="center")
    tv.column("name", anchor="center")
    tv.column("price", anchor="center")
    tv.column("type", anchor="center")


    frame_buttons = ttk.Frame(top)
    frame_buttons.configure(width=1301, height=75)
    frame_buttons.pack(side="bottom", pady=10)


    def edit():
        ci = tv.focus()
        table_value = tv.item(ci)
        top_1 = Toplevel()
        top_1.title("Add New Menu Item")
        top_1.geometry("620x495+550+230")
        top_1.resizable(False, False)

        label_id = ttk.Label(top_1,
                             text="Menu Item Id :                     "
                                  "                                                   ",
                             font=("arial", 15))
        label_id.pack(pady=5)

        strvar1 = StringVar()

        entry_id = Entry(top_1, width=50, font=("arial", 15), textvariable=strvar1)
        entry_id.pack(pady=20)
        entry_id.insert(0, table_value['text'])
        entry_id.config(state="disable")
        # entry_id.state(["disabled"])

        label_id = ttk.Label(top_1,
                             text="Menu Item Name :                                                                  ",
                             font=("arial", 15))
        label_id.pack(pady=5)

        strvar2 = StringVar()

        entry_name = Entry(top_1, width=50, font=("arial", 15), textvariable=strvar2)
        entry_name.insert(0, table_value['values'][0])
        entry_name.pack(pady=20)

        label_id = ttk.Label(top_1,
                             text="Menu Item Price :                                                                   ",
                             font=("arial", 15))
        label_id.pack(pady=5)

        strvar3 = StringVar()

        entry_price = Entry(top_1, width=50, font=("arial", 15), textvariable=strvar3)
        entry_price.insert(0, table_value['values'][1])
        entry_price.pack(pady=20)

        label_id = ttk.Label(top_1,
                             text="type :                                                               "
                                  "                  "
                                  "   ", font=("arial", 15))
        label_id.pack(pady=5)

        combobox_type = ttk.Combobox(top_1, width=48, font=("arial", 15))
        combobox_type.config(value=["Main", "Drink", "Alcohol", "Dessert"])
        combobox_type.insert(0, table_value['values'][2])
        combobox_type.state(["readonly"])
        combobox_type.pack(pady=15)

        style = ttk.Style()
        style.configure(style="frame.TFrame", background="blue")

        frame_buttons_1 = ttk.Frame(top_1)
        frame_buttons_1.configure(width=550, height=60)
        frame_buttons_1.pack()

        def Update():
            popup = messagebox.askyesno(title="asking", message="Do you went to update this item")
            if popup:
                if len(entry_id.get()) == 0 or \
                        len(entry_name.get()) == 0 or \
                        len(entry_price.get()) == 0 or len(combobox_type.get()) == 0:
                    messagebox.showerror("warning", "text boxes empty please fill it.")

                else:
                    with connection_pool.getconn() as connection:
                        with connection.cursor() as cursor:
                            cursor.execute("Update menu set name=%s, price=%s, type=%s Where id=%s",
                                           (entry_name.get(),
                                            entry_price.get(), combobox_type.get(), entry_id.get()))

                            connection.commit()
                            cursor.close()
                            messagebox.showinfo(title="success", message="successfully")

        def cancel():
            top_1.destroy()

        button_save1 = Button(frame_buttons_1, text="Save", bg="blue", fg="#FFD5C6", height=3, width=15, command=Update)
        button_save1.grid(row=0, column=0, padx=40, ipadx=20, ipady=10)
        button_cancel = Button(frame_buttons_1, text="Cancel", bg="blue", fg="#FFD5C6", height=3, width=15, command=cancel)
        button_cancel.grid(row=0, column=1, padx=40, ipadx=20, ipady=10)

    def refresh():
        tv.delete(*tv.get_children())
        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, name, price, type from menu order by total asc")
                for item in list(cursor):
                    tv.insert('', "end", text=f"{item[0]}", values=(f'{item[1]}', f'{item[2]}', f'{item[3]}'))

        tv.column("#0", anchor="center")
        tv.column("name", anchor="center")
        tv.column("price", anchor="center")
        tv.column("type", anchor="center")

    def delete():
        ci = tv.focus()
        table_value = tv.item(ci)
        popup = messagebox.askyesno(title="asking", message="Do you went to delete this item")
        if popup:
            with connection_pool.getconn() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("delete from menu Where id=%s", (table_value['text'],))

    def Add_new_item():
        top_1 = Toplevel()
        top_1.title("Edit New Menu Item")
        top_1.geometry("620x495+550+230")
        top_1.resizable(False, False)

        label_id = ttk.Label(top_1,
                             text="Menu Item Id :                                                                        ", font=("arial", 15))
        label_id.pack(pady=5)

        strvar1 = StringVar()

        entry_id = ttk.Entry(top_1, width=50, font=("arial", 15), textvariable=strvar1)
        entry_id.pack(pady=20)

        label_id = ttk.Label(top_1,
                             text="Menu Item Name :                                                                  ", font=("arial", 15))
        label_id.pack(pady=5)

        strvar2 = StringVar()

        entry_name = ttk.Entry(top_1, width=50, font=("arial", 15), textvariable=strvar2)
        entry_name.pack(pady=20)

        label_id = ttk.Label(top_1,
                             text="Menu Item Price :                                                                   ", font=("arial", 15))
        label_id.pack(pady=5)

        strvar3 = StringVar()

        entry_price = ttk.Entry(top_1, width=50, font=("arial", 15), textvariable=strvar3)
        entry_price.pack(pady=20)


        label_id = ttk.Label(top_1,
                             text="type :                                                               "
                                  "                  "
                                  "   ", font=("arial", 15))
        label_id.pack(pady=5)

        combobox_type = ttk.Combobox(top_1, width=48, font=("arial", 15))
        combobox_type.config(value=["Main", "Drink", "Alcohol", "Dessert"])
        combobox_type.state(["readonly"])
        combobox_type.pack(pady=15)

        frame_buttons_1 = ttk.Frame(top_1)
        frame_buttons_1.configure(width=550, height=60, style="frame.TFrame")
        frame_buttons_1.pack()


        def Save():

            if len(entry_id.get()) == 0 or \
                    len(entry_name.get()) == 0 or \
                    len(entry_price.get()) == 0 or len(combobox_type.get()) == 0:
                messagebox.showerror("warning", "Id id empty please fill it.")

            else:
                with connection_pool.getconn() as connection:
                    with connection.cursor() as cursor:
                        cursor.execute("insert into menu(id, name, price, type) "
                                       "values(%s, %s, %s, %s)",
                                       (entry_id.get(), entry_name.get(),
                                        entry_price.get(), combobox_type.get()))

                        connection.commit()
                        cursor.close()
                        messagebox.showinfo(title="success", message="successfully")

        def New():
            entry_id.delete(0, "end")
            entry_name.delete(0, "end")
            entry_price.delete(0, "end")
            combobox_type.set("")

        def cancel():
            top_1.destroy()

        button_save = Button(frame_buttons_1, text="Save", command=Save, bg="blue", fg="#FFD5C6", height=3, width=15)

        button_new = Button(frame_buttons_1, text="New", command=New, bg="blue", fg="#FFD5C6", height=3, width=15)

        button_cancel = Button(frame_buttons_1, text="Cancel", command=cancel, bg="blue", fg="#FFD5C6", height=3, width=15)

        button_save.grid(row=0, column=0, padx=5, ipadx=10)
        button_new.grid(row=0, column=1, padx=5, ipadx=10)
        button_cancel.grid(row=0, column=2, padx=5, ipadx=10)


    button_add_item = Button(frame_buttons, text="Add New menu item", command=Add_new_item, bg="blue", fg="white")
    button_add_item.grid(ipadx=30, ipady=20, padx=10)

    button_edit_item = Button(frame_buttons, text="Edit New menu item", bg="blue", fg="white", command=edit)
    button_edit_item.grid(ipadx=30, ipady=20, row=0, column=1, padx=10)

    button_delete_item = Button(frame_buttons, text="Delete New menu item", bg="blue", fg="white", command=delete)
    button_delete_item.grid(ipadx=30, ipady=20, row=0, column=2, padx=10)

    button_refresh = Button(frame_buttons, text="   Refresh    ", bg="blue", fg="white", command=refresh)
    button_refresh.grid(ipadx=30, ipady=20, row=0, column=3, padx=10)

