# from login_window import Menu_window
from tkinter import Toplevel, ttk, Text
from connection_poll import connection_pool
from tkinter import messagebox
from psycopg2 import errors

def Manage_menu_window():
    top = Toplevel()
    top.title("Show Menu")
    top.geometry("1301x800+250+130")
    top.resizable(False, False)

    main_heading = ttk.Label(top, text="Restaurant Management System", foreground="red",
                             font=("arial", 30, "bold italic"))
    main_heading.pack(padx=300)

    style = ttk.Style()
    style.configure(style="frame.TFrame")

    frame_buttons = ttk.Frame(top)
    frame_buttons.configure(width=1301, height=75)
    frame_buttons.pack(side="bottom", pady=10)




    def Add_new_item():
        top_1 = Toplevel()
        top_1.title("Add New Menu Item")
        top_1.geometry("620x495+550+230")
        top_1.resizable(False, False)



        label_id = ttk.Label(top_1,
                             text="Menu Item Id :                                                                        ", font=("arial", 15))
        label_id.pack(pady=5)
        entry_id = Text(top_1, width=50, height=1, font=("arial", 15))
        entry_id.pack(pady=20)

        label_id = ttk.Label(top_1,
                             text="Menu Item Name :                                                                  ", font=("arial", 15))
        label_id.pack(pady=5)

        entry_name = Text(top_1, width=50, height=1, font=("arial", 15))
        entry_name.pack(pady=20)

        label_id = ttk.Label(top_1,
                             text="Menu Item Price :                                                                   ", font=("arial", 15))
        label_id.pack(pady=5)

        entry_price = Text(top_1, width=50, height=1, font=("arial", 15))
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

            if len(entry_id.get(0.0, "end")) == 0 or \
                    len(entry_name.get(0.0, "end")) == 0 or \
                    len(entry_price.get(0.0, "end")) == 0 or len(combobox_type.get()) == 0:
                messagebox.showerror("warning", "Id id empty please fill it.")

            else:
                with connection_pool.getconn() as connection:
                    with connection.cursor() as cursor:
                        cursor.execute("insert into menu(id, name, price, type) "
                                       "values(%s, %s, %s, %s)",
                                       (entry_id.get(0.0, "end"), entry_name.get(0.0, "end"),
                                        entry_price.get(0.0, "end"), combobox_type.get()))

                        connection.commit()
                        cursor.close()
                        messagebox.showinfo(title="success", message="successfully")

        def New():
            entry_id.delete(0.0, "end")
            entry_name.delete(0.0, "end")
            entry_price.delete(0.0, "end")
            combobox_type.set("")

        def cancel():
            top_1.destroy()


        button_save = ttk.Button(frame_buttons_1, text="Save", command=Save)

        button_new = ttk.Button(frame_buttons_1, text="New", command=New)
        button_cancel = ttk.Button(frame_buttons_1, text="Cancel", command=cancel)

        button_save.grid(row=0, column=0, padx=5, ipadx=50, ipady=30)
        button_new.grid(row=0, column=1, padx=5, ipadx=50, ipady=30)
        button_cancel.grid(row=0, column=2, padx=5, ipadx=50, ipady=30)





    button_add_item = ttk.Button(frame_buttons, text="Add New menu item", command=Add_new_item)
    button_add_item.grid(ipadx=30, ipady=20, padx=10)

    button_edit_item = ttk.Button(frame_buttons, text="Edit New menu item")
    button_edit_item.grid(ipadx=30, ipady=20, row=0, column=1, padx=10)

    button_delete_item = ttk.Button(frame_buttons, text="Delete New menu item")
    button_delete_item.grid(ipadx=30, ipady=20, row=0, column=2, padx=10)

    button_refresh = ttk.Button(frame_buttons, text="Refresh")
    button_refresh.grid(ipadx=30, ipady=20, row=0, column=3, padx=10)

