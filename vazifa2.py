
# class Person:
#     def __init__(self, name, phone,age):
#         self.name = name
#         self.phone = phone
#         self.age = age
#
#     def show(self):
#         print(f"name: {self.name}, phone: {self.phone}")
#
#
# class Student(Person):
#     def __init__(self, name, phone, age, student,group_id):
#         super().__init__(name,phone,age)
#         self.student_id = student
#         self.group_id = group_id
#
#
#     def show(self):
#         print(f"name: {self.name}, student_id: {self.student_id}, group_id: {self.group_id}")
#
# p1=Person('ali','12345667',12)
# s1=Student('vali','56677888',11,766788,45)
# p1.show()
# s1.show()
#
#
#
#
#
#
#
# class Student:
#     def __init__(self, name,phone,age,email):
#         self.name = name
#         self.phone = phone
#         self.age = age
#         self.email = email
#
#     def view_student(self):
#         print(f'{self.name} {self.phone} {self.age} {self.email}')
#
#
# class Students(Student):
#     def __init__(self,name,phone,age,email,group_id):
#         super().__init__(name,phone,age,email)
#         self.group_id = group_id
#
#     def view_student(self):
#         print(f'{self.name} {self.phone} {self.age} {self.email} {self.group_id}')
#
# class Group:
#     def __init__(self,title,profession):
#         self.title = title
#         self.profession = profession
#         self.students = []
#
#     def add_student(self):
#         name=input("name:")
#         phone=input("phone:")
#         age=input("age:")
#         email=input("email:")
#         student = Student(name,phone,age,email)
#         self.students.append(student)
#     def view_students(self):
#         count=0
#         for item in self.students:
#             count+=1
#             print(f"{count}. name:{item.name} age:{item.age}")
#
# class OTM:
#     def __init__(self,title):
#         self.title=title
#         self.groups=[]
#
#     def add_group(self):
#         title=input("title:")
#         profession=input("profession:")
#         group=Group(title,profession)
#         self.groups.append(group)
#
#     def view_groups(self):
#         count=0
#         for item in self.groups:
#             count+=1
#             print(f"{count}. title:{item.title} profession:{item.profession}")
#
# class ERP:
#     def __init__(self):
#         self.title='ERP'
#         self.otms=[]
#
#     def add_otm(self):
#         title=input("title:")
#         otm=OTM(title)
#         self.otms.append(otm)
#
#     def view_otms(self):
#         count=0
#         for item in self.otms:
#             count+=1
#             print(f"{count}. title:{item.title}")
#
# erp=ERP()
#
# def students_manager(students:Students):
#     while True:
#         kod=input("1.view student\n2.exit")
#         if kod=='1':
#             students.view_student
#         else:
#             break
#
#
# def group_manager(group:Group):
#     while True:
#         kod=input("1. add student\n2. view students\n3. break")
#         if kod=="1":
#             print('============')
#             group.add_student()
#             print('---------------')
#         elif kod=="2":
#             print('============')
#             group.view_students()
#             print('---------------')
#         else:
#             break
#
# def otm_manager(otm:OTM):
#     while True:
#         kod=input("1. add group\n2. view groups\n3. break")
#         if kod=="1":
#             print('============')
#             otm.add_group()
#             print('---------------')
#         elif kod=="2":
#             print('============')
#             otm.view_groups()
#             print('---------------')
#         else:
#             break
#
# def erp_manager(ep:ERP):
#     while True:
#         kod=input("1. add otm\n2. view otms\n3.OTM detail \n 4. break")
#         if kod=="1":
#             print('============')
#             ep.add_otm()
#             print('---------------')
#         elif kod=="2":
#             print('============')
#             ep.view_otms()
#             print('---------------')
#         elif kod=="3":
#             print('============')
#             ep.view_otms()
#             print('---------------')
#             index=int(input("otm_id :"))
#             otm=ep.otms[index-1]
#             otm_manager(otm)
#
#         else:
#             break
#
# erp_manager(erp)


