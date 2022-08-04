from tkinter import *

window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
#  foe padding
window.config(padx= 20, pady= 20)
def radio_used():
    print(radio_state.get())

#Label
my_label = Label(text= "I am a label", font=("Arial", 24))
my_label.grid(row=0,column=0)
my_label["text"] = 'New text'
my_label.config(text="New Text")

# Buttons

def button_clicked():
    my_label.config(text= entry.get())
def button_clicked2():
    my_label.config(text= text.get("1.0"))

button = Button(text= "Click Me", command= button_clicked)

button.grid(row=1,column=1)

# 2nd button
button2 = Button(text= "Touch me!!", command= button_clicked2)
button2.grid(row= 0, column = 2)
# Entry

entry = Entry(width=30)
entry.insert(END, string="single line text")
entry.grid(row=2,column=2)
print(entry.get())


# text
text = Text(width= 30)
text.insert(END, "Multiple line text")
text.focus()
text.grid(row=3,column=3)
print(text.get("1.0"))


# spindbox
def spin_value():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spin_value)


# Scale
def scale_value(value):
    print(value)
scale = Scale(from_= 1, to= 10, command =scale_value)


# Checkbutton
def check_used():
    print(check_state.get())
check_state = IntVar()
check = Checkbutton(text="Is On?",variable= check_state, command= check_used)
check_state.get()


# Radio Button





radio_state = IntVar()
radio1 = Radiobutton(text="Option 1", value=1, variable= radio_state, command= radio_used)
radio2 = Radiobutton(text="Option 1", value=2, variable= radio_state, command= radio_used)


# ListBox

def list_used():
    print(listbox.get(listbox.cut))

list = ["Apple","Banana","Pear","Guava"]
listbox = Listbox(height=4)
for items in list:
    listbox.insert(list.index(items),items)
listbox.bind("<<ListboxSelect>>", list_used)



window.mainloop()
