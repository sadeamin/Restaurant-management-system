# from login_window import Menu_window
from tkinter import Toplevel, ttk
from connection_poll import connection_pool
from tkinter import messagebox
from tkinter import *


class Manage_staff:
    def __init__(self):
        self.top = Toplevel()
        self.top.title("Manage Employees")
        self.top.geometry("1301x820+250+130")
        self.top.resizable(False, False)

        main_heading = ttk.Label(self.top, text="Staff Management", foreground="red",
                                 font=("arial", 30, "bold italic"))
        main_heading.pack(padx=300)

        self.tv = ttk.Treeview(self.top, height=32)
        self.tv.pack()
        self.tv["columns"] = ("first_name", "last_name")
        self.tv.heading("#0", text="Id")
        self.tv.heading("first_name", text="First Name")
        self.tv.heading("last_name", text="Last Name")

        self.tv.column("#0", width=410)
        self.tv.column("first_name", width=410)
        self.tv.column("last_name", width=410)

        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, frist_name, last_name from users order by total asc")
                for item in list(cursor):
                    self.tv.insert('', "end", text=f"{item[0]}", values=(f'{item[1]}', f'{item[2]}'))

        self.tv.column("#0", anchor="center")
        self.tv.column("first_name", anchor="center")
        self.tv.column("last_name", anchor="center")

        style = ttk.Style()
        style.configure(style="frame.TFrame")

        self.frame_buttons = ttk.Frame(self.top)
        self.frame_buttons.configure(width=1301, height=75)
        self.frame_buttons.pack(side="bottom", pady=10)

        self.button_add_staff = Button(self.frame_buttons, text="Add New Staff", command=self.Add_new_employee,
                                      bg="blue",
                                      fg="white")
        self.button_add_staff.grid(ipadx=30, ipady=20, padx=10)

        self.button_edit_staff = Button(self.frame_buttons, text="Edit Staff", bg="blue", fg="white", command=self.edit)
        self.button_edit_staff.grid(ipadx=30, ipady=20, row=0, column=1, padx=10)

        self.button_delete_staff = Button(self.frame_buttons, text="Delete Staff", bg="blue", fg="white", command=self.delete)
        self.button_delete_staff.grid(ipadx=30, ipady=20, row=0, column=2, padx=10)

        self.button_refresh = Button(self.frame_buttons, text="   Refresh    ", bg="blue", fg="white",
                                     command=self.refresh)
        self.button_refresh.grid(ipadx=30, ipady=20, row=0, column=3, padx=10)

    def refresh(self):
        self.tv.delete(*self.tv.get_children())
        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute("select id as total, frist_name, last_name from users order by total asc")
                for item in list(cursor):
                    self.tv.insert('', "end", text=f"{item[0]}", values=(f'{item[1]}', f'{item[2]}'))

    def delete(self):
        ci = self.tv.focus()
        table_value = self.tv.item(ci)
        if len(table_value["text"]) == 0 or len(table_value["values"]) == 0:
            messagebox.showerror("please select something", "Select the user which one should you went to delete")
        else:
            popup = messagebox.askyesno(title="asking", message="Do you went to delete this user")
            if popup:
                with connection_pool.getconn() as connection:
                    with connection.cursor() as cursor:
                        cursor.execute("delete from users Where id=%s", (table_value['text'],))

    def edit(self):

        ci = self.tv.focus()
        table_value = self.tv.item(ci)

        if len(table_value["text"]) == 0 or len(table_value["values"]) == 0:
            messagebox.showerror("warning", "Select any user which one should you went to edit")
        else:
            self.top_1 = Toplevel()
            self.top_1.title("Add New Menu Item")
            self.top_1.geometry("620x455+550+230")
            self.top_1.resizable(False, False)

            label_id = ttk.Label(self.top_1,
                                 text="Staff id :                            "
                                      "                                                   ",
                                 font=("arial", 15))
            label_id.pack()

            strvar1 = StringVar()

            self.entry_id_one = Entry(self.top_1, width=50, font=("arial", 15), textvariable=strvar1)
            self.entry_id_one.pack(pady=30)
            self.entry_id_one.insert(0, table_value['text'])
            self.entry_id_one.config(state="disable")

            label_id = ttk.Label(self.top_1,
                                 text="Staff first name :                       "
                                      "                                             ",
                                 font=("arial", 15))
            label_id.pack()

            strvar2 = StringVar()

            self.entry_first_name_one = Entry(self.top_1, width=50, font=("arial", 15), textvariable=strvar2)
            self.entry_first_name_one.insert(0, table_value['values'][0])
            self.entry_first_name_one.pack(pady=30)

            label_id = ttk.Label(self.top_1,
                                 text="Staff last name :                "
                                      "                                                     ",
                                 font=("arial", 15))
            label_id.pack()

            strvar3 = StringVar()

            self.entry_last_name_one = Entry(self.top_1, width=50, font=("arial", 15), textvariable=strvar3)
            self.entry_last_name_one.insert(0, table_value['values'][1])
            self.entry_last_name_one.pack(pady=30)

            style = ttk.Style()
            style.configure(style="frame.TFrame", background="blue")

            frame_buttons_1 = ttk.Frame(self.top_1)
            frame_buttons_1.pack()
            frame_buttons_1.configure(width=550, height=60)

            button_save1 = Button(frame_buttons_1, text="Save", bg="blue", fg="#FFD5C6", height=3, width=15,
                                  command=self.Update)
            button_save1.grid(row=0, column=0, padx=40, ipadx=20, ipady=10)
            button_cancel = Button(frame_buttons_1, text="Cancel", bg="blue", fg="#FFD5C6", height=3, width=15,
                                   command=self.cancel)
            button_cancel.grid(row=0, column=1, padx=40, ipadx=20, ipady=10)

    def cancel(self):
        self.top_1.destroy()

    def Add_new_employee(self):
        self.top_2 = Toplevel()
        self.top_2.title("Add Staff Item")
        self.top_2.geometry("620x495+550+230")
        self.top_2.resizable(False, False)

        self.strvar1 = StringVar()

        label_id = ttk.Label(self.top_2,
                             text="Staff Id :                                                                               ",
                             font=("arial", 15))

        label_id.pack(pady=5)
        self.entry_id = ttk.Entry(self.top_2, width=50, font=("arial", 15), textvariable=self.strvar1)
        self.entry_id.pack(pady=20)

        label_id = ttk.Label(self.top_2,
                             text="Staff First Name :                                                                  ",
                             font=("arial", 15))
        label_id.pack(pady=5)

        self.strvar2 = StringVar()

        self.entry_first_name = ttk.Entry(self.top_2, width=50, font=("arial", 15), textvariable=self.strvar2)
        self.entry_first_name.pack(pady=20)

        label_id = ttk.Label(self.top_2,
                             text="Staff Last Name :                                                                   ",
                             font=("arial", 15))
        label_id.pack(pady=5)

        self.strvar3 = StringVar()

        self.entry_last_name = ttk.Entry(self.top_2, width=50, font=("arial", 15), textvariable=self.strvar3)
        self.entry_last_name.pack(pady=20)

        label_id = ttk.Label(self.top_2,
                             text="Password :                                                       "
                                  "                  "
                                  "   ", font=("arial", 15))
        label_id.pack(pady=5)

        self.strvar4 = StringVar()

        self.entry_password = ttk.Entry(self.top_2, font=("arial", 15), width=50, textvariable=self.strvar4)
        self.entry_password.config(show="*")

        self.entry_password.pack()

        self.frame_buttons_1 = ttk.Frame(self.top_2)
        self.frame_buttons_1.configure(width=550, height=60, style="frame.TFrame")
        self.frame_buttons_1.pack(pady=20)

        self.button_save = Button(self.frame_buttons_1, text="Save", command=self.Save, bg="blue", fg="#FFD5C6",
                                  height=3,
                                  width=15)

        self.button_new = Button(self.frame_buttons_1, text="New", command=self.New, bg="blue", fg="#FFD5C6", height=3,
                                 width=15)

        self.button_cancel = Button(self.frame_buttons_1, text="Cancel", command=self.Cancel, bg="blue", fg="#FFD5C6",
                                    height=3,
                                    width=15)

        self.button_save.grid(row=0, column=0, padx=5, ipadx=10)
        self.button_new.grid(row=0, column=1, padx=5, ipadx=10)
        self.button_cancel.grid(row=0, column=2, padx=5, ipadx=10)

    def Cancel(self):
        self.top_2.destroy()

    def Update(self):
        popup = messagebox.askyesno(title="asking", message="Do you went to update this user")
        if popup:
            if len(self.entry_id_one.get()) == 0 or \
                    len(self.entry_last_name_one.get()) == 0 or \
                    len(self.entry_last_name_one.get()) == 0:
                messagebox.showerror("warning", "text boxes empty please fill it.")

            else:
                with connection_pool.getconn() as connection:
                    with connection.cursor() as cursor:
                        cursor.execute("Update users set frist_name=%s, last_name=%s Where id=%s",
                                       (self.entry_first_name_one.get(), self.entry_last_name_one.get(),
                                        self.entry_id_one.get()))

                        connection.commit()
                        cursor.close()
                        messagebox.showinfo(title="success", message="successfully")

    def Save(self):
        if len(self.entry_id.get()) == 0 or \
                len(self.entry_first_name.get()) == 0 or \
                len(self.entry_last_name.get()) == 0 or len(self.entry_password.get()) == 0:
            messagebox.showerror("warning", "Those entry fields are empty please fill it.")

        else:
            with connection_pool.getconn() as connection:
                with connection.cursor() as cursor:
                    qu = f"insert into users(id, frist_name, last_name, password) values('{self.strvar1.get()}', '{self.strvar2.get()}', '{self.strvar3.get()}', '{self.strvar4.get()}')"
                    print(qu.strip())
                    cursor.execute(qu)

                    connection.commit()
                    cursor.close()
                    messagebox.showinfo(title="success", message="successfully")

    def New(self):
        self.entry_id.delete()
        self.entry_first_name.delete()
        self.entry_last_name.delete()
        self.entry_password.delete()
