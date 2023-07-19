#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', \
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', \
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', \
                'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', \
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', \
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = ''.join(password_list)
    pass_input.delete(0, tk.END)
    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = web_input.get()
    uname = uname_input.get()
    password = pass_input.get()
    new_data = {
        web:{
            "email":uname,
            "password": password
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title = 'Warning', message = "Please make sure you haven't\
                            left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title = web, message = f"These are details entered:\
                            Email: {uname}\
                            Password: {password}\
                                Is it okay to save?")
        if is_ok:
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent = 4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent = 4)
            finally:
                web_input.delete(0, tk.END)
                pass_input.delete(0, tk.END)
# ---------------------------- FIND PASSWORD ------------------------------- #

def search_password():
    web = web_input.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title = 'error', message = 'No Data File Found. ')
    else:
        if web in data:
            email = data[web]['email']
            password = data[web]['password']
            messagebox.showinfo(title = web, message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title = 'error', message = f"No data for {web} exists. ")
# ---------------------------- UI SETUP ------------------------------- #

# window
window = tk.Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

# canvas
canva = tk.Canvas(width = 200, height = 200)
mypass_img = tk.PhotoImage(file = '/home/ghazi/belajar/py_gui/password-manager-start/logo.png')
canva.create_image(100, 100, image = mypass_img)
canva.grid(row = 0, column = 1)

# label web
web_label = tk.Label(text = "Website: ")
web_label.grid(row = 1, column = 0)

# label uname
uname_label = tk.Label(text = 'Email/Username: ')
uname_label.grid(row = 2, column = 0)

# label password
pass_label = tk.Label(text = 'Password: ')
pass_label.grid(row = 3, column = 0)

# input web
web_input = tk.Entry(width = 35)
web_input.grid(row = 1, column = 1, columnspan = 2)
web_input.focus()

# input uname
uname_input = tk.Entry(width = 35)
uname_input.grid(row = 2, column = 1, columnspan = 2)
uname_input.insert(0, 'ghozi6024@gmail.com')

# input password
pass_input = tk.Entry(width = 18)
pass_input.grid(row = 3, column = 1)

# button password
pass_button = tk.Button(text = 'Generate Password', width = 13, command = generate_password)
pass_button.grid(row = 3, column = 2, columnspan = 2)

# button add
add_button = tk.Button(text = 'Add', width = 39, command = save_password)
add_button.grid(row = 4, column = 1, columnspan = 2)

# button search
search_button = tk.Button(text = 'search', width = 13, command = search_password)
search_button.grid(row = 1, column = 2)


window.mainloop()