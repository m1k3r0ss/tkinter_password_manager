from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
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

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    web = website_entry.get()
    email = email_entry.get()
    pas = password_entry.get()

    is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email} \n "
                                             f"Password: {pas}\n Save these?", icon="question")
    if is_ok:
        if len(pas) !=0 and len(web) != 0:
            with open(file="data.txt", mode="a") as data:
                data.write(f"Website:{web} | Email:{email} |Password:{pas}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(title="Done", message="Data saved successfully.")
        else:
            messagebox.showerror(title="Empty", message="Cannot have empty password or website!", icon="error")
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

website_entry = Entry(width=35, highlightthickness=0, relief="groove")
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, pady=2)

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