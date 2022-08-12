import os
import requests
import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox



w = tk.Tk()
w.title('Balance')

def balance():
    id = e1.get()
    balance = e2.get()
    if e1.get() != '' and e2.get() != '':
        url = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user={}&balance={}".format(id, balance)
        res = requests.get(url)
        urls = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={}".format(id)
        output = requests.get(urls)
        json = output.json()
    
        for a in json:
            id1 = a["id"]
            name = a["name"]
            surname = a["surname"]
            email = a["email"]
            school_group = a["school_group"]
            status = a["status"]
            balance1 = a["balance"]
            if a["id"] is None:
                messagebox.showerror('Error', 'No User')
            else:
                label1.config(text="Id: {}\nName: {}\nSurname: {}\nEmail: {}\nGroup: {}\nStatus: {}\nBalance: {}".format(id1, name, surname, email, school_group, status, balance1))
            

f1 = tk.Frame(width=300, height=300)
f2 = tk.Frame(width=700, height=300)

f1.pack(fill=tk.BOTH, side=tk.LEFT)
f2.pack(fill=tk.BOTH, side=tk.RIGHT)

e1 = tk.Entry(master=f1, width=40)
l1 = tk.Label(master=f1, text='id:')

e1.grid(row=1, column=1, padx=10, pady=10)
l1.grid(row=1, column=0, sticky=tk.N, padx=20, pady=20)

e2 = tk.Entry(master=f1, width=40)
l2 = tk.Label(master=f1, text='Balance:')

e2.grid(row=2, column=1, padx=10, pady=10)
l2.grid(row=2, column=0, sticky=tk.N, padx=20, pady=20)

b1 = tk.Button(master=f1, width=20, text='Тисни', command=balance)
b1.grid(row=3, column=0, sticky=tk.E)

label1 = tk.Label(master=f2, text='')
label1.grid(sticky=tk.NW)

w.mainloop()