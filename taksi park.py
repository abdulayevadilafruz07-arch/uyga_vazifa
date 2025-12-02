
class User:
    def __init__(self,name,phone,seria,age):
        self.name = name
        self.phone = phone
        self.seria=seria
        self.age = age
        self.is_active = True

class Car:
    def __init__(self,model,brand, year,seria):
        self.model = model
        self.brand = brand
        self.year = year
        self.seria = seria
        self.is_active = True

class Order:
    def __init__(self,user_id,car_id,date_start,date_end):
        self.user_id = user_id
        self.car_id = car_id
        self.date_start = date_start
        self.date_end = date_end

class Park:
    def __init__(self,title):
        self.cars=[]
        self.orders=[]
        self.users=[]
        self.title = title



    def add_car(self):
        model=input("model=")
        brand=input("brand=")
        year=input("year=")
        seria=input("seria=")
        car=Car(model,brand,year,seria)
        self.cars.append(car)

    def add_user(self):
        name=input("name=")
        phone=input("phone=")
        seria=input("seria=")
        age=input("age=")
        user=User(name,phone,seria,age)
        self.users.append(user)

    def add_order(self):
        self.view_user()
        user_id=int(input("user_id="))-1

        self.view_car()
        car_id=int(input("car_id="))-1
        date_start=input("date_start=")
        date_end=input("date_end=")

        order=Order(user_id,car_id,date_start,date_end)
        self.orders.append(order)



    def view_user(self):
        count = 0
        for user in self.users:
            count += 1
            print(f"{count}. {user.name}, {user.phone}, {user.seria}, {user.age}")

    def view_car(self):
        count = 0
        for car in self.cars:
            count += 1
            print(f"{count}. {car.model}, {car.brand}, {car.year}, {car.seria}")

    def view_orders(self):
        count = 0
        for order in self.orders:
            count += 1
            user=self.users[order.user_id]
            car=self.cars[order.car_id]
            print(f"{count}. {user.name}, {car.model}, {order.date_start}, {order.date_end}")


    # bosh mashinalar
    def free_cars(self):
        f={order.car_id for order in self.orders if order.is_active}
        count=0
        for i,car in enumerate(self.cars):
            if i not in f:
                count+=1
                print(f"{count}. {car.model}, {car.brand}, {car.year}")


p=Park("kkkkkk")


def park_manager(p:Park):
    while True:
        kod = input("1.add car\n2.add user\n3.view car\n4.view user\n5.add order\n6.view orders\n7.free_cars\n8.exit")
        if kod == "1":
            p.add_car()
        elif kod == "2":
            p.add_user()
        elif kod == "3":
            p.view_car()
        elif kod == "4":
            p.view_user()
        elif kod == "5":
            p.add_order()
        elif kod == "6":
            p.view_orders()
        elif kod == "7":
            p.free_cars()
        else:
            break


park_manager(p)

# vazifa
class User:
    def __init__(self, name, phone, seria, age):
        self.username = name
        self.phone = phone
        self.seria = seria
        self.age = age
        self.password = 0000
        self.is_active = True
        self.is_admin = False

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


u1 = User('user', '1234', '1234', '34')


# u1.edit()
# print(u1.username)


class Car:
    def __init__(self, model, brand, year, seria):
        self.model = model
        self.brand = brand
        self.year = year
        self.seria = seria
        self.is_active = True


class Order:
    def __init__(self, user_id, car_id, date_start, date_end):
        self.user_id = user_id
        self.car_id = car_id
        self.date_start = date_start
        self.date_end = date_end
        self.is_active = True


class Park:
    def __init__(self, title):
        self.cars = []
        self.orders = []
        self.users = []
        self.title = title

    def public_cars(self):
        count = 0
        for item in self.cars:
            if item.is_active:
                count += 1
                print(f'{count}.model: {item.model},brand:{item.brand}')

    def login(self):
        name = input("username:")
        password = input("password:")
        for item in self.users:
            if item.username == name and item.password == password:
                return item, True
            return 1, False

    def add_car(self):
        model = input("model=")
        brand = input("brand=")
        year = input("year=")
        seria = input("seria=")
        car = Car(model, brand, year, seria)
        self.cars.append(car)

    def add_user(self):
        name = input("name=")
        phone = input("phone=")
        seria = input("seria=")
        age = input("age=")
        user = User(name, phone, seria, age)
        self.users.append(user)

    def add_order(self):
        self.view_user()
        user_id = int(input("user_id=")) - 1

        self.view_car()
        car_id = int(input("car_id=")) - 1
        date_start = input("date_start=")
        date_end = input("date_end=")

        order = Order(user_id, car_id, date_start, date_end)
        self.orders.append(order)

    def view_user(self):
        count = 0
        for user in self.users:
            count += 1
            print(f"{count}. {user.name}, {user.phone}, {user.seria}, {user.age}")

    def view_car(self):
        count = 0
        for car in self.cars:
            count += 1
            print(f"{count}. {car.model}, {car.brand}, {car.year}, {car.seria}")

    def view_orders(self):
        count = 0
        for order in self.orders:
            count += 1
            user = self.users[order.user_id]
            car = self.cars[order.car_id]
            print(f"{count}. {user.name}, {car.model}, {order.date_start}, {order.date_end}")

    # bosh mashinalar
    def free_cars(self):
        f = {order.car_id for order in self.orders if order.is_active}
        count = 0
        for i, car in enumerate(self.cars):
            if i not in f:
                count += 1
                print(f"{count}. {car.model}, {car.brand}, {car.year}")


p = Park("park1")
admin = User("admin", "12345", "1234", "12")
admin.is_admin = True
p.users.append(admin)


def taxi_manager(p: Park, u: User):
    while True:
        kod = input("1.edit \n2.public cars \n3.free_cars \nbreak: ")
        if kod == '1':
            u.edit()
        elif kod == '2':
            p.public_cars()
        elif kod == '3':
            p.free_cars()
        else:
            break



# taxi_manager(p,u1)

def admin_manager(p: Park, u: User):
    while True:
        kod = input("1.add_user \n2.add_car \n3.add_order \n4.view_orders  \n5:view_users \n6:view_cars \n:break ")
        if kod == '1':
            p.add_user()
        elif kod == '2':
            p.add_car()
        elif kod == '3':
            p.add_order()
        elif kod == '4':
            p.view_orders()
        elif kod == '5':
            p.view_user()
        elif kod == '6':
            p.view_car()
        else:
            break



