
'''Rent car'''
'''1.class Car:
2.class User:
3.class RentCompany:'''

class Car:
    def __init__(self,name,year,price_per_day):
        self.name = name
        self.year = year
        self.price_per_day = price_per_day
        self.is_rented = False

    def add_car(self):
        name=input("name==")
        year=input("year==")
        price_per_day=input("price_per_day==")
        car=Car(name,year,price_per_day)
        self.cars.append(car)

    def show_all(self):
        count=0
        for item in self.cars:
            count+=1
            print(f"{count}.name:{item.name},year:{item.year},price_per_day:{item.price_per_day}")

    def update_car(self,index):
        if 0<=index<len(self.cars):
            car=self.cars[index]
            new_name=input(f'Name({car.name}):')
            new_year=input(f'Year({car.year}):')
            new_price_per_day=input(f'Price({car.price_per_day}):')
            car.name=new_name
            car.year=new_year
            car.price_per_day=new_price_per_day
            print('malumot yangilandi')
        else:
            print('bunday index yoq')


class User:
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.rented_cars = []

    def user_rented_cars(self):
        count=0
        for item in self.rented_cars:
            count+=1
            print(f'{count}.first_name:{item.first_name},last_name:{item.last_name},salary:{item.salary},rented_cars:{item.rented_cars}')


class RentCompany:
    def __init__(self):
        self.balance = 0
        self.cars = []
        self.rented_cars = []


# '''ijaraga berish'''
    def rent_car(self,user,car_name):
        car=next((c for c in self.cars if c.name.lower()==car_name.lower()), None)
        if not car:
            print('car topilmadi')
            return
        if any(car==c for c, u in self.rented_cars):
            print('rented car. allaqachon ijarada')
            return
        if user.salary < car.price_per_day:
            print('yetarli emas')
            return

        self.rented_cars.append((car,user))
        user.rented_cars.append(car)
        self.balance += car.price_per_day
        print(f'{car} {user} ga ijaraga berildi.Balance: {self.balance}')

# '''mashinani qaytarish'''
    def return_car(self,user,car_name):
        car= next((c for c in user.rented_cars if c.name.lower()==car_name.lower()), None)
        if not car:
            print('user bu car ni ijaraga olmagan')
            return

        self.rented_cars.remove((car,user))
        user.rented_cars.remove(car)
        print(f'{car} {user} tomonidan qaytarildi')



def car_manager(Car):
    while True:
        kod=input("1.add car\n2.show all\n3.update car\n4.exit")
        print('1.add car'
              '2.show all'
              '3.update car'
              '4.exit')
        if kod=='1':
            Car.add_car()
        elif kod=='2':
            Car.show_all()
        elif kod=='3':
            Car.update_car(0)
        else:
            break

car_manager(Car)

def manager_r_u(company,users):
    while True:
        kod=input("1. rent car\n2.return car\n3.exit")
        if kod=='1':
            user_name=input("user name")
            user=next((u for u in users if u.first_name.lower()==user_name.lower()), None)
            if not user:
                print('user topilmadi')
                continue
            car_name=input("car name")
            company.return_car(user,car_name)
        else:
            break

users=[User("ali","valiyev",400),User("bobur","karimov",600)]

company=RentCompany()
manager_r_u(company,users)
