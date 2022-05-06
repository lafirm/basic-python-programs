from tkinter import *
from tkinter.ttk import Combobox
window = Tk()  # creating an application object (called window) using Tk() function

# add widgets for our app below
# to create a button
btn = Button(window, text="This is Button widget", fg="blue")
btn.place(x=40, y=100)

#to create a label
lbl = Label(window, text="This is Label widget", fg="red", font=("Times", 16))
lbl.place(x=40, y=60)

# to create a single line text box
text_field = Entry(window, fg="purple", bd=3)
text_field.place(x=40, y=140)

# to create a combo-box (it creates a dropdown for collection datatypes like tuple or list)
var = StringVar()
var.set("one")
data = ("one", "two", "three", "four")
cb_box = Combobox(window, values=data)
cb_box.place(x=40, y=180)

# to create a list-box (it displays collection of all string items)
lb = Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END, num)
lb.place(x=40, y=220)

# to create radio-buttons
v0 = IntVar()
v0.set(1)
rb1 = Radiobutton(window, text="Male", variable=v0, value=1)
rb1.place(x=40, y=10)
rb2 = Radiobutton(window, text="Female", variable=v0, value=0)
rb2.place(x=40, y=30)

# to create check-buttons
v1 = IntVar()
v2 = IntVar()
cb1 = Checkbutton(window, text="Cricket", variable=v1)
cb1.place(x=200, y=10)
cb2 = Checkbutton(window, text="Tennis", variable=v2)
cb2.place(x=200, y=30)

window.title("Application Title")  # set title for the application
window.geometry("400x500+10+20")  # set size for the application window
window.mainloop()  # entering into event listening loop