# # contact manager
# class Contact:
#     def __init__(self, name, phone, email):
#         self.name = name
#         self.phone = phone
#         self.email = email
#
# #
# # contact1=Contact("dilafruz","+998900461045","dilafruz@gmail.com")
# # baza=[contact1]
# # # print(baza)
#
# class Sms:
#     def __init__(self, to_phone,text):
#         self.to_phone = to_phone
#         self.text = text
#
#
#
# def view_contact(s:list):
#     for item,c in enumerate(s):
#         print(f"{item}. {c.name}, {c.phone}, {c.email}")
#
#
# def add_contact(s:list):
#     n_name=r'^[a-z0-9_-]{3,15}$'
#     for i in range(3):
#         name=input("ismi=")
#         if re.match(n_name,name):
#             break
#         else:
#             print("x")
#     else:
#         name=None
#
#     d_phone=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
#     for i in range(3):
#         phone=input("phone=")
#         if re.match(d_phone,phone):
#             break
#         else:
#             print("x")
#     else:
#         phone=None
#
#     c_email=r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
#     for i in range(3):
#         email=input("email=")
#         if re.match(c_email,email):
#             break
#         else:
#             print("x")
#     else:
#         email=None
#
#     if name and phone and email:
#         contact2=Contact(name,phone,email)
#         s.append(contact2)
#         print("qoshildi")
#     else:
#         print("qoshilmadi")
#
# import re
# n=r'^[a-z0-9_-]{3,15}$'
# d=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# c=r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
#
#
# def update_contact(s:list):
#     view_contact(s)
#     idx=input("yangilamaoqchi bolgan contact indeksini kiriting")
#     if not idx.isdigit() or int(idx)>=len(s):
#         print("bunday indeks yoq")
#         return
#     idx=int(idx)
#     contact=s[idx]
#     newname=input("yangi ism")
#     if newname:
#         if re.match(n,newname):
#             contact.name=newname
#         else:
#             print("notogri ism")
#
#     newphone=input("raqami")
#     if newphone:
#         if re.match(d,newphone):
#             contact.phone=newphone
#         else:
#             print("notogri phone")
#
#     newemail=input("emaili")
#     if newemail:
#         if re.match(c,newemail):
#             contact.email=newemail
#         else:
#             print("notogri email")
#     print("contact yangilandi")
#
#
# def delete_contact(s:list):
#     view_contact(s)
#     idx=input("ochirmoqchi bolgan contact indeksi kiriting")
#     if not idx.isdigit() or int(idx)>=len(s):
#         print("bunday indeks yoq")
#         return
#     idx=int(idx)
#     s.pop(idx)
#     print("contact ochdi")
#
# def contact_manager(s:list):
#     while True:
#         kod=input("1. view contact\n2. add contact\n3.update contact\n4. delete contact\n5. exit")
#         if kod=="1":
#             view_contact(s)
#         elif kod=="2":
#             add_contact(s)
#         elif kod=="3":
#             update_contact(s)
#         elif kod=="4":
#             delete_contact(s)
#         else:
#             break
# # contact_manager(baza)
#
# '''sms manager'''
#
# def sms_view(smsl:list):
#     if not smsl:
#         print(" sms yoq")
#         return
#     for i, s in enumerate(smsl):
#         print(f"{i}. {s.to_phone}: {s.text}")
#
# def sms_send(s:list,smsl:list):
#     if not s:
#         print("contact yoq")
#         return
#
#     view_contact(s)
#     idx=input("qaysi contactga sms? (index): ")
#     if not idx.isdigit() or int(idx)>=len(s):
#         print("bunday indeks yoq")
#         return
#     idx=int(idx)
#     text=input("sms matni")
#
#
#     smsl.append(Sms(s[idx].phone,text))
#     print("yuborildi")
#
# def sms_delete(smsl:list):
#     sms_view(smsl)
#     idx=input("qaysi sms ochiriladi")
#     if not idx.isdigit() or int(idx)>=len(smsl):
#         print("bunday indeks yoq")
#         return
#     smsl.pop(int(idx))
#     print("sms ochdi")
#
# def sms_manager(s:list,smsl:list):
#     if not s:
#         print("contact yoq")
#         return
#     while True:
#         kod=input("1. view sms\n2. send sms\n3. delete sms\n4. exit")
#         if kod=="1":
#             sms_view(smsl)
#         elif kod=="2":
#             sms_send(s,smsl)
#         elif kod=="3":
#             sms_delete(smsl)
#         else:
#             break
#
#
# def manager_s_c():
#     s=[]
#     smsl=[]
#     while True:
#         kod=input("1.sms manager\n2.contact manager\n3. exit")
#         if kod=="1":
#             sms_manager(s,smsl)
#         elif kod=="2":
#             contact_manager(s)
#         else:
#             break
#
#
# manager_s_c()