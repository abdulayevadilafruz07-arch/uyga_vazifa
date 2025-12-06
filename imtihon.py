
class User:
    def __init__(self,username,phone,age,seria):
        self.username=username
        self.phone=phone
        self.age=age
        self.seria=seria
        self.balance=100
        self.password='3333'
        self.is_active = True
        self.is_admin = False
        self.savati = []


    def edit(self):
        field = input('1:username\n2:phone\n3:age\n4:password:')
        new_field = input('new: ')
        if field == '1':
            self.username = new_field
        elif field == '2':
            self.phone = new_field
        elif field == '3':
            self.age = new_field
        elif field == '4':
            self.password = int(new_field)

u1=User('user1','9055555','13','12345')
u2=User('user2','905555','12','1234')



class Product:
    def __init__(self,year,type,price,seria):
        self.year=year
        self.type=type
        self.price=int(price)
        self.seria=seria
        self.is_active = True


p1=Product('2025','food1','10','a1')
p2=Product('2025','food2','20','a2')
p3=Product('2025','food3','30','a3')
baza=[p1,p2,p3]

class Shop:
    def __init__(self,title):
        self.title=title
        self.products=[]
        self.users=[]
        self.balance=0
        self.baza=baza

    def login(self):
        name=input('username:')
        password=input('password:')
        count=0
        for item in self.users:
            count+=1
            if item.username==name and item.password==password:
                return item,True
            else:
                if count==len(self.users):
                    return 0,False


    # product funksiyalar
    def add_product(self):
        year=input('year:')
        type=input('type:')
        price=input('price:')
        seria=input('seria:')
        product=Product(year,type,price,seria)
        self.products.append(product)

    def delete_product(self):
        self.view_product()
        seria=input('ochiriladigan product seria:')
        for product in self.baza:
            if product.seria==seria:
                self.products.remove(product)
                print('ochirildi')
        print('topilmadi')

    def edit_product(self):
        self.view_product()
        seria=input('ozgaradigan product seria:')
        for product in self.products or self.baza:
            if product.seria==seria:
                product.type=input('new type:')
                product.price=int(input('new price:'))
                product.year=int(input('new year:'))
                print('ozgartirildi')
                return
        print('topilmadi')



    def view_product(self):
        print('===Productlar===')
        if not self.baza:
            print('no product')
        count=0
        for product in self.baza or self.products:
            count+=1
            print(f"{count}.yili: {product.year},type: {product.type}, narxi:{product.price},seriasi: {product.seria}")


    # user funksiyalari
    def view_user(self):
        count=0
        for user in self.users:
            count+=1
            print(f"{count}. name:{user.username},phone: {user.phone}, seria:{user.seria}, age:{user.age}")

    def add_balance(self,user):
        summa=int(input('necha pul qoshadi:'))
        if summa>0:
            user.balance+=summa
            print(f'qoshildi:{summa} som, yangi balance',user.balance)

    # savat funksiyalari
    def add_savat(self,user):
        self.view_product()
        seria=input(' product seria:')
        kg=int(input('necha kg:'))
        for p in self.baza:
            if p.seria==seria:
                for item in user.savati:
                    if item['product'].seria==seria:
                        item['kg']+=kg
                        print('savat yangilandi')
                        return

                user.savati.append({"product": p,"kg":kg})
                print('savatga qoshildi')
                return
            print('topilmadi mahsulot')

    def view_savat(self,user):
        print('===savat===')
        if not user.savati:
            print('no savat')
            return
        for item in user.savati:
            p=item['product']
            print(f"{p.type},kilosi {p.price}  som {item['kg'] }kg")

    def delete_savat(self,user):
        self.view_savat(user)
        seria=input('ochiriladigan mahsulot seria:')
        for item in user.savati:
            if item['product'].seria==seria:
                user.savat.remove(item)
                print('ochirildi')
                return
        print('topilmadi mahsulot')

    def minus_kg(self,user):
        self.view_savat(user)
        seria=input('qaysi product kg kamayadi:')
        minus=int(input('necha kg ayirilsin:'))
        for item in user.savati:
            if item['product'].seria==seria:
                if minus>item['kg']:
                    user.savati.remove(item)
                    print('mahsulot savatdan ochirildi')
                else:
                    item['kg']-=minus
                    print(f"{minus} kg ayirildi. qolgan: {item['kg']} kg")
                    return
        print('topilmadi')

    def shopping(self,user):
        if not user.savati:
            print('no savat')
            return
        count=0
        for item in user.savati:
            count+=item['product'].price*item['kg']
            print('umumiy summa:',count)
            if user.balance<count:
                print('pul yetmaydi')
                return

            user.balance-=count
            self.balance+=count
            user.savati.clear()
            print("xarid qilindi")


    # <<<<<<<<<<<<<<<<<<<<<<<<<<<MAIN--MENU>>>>>>>>>>>>>>>>>>>>>>

def user_manager(shop,user):
    while True:
        kod=input('1.savatga qoshish\n2.savatni korish\n3.kg ayirish\n4.savatdan mahsulot ochirish\n5.balansga pul qoshish\n6.xarid qilish\n7.edit user\n8.exit')
        if kod=='1':
            shop.add_savat(user)
        elif kod=='2':
            shop.view_savat(user)
        elif kod=='3':
            shop.minus_kg(user)
        elif kod=='4':
            shop.delete_savat(user)
        elif kod=='5':
            shop.add_balance(user)
        elif kod=='6':
            shop.shopping(user)
        elif kod=='7':
            shop.edit(user)
        else:
            break


def admin_manager(shop,admin):
    while True:
        kod=input('1.product qoshish\n2.product korish\n3.product ochirish\n4.view user\n5.edit_product\n6.exit')
        if kod=='1':
            shop.add_product()
        elif kod=='2':
            shop.view_product()
        elif kod=='3':
            shop.delete_product()
        elif kod=='4':
            shop.view_user()
        elif kod=='5':
            shop.edit_product()
        else:
            print('toxtadi')
            break


shop=Shop('korzinka')
admin=User('admin',"12345","30","9999")
admin.is_admin=True
shop.users.append(admin)
shop.users.append(u1)
shop.users.append(u2)


def shop_manager():
    while True:
        kod = input('1.login\n2.exit')
        if kod == '1':
            user, ok = shop.login()
            if not ok:
                print('xato')
                continue
            if user.is_admin:
                admin_manager(shop, user)
            else:
                user_manager(shop, user)
        else:
            break

shop_manager()

