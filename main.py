from tkinter import font, messagebox
from tkinter import *
import re
from tkinter.ttk import Treeview

from click import command
from numpy import insert
from module.contact import Contact

# fuction for add a contact to contact book
def addContact():
    name  = valName.get()
    phone = valPhone.get()
    mail = valEmail.get()
    Contact(name,phone,mail)

# function for update a contact and inside the function i create another window
def updatecontact():
    contact_f = Toplevel()
    contact_f.title("update contact".upper())
    contact_f.geometry("400x350")
    contact_f.config(bg="#ffeaa7")
    contact_f.resizable(False,False)

    # label for search name that you need to update
    name_search = Label(contact_f, text="Name",bg="#ffeaa7")
    valNameS = StringVar()
    Entry_nameSeach = Entry(contact_f, font=15, width=25, textvariable=valNameS)
    name_search.place(x=10, y=50)
    Entry_nameSeach.place(x=53, y=50)

    # function for search contact if exists we give the option for update
    def search():
        nameN = valNameS.get()
        infocheck = Contact.searchContact(nameN)
        if len(infocheck) > 0:
            # label for name  update
            name = Label(contact_f, text="New Name",bg="#ffeaa7")
            valName = StringVar()
            valName.set(infocheck[0][1])
            Entry_name = Entry(contact_f, font=15, width=25, textvariable=valName)
            name.place(x=10, y=100)
            Entry_name.place(x=130, y=100)

            # label for telephon update
            phone = Label(contact_f, text="New Phone Number",bg="#ffeaa7")
            valPhone = StringVar()
            valPhone.set(infocheck[0][2])
            Entry_phone = Entry(contact_f, font=15, width=25, textvariable=valPhone)
            phone.place(x=10, y=150)
            Entry_phone.place(x=130, y=150)

            # label for email update
            email = Label(contact_f, text="New Email",bg="#ffeaa7")
            valEmail = StringVar()
            valEmail.set(infocheck[0][3])
            Entry_email = Entry(contact_f, font=15, width=25, textvariable=valEmail)
            email.place(x=10, y=200)
            Entry_email.place(x=130, y=200)

            # function for validate the update contact
            def save():
                new_name = valName.get()
                new_phone = valPhone.get()
                new_mail = valPhone.get()
                Contact.updateContact(infocheck[0][0],new_name, new_phone, new_mail)


            # validation the up date
            btn_save = Button(contact_f, text='save'.upper(),bg="#81ecec",command=save)
            btn_save.place(x=10, y=250)
        else :
             messagebox.showwarning("Message Info", "This Contact Is Not Exists")

    # title of contact update 
    title_contact = Label(contact_f, text='contact update'.title(), font=("verdana", 20),
                         fg="#f90",bg="#ffeaa7")
    title_contact.pack()

    # button for search a contact book
    btn = Button(contact_f, text="search contact".title(),bg="#81ecec", command=search)
    btn.place(x=290, y=48)

def delete():
    delete_f = Toplevel()
    delete_f.title("delete contact".upper())
    delete_f.geometry("400x100")
    delete_f.config(bg="#ffeaa7")
    delete_f.resizable(False,False)

    # label for search name that you need to update
    name_delete = Label(delete_f, text="Name",bg="#ffeaa7")
    valNameD = StringVar()
    Entry_nameDelete = Entry(delete_f, font=15, width=25, textvariable=valNameD)
    name_delete.place(x=10, y=50)
    Entry_nameDelete.place(x=53, y=50)

    # button for search a contact book
    btn = Button(delete_f, text="delete contact".title(),bg="#81ecec",
                 command=lambda : Contact.deleteContact(valNameD.get()))
    btn.place(x=290, y=48)


# show all the contact
def show():
    show_f = Toplevel()
    show_f.title("show all contact".upper())
    show_f.geometry("500x300")
    show_f.config(bg="#ffeaa7")
    show_f.resizable(False,False)

    titleTab = Label(show_f, text='list of all the contact'.title(), font=16, bg="#ffeaa7")
    titleTab.pack()

    data = Contact.showAllContact()

    area = ('nom', 'phone', 'email')
    table = Treeview(show_f, columns=area, show='headings')
    for i in range(len(area)):
        table.column(area[i], width=150,anchor='center')
        table.heading(area[i], text=area[i])
    table.pack()
    # insert into the the table
    for i in range(len(data)):
        table.insert('', 'end', values=data[i])


# show all the trash contact
def showtrash():
    showTrash_f = Toplevel()
    showTrash_f.title("show all contact".upper())
    showTrash_f.geometry("500x300")
    showTrash_f.config(bg="#ffeaa7")
    showTrash_f.resizable(False,False)

    titleTab = Label(showTrash_f, text='list of all trash contact'.title(), font=16, bg="#ffeaa7")
    titleTab.pack()

    data = Contact.showTrashContact()

    area = ('nom', 'phone', 'email')
    table = Treeview(showTrash_f, columns=area, show='headings')
    for i in range(len(area)):
        table.column(area[i], width=150,anchor='center')
        table.heading(area[i], text=area[i])
    table.pack()
    # insert into the the table
    for i in range(len(data)):
        table.insert('', 'end', values=data[i])

# ---------- gui app contact book
root = Tk()
root.title("contact book".upper())
root.geometry("400x350")
root.config(bg="#ffeaa7")
root.resizable(False,False)
titleApp = Label(root, text="Contact book", font=("verdana", 20), fg="#f90",bg="#ffeaa7")
titleApp.place(x=10, y=5)

# label for name
name = Label(root, text="Name",bg="#ffeaa7")
valName = StringVar()
Entry_name = Entry(root, font=15, width=25, textvariable=valName)
name.place(x=10, y=50)
Entry_name.place(x=110, y=50)

# label for telephon
phone = Label(root, text="Phone Number",bg="#ffeaa7")
valPhone = StringVar()
Entry_phone = Entry(root, font=15, width=25, textvariable=valPhone)
phone.place(x=10, y=100)
Entry_phone.place(x=110, y=100)

# label for email
email = Label(root, text="Email",bg="#ffeaa7")
valEmail = StringVar()
Entry_email = Entry(root, font=15, width=25, textvariable=valEmail)
email.place(x=10, y=150)
Entry_email.place(x=110, y=150)

# btn for add a contact
addBtn = Button(root, text="add contact".title(),bg="#81ecec",padx=10,pady=5, command=addContact)
addBtn.place(x=10, y=200)

# btn for update a contact
updateBtn = Button(root, text="update contact".title(),bg="#81ecec",padx=10,pady=5, command=updatecontact)
updateBtn.place(x=120, y=200)

# btn for delete a contact
deleteBtn = Button(root, text="delete contact".title(),bg="#81ecec",padx=10,pady=5, command=delete)
deleteBtn.place(x=240, y=200)

# btn for show a contact
showBtn = Button(root, text="show all contact".title(),bg="#81ecec",padx=10,pady=5, command=show)
showBtn.place(x=10, y=250)

# btn for show trash contact
showBtn = Button(root, text="show trash contact".title(),bg="#81ecec",padx=10,pady=5, command=showtrash)
showBtn.place(x=140, y=250)

# button for exit the app
exitBtn = Button(root, text="Exit",bg="#81ecec",padx=10,pady=5, command=root.quit)
exitBtn.place(x=300, y=250)

root.mainloop()
