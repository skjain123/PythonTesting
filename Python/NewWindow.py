from tkinter import *
from math import *
from random import *

login = False
Loginit = False

def LoginSetup():
    tk_login = Tk()
    tk_login.geometry('500x600+700+200')
    tk_login.title("My New Window Login")
    username = Text(tk_login, height=1, width=20).pack()
    password = Text(tk_login, height=1, width=20).pack()
    LoginButton = Button(tk_login, height=1, width=20, text="Login", command="Login").pack()
    

def Login():
    if (username.text == "skjain123" and password.text == "skjain123"):
        tk_login.destroy()
        tk = Tk()
        tk.geometry('500x600+700+200')
        tk.title("My New Window")
        print ("yay")

LoginSetup()
