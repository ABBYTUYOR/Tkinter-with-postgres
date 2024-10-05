from tkinter import Tk, Label, Entry, Button, END
from database import *


def save():
    save_fname = fname_entry.get().title()
    save_mname = mname_entry.get().title()
    save_lname = lname_entry.get().title()

    database_save(save_fname, save_mname, save_lname )
    fname_entry.delete(0, END)
    mname_entry.delete(0, END)
    lname_entry.delete(0, END)
    database_display()

def update():
    update_fname = update_fname_entry.get().title()
    update_mname = update_mname_entry.get().title()
    update_lname = update_lname_entry.get().title()

    database_update(update_fname, update_mname, update_lname)
    update_fname_entry.delete(0, END)
    update_mname_entry.delete(0, END)
    update_lname_entry.delete(0, END)
    database_display()

def delete():
    delete_fname = delete_fname_entry.get().title()
    database_delete(delete_fname)
    delete_fname_entry.delete(0, END)
    database_display()


database_display()
window = Tk()
window.title('TKinter with postgress')
window.config(padx=100, pady=50)
title_label = Label(text='TKinter with postgress')
title_label.grid(column=0, row=0)

fname_label = Label(text='First name:')
fname_label.grid(column=0, row=2)
fname_entry = Entry()
fname_entry.grid(column=1, row=2)

mname_label = Label(text='Middle name:')
mname_label.grid(column=0, row=3)
mname_entry = Entry()
mname_entry.grid(column=1, row=3)

lname_label = Label(text='Last name:')
lname_label.grid(column=0, row=4)
lname_entry = Entry()
lname_entry.grid(column=1, row=4)

save_button = Button(text="Save", command=save, width=15)
save_button.grid(column=1, row=5)

update_label = Label(text='Update using name')
update_label.grid(column=0, row=6)

update_fname_label = Label(text='First name:')
update_fname_label.grid(column=0, row=7)
update_fname_entry = Entry()
update_fname_entry.grid(column=1, row=7)

update_mname_label = Label(text='Middle name:')
update_mname_label.grid(column=0, row=8)
update_mname_entry = Entry()
update_mname_entry.grid(column=1, row=8)

update_lname_label = Label(text='Last name:')
update_lname_label.grid(column=0, row=9)
update_lname_entry = Entry()
update_lname_entry.grid(column=1, row=9)

update_button = Button(text="Update", command=update, width=15)
update_button.grid(column=1, row=10)

delete_label = Label(text='Delete using name')
delete_label.grid(column=0, row=11)

delete_fname_label = Label(text='First name:')
delete_fname_label.grid(column=0, row=12)
delete_fname_entry = Entry()
delete_fname_entry.grid(column=1, row=12)

delete_button = Button(text="Delete", command=delete, width=15)
delete_button.grid(column=1, row=15)

window.mainloop()


