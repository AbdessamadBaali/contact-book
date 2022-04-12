

# ===================================
# function for add a person to contact
import sqlite3
from tkinter import messagebox


class Contact:

    def __init__(self,name,phone,mail):
        try:
            db = sqlite3.connect("contactData.db")
            cr = db.cursor()
            cr.execute("""create table if not exists contactInfo
            (name varchar(25) not null,
            phone varchar(25) not null unique,
            mail varchar(35) not null unique )""")
            cr.execute(f"insert into contactinfo values('{name}', '{phone}', '{mail}')")
            messagebox.showinfo("Message Info", "The Contact is Added With Successfully")
            
        except Exception as e:
            messagebox.showerror("Message Error", f"Something wrong {str(e)}")

        finally:
            db.commit()
            db.close()

    @staticmethod
    def addContact(name, phone, mail):
        return "done with successfully!"

    @staticmethod
    def updateContact():
        pass

    # function for delete a contact
    # def deleteContact(self):
    #     update = []
    #     contactFile = open('contact.txt', encoding='utf8')
    #     lignesContact = contactFile.readlines()
    #     contactFile.close()
    #     for i in lignesContact:
    #         person = i.split('-')
    #         if person[0] != name:
    #             update.append(i)
    #     contactFile = open('contact.txt', 'w', encoding='utf8')
    #     contactFile.writelines(update)
    #     contactFile.close()
    #     print('contct delete with successfully \n')
