from distutils.filelist import findall
from tkinter import *
import re
from module.contact import Contact
def addContact():
    name  = valName.get()
    phone = valPhone.get()
    mail = valEmail.get()
    
    Contact(name,phone,mail)



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
updateBtn = Button(root, text="update contact".title(),bg="#81ecec",padx=10,pady=5)
updateBtn.place(x=120, y=200)

# btn for delete a contact
deleteBtn = Button(root, text="delete contact".title(),bg="#81ecec",padx=10,pady=5)
deleteBtn.place(x=240, y=200)

# btn for show a contact
showBtn = Button(root, text="show all contact".title(),bg="#81ecec",padx=10,pady=5)
showBtn.place(x=10, y=250)

# button for exit the app
exitBtn = Button(root, text="Exit",bg="#81ecec",padx=10,pady=5, command=root.quit)
exitBtn.place(x=140, y=250)
root.mainloop()
