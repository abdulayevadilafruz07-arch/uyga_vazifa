# contact manager
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


contact1=Contact("dilafruz","+998900461045","dilafruz@gmail.com")
baza=[contact1]
print(baza)


def view_contact(s:list):
    for item in s:
        print(f"name:{item.name},phone:{item.phone},email:{item.email}")


def add_contact(s:list):
    n_name=r'^[a-z0-9_-]{3,15}$'
    for i in range(3):
        name=input("ismi=")
        if re.match(n_name,name):
            break
        else:
            print("x")
    else:
        name=None

    d_phone=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
    for i in range(3):
        phone=input("phone=")
        if re.match(d_phone,phone):
            break
        else:
            print("x")
    else:
        phone=None

    c_email=r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
    for i in range(3):
        email=input("email=")
        if re.match(c_email,email):
            break
        else:
            print("x")
    else:
        email=None

    if name and phone and email:
        contact2=Contact(name,phone,email)
        s.append(contact2)
        print("qoshildi")
    else:
        print("qoshilmadi")

import re
n=r'^[a-z0-9_-]{3,15}$'
d=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
c=r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'


def update_contact(s:list):
    view_contact(s)
    idx=input("yangilamaoqchi bolgan contact indeksini kiriting")
    if not idx.isdigit() or int(idx)>=len(s):
        print("bunday indeks yoq")
        return
    idx=int(idx)
    contact=s[idx]
    newname=input("yangi ism")
    if newname:
        if re.match(n,newname):
            contact.name=newname
        else:
            print("notogri ism")

    newphone=input("raqami")
    if newphone:
        if re.match(d,newphone):
            contact.phone=newphone
        else:
            print("notogri phone")

    newemail=input("emaili")
    if newemail:
        if re.match(c,newemail):
            contact.email=newemail
        else:
            print("notogri email")
    print("contact yangilandi")


def delete_contact(s:list):
    view_contact(s)
    idx=input("ochirmoqchi bolgan contact indeksi kiriting")
    if not idx.isdigit() or int(idx)>=len(s):
        print("bunday indeks yoq")
        return
    idx=int(idx)
    s.pop(idx)
    print("contact ochdi")

def contact_manager(s:list):
    while True:
        kod=input("1. view contact\n2. add contact\n3.update contact\n4. delete contact\n5. exit")
        if kod=="1":
            view_contact(s)
        elif kod=="2":
            add_contact(s)
        elif kod=="3":
            update_contact(s)
        elif kod=="4":
            delete_contact(s)
        else:
            break
contact_manager(baza)


