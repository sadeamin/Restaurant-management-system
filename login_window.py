from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from psycopg2 import *
from menu_window import Menu_window
from manage_menu_window import Manage_menu_window
from manage_employees import Manage_staff
from order_window import *


class Login_window:
    USER = 'First'
    def __init__(self, login_master=Tk()):  # Tk() the Tk() default parameter
        self.login_master = login_master
        login_master.title("Login")
        login_master.protocol("WM_DELETE_WINDOW", self.exit_event)
        login_master.geometry("620x420+500+500")
        login_master.resizable(False, False)
        self.label = ttk.Label(login_master, background="black", foreground="white",
                               text="Restaurant Management System",
                               font=("arial", 29, "bold"))
        self.label.config(width=650)

        self.label.pack(ipady=20)

        self.style = ttk.Style()

        self.frame2 = ttk.Frame(login_master)
        self.frame2.configure(width=40, height=100, style="1.TFrame")
        self.frame2.pack()

        self.user_label = ttk.Label(self.frame2, text='User ID :')
        self.entry_user_id = ttk.Entry(self.frame2, width=35, font=("arial", 20))

        self.strvar = StringVar()

        self.pw_label = ttk.Label(self.frame2, text="Password :")
        self.entry_password = ttk.Entry(self.frame2, width=35, show="*", font=("arial", 20), textvariable=self.strvar)
        self.entry_password.config(show="*")
        self.entry_password.bind("<Return>", self.Login)

        self.user_label.grid(row=0, column=0)
        self.entry_user_id.grid(row=0, pady=15, column=1, padx=5)
        self.pw_label.grid(row=1, column=0, padx=5)
        self.entry_password.grid(row=1, pady=20, column=1)

        self.frame1 = ttk.Frame(login_master)
        self.frame1.configure(width=50, height=50)

        self.frame1.pack(fill=BOTH, padx=15, pady=15)
        self.button_login = Button(self.frame1, text="Login", command=self.Login, bg="blue", fg="white")
        self.button_Cancel = Button(self.frame1, text="Cancel", command=self.exit_event, bg="blue", fg="white")
        self.button_login.grid(row=0, column=1, padx=100, ipady=10, ipadx=25, pady=10)
        self.button_Cancel.grid(row=0, column=2, padx=100, ipady=10, ipadx=25, pady=10)

        self.label2 = ttk.Label(login_master, background="blue", foreground="white",
                                text="    Welcome, to the Restaurant",
                                font=("arial", 29, "bold"))
        self.label2.config(width=650)
        self.label2.pack(ipady=11)

    # exit function
    def exit_event(self):
        msg = messagebox.askyesno("Exit", "Are you sure you want exit?")
        if msg:
            exit()

    # login validation function
    def Login(self, h=None):
        h = self.entry_password.get()
        g = self.entry_user_id.get()

        try:
            if len(h) > 10 or len(g) > 10:
                messagebox.showerror(title="invalid value", message="Invalid Credentials")
            elif len(h) == 0 or len(g) == 0:
                messagebox.showerror(title="Warning",
                                     message="You'r password or user id is empty, please input something")

            with connect(database="learning", user="postgres", password="782489", host="localhost") as connection:
                with connection.cursor() as cursor:
                    cursor.execute("select password from users Where id = '%s'", (int(g),))

                    pw = tuple(cursor)[0][0]

                    if pw == h:
                        # calling the main window
                        self.login_master.destroy()
                    else:
                        messagebox.showerror(title="Something when's wrong!", message="Incorrect password!")
        except:
            messagebox.showerror(title="Error", message="Incorrect Id or some is wrong!")

        connection = connect(database="learning", user="postgres", password="782489", host="localhost")
        cursor = connection.cursor()
        cursor.execute("select * from public.users Where password=%s", (self.strvar.get(),))
        self.login_name = tuple(cursor)
        Login_window.USER = self.login_name

    def main_loop_window(self):

        self.login_master.mainloop()



login_page = Login_window()
login_page.main_loop_window()

### Main Window ###

class Main_Window(Login_window):
    def __init__(self, master_main = Tk()):
        self.master_main = master_main
        master_main.title("Restaurant Management system")
        master_main.geometry("1301x800+250+130")
        master_main.resizable(False, False)

        self.menu = Menu(master_main)
        master_main.config(menu=self.menu)
        self.submenu = Menu(self.menu)
        self.submenu1 = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.submenu)
        self.menu.add_cascade(label="Help", menu=self.submenu1)
        self.submenu.add_command(label="Exit", command=sys.exit)

        # creating the main heading
        self.main_heading = ttk.Label(self.master_main, text="Restaurant Management System", foreground="red", font=("arial", 30, "bold italic"))
        self.main_heading.grid(pady=20)

        self.logo = PhotoImage(file="20.gif").subsample(2, 2)
        self.menu_img = PhotoImage(file="list_book.png").subsample(2, 2)
        self.order_img = PhotoImage(file="book_1.png").subsample(2, 2)
        self.employees_img = PhotoImage(file="book_2.png").subsample(2, 2)
        self.menu_items_img = PhotoImage(file="issued.png").subsample(8, 8)
        self.payments_img = PhotoImage(file="search.png").subsample(8, 8)

        self.restaurant_logo = ttk.Label(self.master_main, image=self.logo)
        self.restaurant_logo.grid(ipadx=60)

        self.frame_buttons = ttk.Frame(self.master_main)
        self.frame_buttons.configure(width=200, height=740)
        self.frame_buttons.grid(row=0, column=1, rowspan=2, pady=40)

        self.menu_button = ttk.Button(self.frame_buttons, text="Show Menu", image=self.menu_img,
                                      compound=TOP, command=Menu_window)
        self.payments_button = ttk.Button(self.frame_buttons, text="Show Payments",
                                          image=self.payments_img, compound=TOP)
        self.order_button = ttk.Button(self.frame_buttons, text="Order Management", command=Order_management_system,
                                       image=self.order_img, compound=TOP)
        self.employees_button = ttk.Button(self.frame_buttons, text="Manage Employees",
                                           image=self.employees_img, compound=TOP, command=Manage_staff)
        self.menu_items_button = ttk.Button(self.frame_buttons, text="Manage Menu Items",
                                            image=self.menu_items_img, compound=TOP, command=Manage_menu_window)

        self.menu_button.grid(ipadx=65, ipady=10, pady=5)
        self.order_button.grid(ipadx=47, ipady=10, pady=5)
        self.employees_button.grid(ipadx=47, ipady=25, pady=5)
        self.menu_items_button.grid(ipadx=47, ipady=40, pady=5)
        self.payments_button.grid(ipadx=60, ipady=45, pady=5)

        self.label = ttk.Label(text=f"Logged in as : {Login_window.USER[0][1]} {Login_window.USER[0][2]}")
        self.label.grid(row=2, column=0, sticky="sw")

    def mainloop_mainWindow(self):
        self.master_main.mainloop()


if __name__ == '__main__':
    mainWindow = Main_Window()
    mainWindow.mainloop_mainWindow()
