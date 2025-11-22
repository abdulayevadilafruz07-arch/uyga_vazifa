'''onlayn magazin'''
# shop manager loyihasi
# class Product:
#     def __init__(self,title,price,year):
#         self.title = title
#         self.price = price
#         self.year = year
#         self.type=''
#
#
# class Shop:
#     def __init__(self,title,phone):
#         self.title = title
#         self.phone = phone
#         self.baza=[]
#
#     def add_water(self):
#         title =input("title")
#         price = input("price")
#         year = input("year")
#         p1 = Product(title,price,year)
#         p1.type='water'
#         self.baza.append(p1)
#
#
#     def add_food(self):
#         title =input("title")
#         price = int(input("price"))
#         year = int(input("year"))
#         p1 = Product(title,price,year)
#         p1.type='food'
#         self.baza.append(p1)
#
#
#     def view_all(self):
#         for item in self.baza:
#             if item.type == 'water':
#                 print(f"title: {item.title}, price: {item.price}, year: {item.year}")
#             else:
#                 print(f"title: {item.title}, price: {item.price}, year: {item.year}")
#
#             print(f"title: {item.title}, price: {item.price}, type: {item.type}")
#
#
#     def update_water(self):
#         if self.type == 'water':
#             n_title = input("title")
#             n_price = int(input("price"))
#             n_year = int(input("year"))
#             p1= Product(n_title,n_price,n_year)
#             p1.type='water'


    # def update_food(self):
    #     shop1.view_all()
# shop1=Shop("shop1","123445666")
# shop1.update_water()
#
# def shop_manager(shop:Shop):
#     while True:
#         kod=input("1. add water\n2. add food\n3. view all\n4. update water\n5. exit")
#         if kod=='1':
#             shop.add_water()
#         elif kod=='2':
#             shop.add_food()
#         elif kod=='3':
#             shop1.view_all()
#         elif kod=='4':
#             shop1.view_all()
#             shop1.update_water()
#         else:
#             break
# shop_manager(shop1)
#
# '''uyga vazifa'''
# class Product():
#     def __init__(self,title,price,year):
#         self.title = title
#         self.price = price
#         self.year = year
#
#     def info(self):
#         print(f"title:{self.title},price:{self.price},year:{self.year}")
#
# class electronics(Product):
#     pass
# s1=Product('tv','100','2025')
# s1.info()
#
# class food(Product):
#     pass
# s2=Product('water','10','2025')
# s2.info()
#
# class book(Product):
#     pass
# s3=Product('book1','10','2025')
# s3.info()
#
# class elect(Product):
#     def __init__(self,title,price,year,size,cpu):
#         super().__init__(title,price,year)
#         self.size = size
#         self.cpu = cpu
# s1=elect('tv','100','2025','42','16')
# s1.info()
#
# class food1(Product):
#     def __init__(self,title,price,year,sizew,waterw)
#         super().__init__(title,price,year)
#         self.sizew = sizew
#         self.waterw = waterw
# s2=food1('water','10','2025','1','w')
# s2.info()
#
# class book2(Product):
#     def __init__(self,title,price,year,sizeb,colour):
#         super.__init__(title,price,year)
#         self.sizeb = sizeb
#         self.colour = colour
# s3=book2('book1','30','2025','2','green')
# s3.info()
#
# class Shop():
#     def __init__(self,name,baza):
#         self.name = name
#         self.baza = baza
#         self.electronics_products = []
#         self.food_products = []
#         self.book_products = []
#
#
#     def add_elect(self,product):
#         self.electronics_products.append(product)
#
#
#     def delete_elect(self,title):
#         for p in self.electronics_products:
#             if p.title == title:
#                 self.electronics_products.remove(p)
#                 print(f'{title} ochdi')
#         print("topilmadi")
#
#     def edit_elect(self,title,n_price=None,n_year=None):
#         for p in self.electronics_products:
#             if p.title == title:
#                 if n_price:
#                     p.price = n_price
#                 if n_year:
#                     p.year = n_year
#                     print(f'{title} yangilandi')
#                     return
#         print("topilmadi")
#
#     def show_elect(self,product):
#         for p in self.electronics_products:
#             p.info()