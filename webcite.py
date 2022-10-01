import os
import requests
import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox



w = tk.Tk()
w.title('Balance')

def balance():
    id = e1.get() # Assigns a line to enter changes
    balance = e2.get() # Assigns a line to enter changes
    if e1.get() != '' and e2.get() != '': # If the line is not empty, then fill in the following code
        url = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user={}&balance={}".format(id, balance) # Assigns the given url to changes
        res = requests.get(url) # Assigns url changes to the request library
        urls = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={}".format(id) # Assigns the given url to changes
        output = requests.get(urls) # Assigns url changes to the request library
        json = output.json() # Makes a change from the url jason change
    
        for a in json: # Cycles through json
            id1 = a["id"] 
            name = a["name"] 
            surname = a["surname"] 
            email = a["email"] 
            school_group = a["school_group"] 
            status = a["status"] 
            balance1 = a["balance"] 
            if a["id"] is None: # If there is no id, then fill in the following code
                messagebox.showerror('Error', 'No User') # Returns an error
            else:
                label1.config(text="Id: {}\nName: {}\nSurname: {}\nEmail: {}\nGroup: {}\nStatus: {}\nBalance: {}".format(id1, name, surname, email, school_group, status, balance1)) # Outputs what is in the url
            

f1 = tk.Frame(width=300, height=300) # Creates a window with a button that displays the url and 2 lines for input that replace the balance and another that displays everything by ID
f2 = tk.Frame(width=700, height=300) # Creates a window in which everything from the url is displayed

f1.pack(fill=tk.BOTH, side=tk.LEFT)
f2.pack(fill=tk.BOTH, side=tk.RIGHT)

e1 = tk.Entry(master=f1, width=40) # Makes a line for input
l1 = tk.Label(master=f1, text='id:') # Makes the text for the input line

e1.grid(row=1, column=1, padx=10, pady=10)
l1.grid(row=1, column=0, sticky=tk.N, padx=20, pady=20)

e2 = tk.Entry(master=f1, width=40) # Makes a line for input
l2 = tk.Label(master=f1, text='Balance:') # Makes the text for the input line

e2.grid(row=2, column=1, padx=10, pady=10)
l2.grid(row=2, column=0, sticky=tk.N, padx=20, pady=20)

b1 = tk.Button(master=f1, width=20, text='Тисни', command=balance) # Creates a button that records the balance and displays everything from the url
b1.grid(row=3, column=0, sticky=tk.E)

label1 = tk.Label(master=f2, text='') # Makes a line where the displayed text is inserted
label1.grid(sticky=tk.NW)

w.mainloop()
