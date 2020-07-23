from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from psycopg2 import *


class Login_window:

    def Login(self, h=None):
        h = self.entry_password.get()
        g = self.entry_user_id.get(0.0, "end")
        if len(h) > 10 or len(g) > 10:
            messagebox.showerror(title="invalid value", message="Invalid Credentials")
        elif len(h) == 0 or len(g) == 0:
            messagebox.showerror(title="Warning", message="You'r password or user id is empty, please input something")

        with connect(database="learning", user="postgres", password="782489", host="localhost") as connection:
            with connection.cursor() as cursor:
                cursor.execute("select password from users Where user_id = %s", (g,))
                pw = tuple(cursor)[0][0]
                if pw == int(h):
                    messagebox.showinfo(title="successful", message="Login was successfully")
                else:
                    messagebox.showerror(title="Something when's wrong!", message="Incorrect password!")

    def __init__(self, master):
        master.title("Login")
        master.geometry("620x420+500+500")
        # master.resizable(False, False)
        self.label = ttk.Label(master, background="orange", foreground="blue", text="Restaurant Management System",
                               font=("arial", 29, "bold"))
        self.label.config(width=650)

        self.label.pack(ipady=20)

        self.style = ttk.Style()

        self.frame2 = ttk.Frame(master)
        self.frame2.configure(width=40, height=100, style="1.TFrame")
        self.frame2.pack()

        self.user_label = ttk.Label(self.frame2, text='User ID :')
        self.entry_user_id = Text(self.frame2, height=1, width=35, relief=GROOVE, font=("arial", 20))

        self.pw_label = ttk.Label(self.frame2, text="Password :")
        self.entry_password = ttk.Entry(self.frame2,  width=35, show="*", font=("arial", 20))
        self.entry_password.config(show="*")
        self.entry_password.bind("<Return>", self.Login)

        self.user_label.grid(row=0, column=0)
        self.entry_user_id.grid(row=0, pady=15, column=1, padx=5)
        self.pw_label.grid(row=1, column=0, padx=5)
        self.entry_password.grid(row=1, pady=20, column=1)

        self.frame1 = ttk.Frame(master)
        self.frame1.configure(width=50, height=50)

        self.frame1.pack(fill=BOTH, padx=15, pady=15)
        self.button_login = ttk.Button(self.frame1, text="Login", command=self.Login)
        self.button_Cancel = ttk.Button(self.frame1, text="Cancel", command=sys.exit)
        self.button_login.grid(row=0, column=1, padx=90, ipady=10, ipadx=20, pady=10)
        self.button_Cancel.grid(row=0, column=2, padx=90, ipady=10, ipadx=20, pady=10)

        self.label2 = ttk.Label(master, background="red", foreground="blue", text="    Welcome, to the Restaurant",
                                font=("arial", 29, "bold"))
        self.label2.config(width=650)
        self.label2.pack(ipady=11)


def main():
    r = Tk()
    login = Login_window(r)
    r.mainloop()


if __name__ == '__main__':
    main()
