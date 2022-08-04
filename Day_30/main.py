from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ------------------------------ DATA SEARCHER --------------------------- #
def search_data():
    search_bar = web_entry.get().lower()
    file = open("data.json", "r")
    data = json.load(file)
    if search_bar in data:
        username = data[search_bar]['email']
        password = data[search_bar]['password']
        messagebox.showinfo(title=f"{search_bar.title()} Details", message=f"ID:{username}"
                                                     f"\nPassword:{password} ")
        mail_entry.delete(0, END)
        password_entry.delete(0, END)
        mail_entry.insert(END, string=f"{username}")
        password_entry.insert(0, string=f"{password}")
    else:
        messagebox.showinfo(title="Error!", message="Data Classified, Reported to local authorities")


# ---------------------------- PASSWORD GENERATOR --------------------------- #


def password_gen():
    password_entry.delete(0, END)
    pass_word = ''
    for i in range(8):
        pass_word += chr(random.randint(47, 125))
    password_entry.insert(string=f"{pass_word}", index=0)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    username = mail_entry.get()
    password = password_entry.get()
    new_data = {
        website.lower(): {
            "email": username,
            "password": password,
        }
    }
    if website == "":
        messagebox.showerror(title="Invalid Entry", message="Please enter the Website's name")

    elif username == "":
        messagebox.showerror(title="Invalid Entry", message="Please Enter your Email/Username")

    elif password == "":
        messagebox.showerror(title="Invalid Entry", message="Please Enter a valid Password")
    else:
        try:                                                      #
            with open("data.json", "r") as data_file:
                # file.write(f"{website} | {username} | {password}\n")
                # file.close()
                data = json.load(data_file)

        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered \nEmail: {username}\n"
                                                                  f"Password: {password}")
            if is_ok:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            if messagebox.askyesno(title="Copy??", message="Do you want to copy your Password?"):
                pyperclip.copy(password)
            else:
                pass


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg="white")


canvas = Canvas(width=200, height=190, bg="white", highlightthickness=0)
lock = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

web_name = Label(text="Website:", bg="white")
web_name.grid(row=1, column=0, sticky=E)

mail_label = Label(text="Email/Username:", bg="white")
mail_label.grid(row=2, column=0, sticky=E)


password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, sticky=E)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2, sticky=W)
web_entry.focus()

mail_entry = Entry(width=35)
mail_entry.insert(index=0, string="eshansinha2002@gmail.com")
mail_entry.grid(row=2, column=1)


password_entry = Entry(width=35)          # show="*" can be used
password_entry.grid(row=3, column=1)

gen_pass = Button(text="Generate Password", width=20, bg="white", command=password_gen, highlightthickness=0)
gen_pass.grid(row=3, column=2,)

search = Button(text="Search", bg="white", width=20, highlightthickness=0, command=search_data)
search.grid(row=1, column=2)

add = Button(text="Add", width=51, bg="white", command=save, highlightthickness=0)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
