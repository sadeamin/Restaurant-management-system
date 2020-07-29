# from login_window import Menu_window
from tkinter import Toplevel, ttk, Text
from connection_poll import connection_pool
from tkinter import messagebox
from psycopg2 import errors
from tkinter import *

def Manage_staff():
    top = Toplevel()
    top.title("Show Menu")
    top.geometry("1301x820+250+130")
    top.resizable(False, False)

    main_heading = ttk.Label(top, text="Staff Management", foreground="red",
                             font=("arial", 30, "bold italic"))
    main_heading.pack(padx=300)

    style = ttk.Style()
    style.configure(style="frame.TFrame")

    frame_buttons = ttk.Frame(top)
    frame_buttons.configure(width=1301, height=75)
    frame_buttons.pack(side="bottom", pady=10)




    def Add_new_employee():
        top_1 = Toplevel()
        top_1.title("Add Staff Item")
        top_1.geometry("620x495+550+230")
        top_1.resizable(False, False)


        strvar1 = StringVar()

        label_id = ttk.Label(top_1,
                             text="Staff Id :                                                                               ", font=("arial", 15))

        label_id.pack(pady=5)
        entry_id = ttk.Entry(top_1, width=50, font=("arial", 15), textvariable=strvar1)
        entry_id.pack(pady=20)


        label_id = ttk.Label(top_1,
                             text="Staff First Name :                                                                  ", font=("arial", 15))
        label_id.pack(pady=5)

        strvar2 = StringVar()


        entry_first_name = ttk.Entry(top_1, width=50, font=("arial", 15), textvariable=strvar2)
        entry_first_name.pack(pady=20)


        label_id = ttk.Label(top_1,
                             text="Staff Last Name :                                                                   ", font=("arial", 15))
        label_id.pack(pady=5)

        strvar3 = StringVar()

        entry_last_name = ttk.Entry(top_1, width=50, font=("arial", 15), textvariable=strvar3)
        entry_last_name.pack(pady=20)


        label_id = ttk.Label(top_1,
                             text="Password :                                                       "
                                  "                  "
                                  "   ", font=("arial", 15))
        label_id.pack(pady=5)

        strvar4 = StringVar()

        entry_password = ttk.Entry(top_1, font=("arial", 15), width=50, textvariable=strvar4)
        entry_password.config(show="*")

        entry_password.pack()

        frame_buttons_1 = ttk.Frame(top_1)
        frame_buttons_1.configure(width=550, height=60, style="frame.TFrame")
        frame_buttons_1.pack(pady=20)



        def Save():
            if len(entry_id.get()) == 0 or \
                    len(entry_first_name.get()) == 0 or \
                    len(entry_last_name.get()) == 0 or len(entry_password.get()) == 0:
                messagebox.showerror("warning", "Those entry fields are empty please fill it.")

            else:
                with connection_pool.getconn() as connection:
                    with connection.cursor() as cursor:
                        qu = f"insert into users(id, frist_name, last_name, password) values('{strvar1.get()}', '{strvar2.get()}', '{strvar3.get()}', '{strvar4.get()}')"
                        print(qu.strip())
                        cursor.execute(qu)

                        connection.commit()
                        cursor.close()
                        messagebox.showinfo(title="success", message="successfully")
        def New():
            entry_id.delete()
            entry_first_name.delete()
            entry_last_name.delete()
            entry_password.delete()

        def cancel():
            top_1.destroy()

        button_save = Button(frame_buttons_1, text="Save", command=Save, bg="blue", fg="#FFD5C6", height=3, width=15)

        button_new = Button(frame_buttons_1, text="New", command=New, bg="blue", fg="#FFD5C6", height=3, width=15)

        button_cancel = Button(frame_buttons_1, text="Cancel", command=cancel, bg="blue", fg="#FFD5C6", height=3, width=15)

        button_save.grid(row=0, column=0, padx=5, ipadx=10)
        button_new.grid(row=0, column=1, padx=5, ipadx=10)
        button_cancel.grid(row=0, column=2, padx=5, ipadx=10)





    button_add_item = Button(frame_buttons, text="Add New Staff", command=Add_new_employee, bg="blue", fg="white")
    button_add_item.grid(ipadx=30, ipady=20, padx=10)

    button_edit_item = Button(frame_buttons, text="Edit Staff", bg="blue", fg="white")
    button_edit_item.grid(ipadx=30, ipady=20, row=0, column=1, padx=10)

    button_delete_item = Button(frame_buttons, text="Delete Staff", bg="blue", fg="white")
    button_delete_item.grid(ipadx=30, ipady=20, row=0, column=2, padx=10)

    button_refresh = Button(frame_buttons, text="   Refresh    ", bg="blue", fg="white")
    button_refresh.grid(ipadx=30, ipady=20, row=0, column=3, padx=10)


