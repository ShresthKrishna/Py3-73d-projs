from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize()
window.config(padx= 20, pady= 20)



def miles_conerter():
    km = int(entry.get())
    label3.config(text=round((km*1.6),1))
    print(km)


entry = Entry(width=30)
entry.focus()
print(entry.get())
entry.grid(row=0, column= 1)

label = Label(text="Miles")
label.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column= 0)

label3 = Label(text='')
label3.grid(row=1, column= 1)

label4 = Label(text='Km')
label4.grid(row=1, column= 2)


button = Button(text="Calculate", command=miles_conerter)
button.grid(row=2, column= 1)
window.mainloop()