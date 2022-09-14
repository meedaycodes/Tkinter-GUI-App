"""
A program that stores Phones information:
Maker, Launch Date, Price
Camera, Display,Battery

User can:

view all records
Search an Entry
Add Entry
Update Entry
Delete
Close 

"""
from sqlite3 import Row
from tkinter import *
from turtle import width
from typing import List
import backend

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(phone_name_text.get(), launch_date_text.get(), camera_text.get(),battery_text.get(), display_size_text.get(), price_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(phone_name_text.get(), launch_date_text.get(), camera_text.get(),battery_text.get(), display_size_text.get(), price_text.get())
    list1.delete(0, END)
    list1.insert(END, (phone_name_text.get(), launch_date_text.get(), camera_text.get(),battery_text.get(), display_size_text.get(), price_text.get()))

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)

        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])

        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])

        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])

        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])

        e5.delete(0,END)
        e5.insert(END, selected_tuple[5])

        e6.delete(0,END)
        e6.insert(END, selected_tuple[6])
    except IndexError:
        pass

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],phone_name_text.get(), launch_date_text.get(), camera_text.get(),battery_text.get(), display_size_text.get(), price_text.get())

window =Tk()

window.wm_title("PHONERECORD")

l1 = Label(window, text="Phone Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="Launch Date")
l2.grid(row=1, column=0)

l3 = Label(window, text="Display_size")
l3.grid(row=0, column=2)

l4 = Label(window, text="Battery")
l4.grid(row=1, column=2)

l5 = Label(window, text="Camera")
l5.grid(row=2, column=0)

l6 = Label(window, text="Price")
l6.grid(row=2, column=2)

phone_name_text = StringVar()
e1=Entry(window, textvariable=phone_name_text)
e1.grid(row=0,column=1)

launch_date_text = StringVar()
e2=Entry(window, textvariable=launch_date_text)
e2.grid(row=1,column=1)

display_size_text = StringVar()
e3=Entry(window, textvariable=display_size_text)
e3.grid(row=0,column=3)

camera_text = StringVar()
e4=Entry(window, textvariable=camera_text)
e4.grid(row=1,column=3)

battery_text = StringVar()
e5=Entry(window, textvariable=battery_text)
e5.grid(row=2,column=1)

price_text = StringVar()
e6=Entry(window, textvariable=price_text)
e6.grid(row=2,column=3)

list1=Listbox(window, height=8, width=65)
list1.grid(row=2,column=0,rowspan=12, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=5, column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=15, command=view_command)
b1.grid(row=3, column=3)

b2 = Button(window, text="Search Entry", width=15,command=search_command)
b2.grid(row=4, column=3)

b3= Button(window, text="Add Entry", width=15, command=add_command)
b3.grid(row=5, column=3)

b4 = Button(window, text="Update", width=15, command=update_command)
b4.grid(row=6, column=3)

b5 = Button(window, text="Delete", width=15, command=delete_command)
b5.grid(row=7, column=3)

b6 = Button(window, text="Close", width=15, command=window.destroy)
b6.grid(row=8, column=3)


window.mainloop()

