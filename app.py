import db_system as db
import tkinter as tk
from tkinter import * 
from tkinter import messagebox

window = tk.Tk()
window.title("Input Password")
window.geometry("300x100")
window.columnconfigure(0, weight=1)

def check_connection():
    connected_status = False
    try:
        connected = db.get_databases()
        if connected == 'connected':
            connected_status = True
        else:
            connected_status = False 
    except:
        messagebox.showinfo("information","Information")  
        connected = 'failed'
    return connected_status

def check_users(data):
    login_status = False
    password = data
    query = "Select Password from users"
    datalist = db.get_data(query)
    if password == datalist:
        login_status = True
        if login_status:
            print("we need binary numbers")
        else:
            print("Login Failed")
    else:
        print("Cannot Found Users")

def login():
    label = tk.Label(window,text = "Enter Password")
    label.pack()
    
    txt_pass = tk.Entry(window, width = 15, show="*")
    txt_pass.pack()

    button = tk.Button(window, text = "Submit", command = lambda: check_users(txt_pass.get()))
    button.pack()

    window.mainloop()

def convertDataTostring(s):
    mystring = ' '.join(map(str, s))
    return mystring

if __name__ == "__main__":
    check_conn = check_connection()
    if check_conn == True:
        login() 
