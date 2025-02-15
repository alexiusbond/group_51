class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def name(self):
        return self.__name


class Car:
    def __init__(self, model, year, color, owner):
        self.__model = model
        self.__year = year
        self.__color = color
        if type(owner) == Person:
            self.__owner = owner

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if type(value) == Person:
            self.__owner = value

    def drive(self):
        print(f'Car {self.__model} is driving.')

    def __str__(self):
        return (f'Model: {self.__model}, Year: {self.__year}, Color: {self.__color}'
                f', Owner: {self.__owner.name}')

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year


# some_car = Car('Toyota Camry', 2020, 'red')
# print(some_car)

class FuelCar(Car):
    __total_fuel_amount = 0

    @staticmethod
    def get_fuel_type():
        return 'AI 95'

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel_amount += amount
        cls.show_fuel_remain()

    @classmethod
    def show_fuel_remain(cls):
        print(f'Factory FUEL_CAR has {cls.__total_fuel_amount} litters of fuel.')

    def __init__(self, model, year, color, fuel_bank, owner):
        # super().__init__(model, year, color)
        # super(self, FuelCar).__init__(model, year, color)
        Car.__init__(self, model, year, color, owner)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel.')

    def __str__(self):
        return super().__str__() + f', Fuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery, owner):
        Car.__init__(self, model, year, color, owner)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by electricity.')

    def __str__(self):
        return super().__str__() + f', Battery: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, fuel_bank, battery, owner):
        FuelCar.__init__(self, model, year, color, fuel_bank, owner)
        ElectricCar.__init__(self, model, year, color, battery, owner)

    def drive(self):
        print(f'Car {self.model} is driving by fuel or electricity.')


# FuelCar.total_fuel_amount += 1000
FuelCar.buy_fuel(1000)

p1 = Person('Peter', 23)
bmw_car = FuelCar('BMW X6', 1999,
                  'black', 70, p1)
print(bmw_car)

p2 = Person('Jim Brown', 50)
tesla_car = ElectricCar('Tesla Model X', 2023,
                        'blue', 15000, p2)
print(tesla_car)

toyota_car = HybridCar('Toyota Prius', 2021,
                       'red', 65, 10000, p2)
print(toyota_car)
toyota_car.drive()

print(HybridCar.mro())
number_1, number_2 = 2, 5
print(f'First number is greater than second number: {number_1 > number_2}')
print(f'Second number is greater than first number: {number_2 > number_1}')
print(f'BMW is better than Toyota: {bmw_car > toyota_car}')
print(f'BMW is worse than Toyota: {bmw_car < toyota_car}')
print(f'BMW is the same with Toyota: {bmw_car == toyota_car}')
print(f'BMW is not the same with Toyota: {bmw_car != toyota_car}')

print(f'Sum of numbers: {number_1 + number_2}')
print(f'Total fuel banks: {bmw_car + toyota_car}')

# FuelCar.total_fuel_amount -= 100
FuelCar.show_fuel_remain()

print(f'Factory FUEL_CAR uses {FuelCar.get_fuel_type()}')
# 123