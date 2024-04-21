from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6,8))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_details():
    web = website_entry.get()
    email = email_entry.get()
    pas = password_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": pas
        }
    }
    if len(pas) == 0 or len(web) == 0:
        messagebox.showerror(title="Empty", message="Cannot have empty password or website!", icon="error")
    else:
        try:
            with open(file="data.json", mode="r") as data:
                data_entry = json.load(data)
                data_entry.update(new_data)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as data:
                json.dump(new_data, data ,indent=4)
        else:
            data_entry.update(new_data)

            with open(file="data.json", mode="w") as data:
                json.dump(data_entry, data,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Done", message="Data saved successfully.")

# -------------------------- FIND PASSWORD ---------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"Credentials for website {website} does not exist.")
# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.title("Password Manager")
root.config(padx=50,pady=50)

canvas = Canvas(width= 200, height=200, highlightthickness=0)
logo = PhotoImage(file="3D Lock Icon.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0,pady=10)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=20, highlightthickness=0, relief="groove")
website_entry.focus()
website_entry.grid(column=1, row=1, pady=2)

search_btn = Button(text="Search", width=11,command=find_password)
search_btn.grid(column=2, row=1, pady=0)

email_label = Label(text="E-mail/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35,highlightthickness=0, relief="groove", bd=2)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"jotiprovapal@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, padx=0)

password_entry = Entry(width=20,highlightthickness=0, relief="groove")
password_entry.grid(column=1, row=3, padx=0)

generate_btn = Button(text="Generate Password", width=11, command=generate)
generate_btn.grid(column=2, row=3, padx=0, pady=0)

add_button = Button(text="Add", width=33, command=add_details)
add_button.grid(column=1, row=4, columnspan=2)

root.mainloop()