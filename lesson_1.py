class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    # class attribute
    counter = 0

    # constructor           parameters
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # fields / attributes
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    counter = 0
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, weight, product_type):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg!')
        else:
            print(f'You loaded {product_type} on {self.model} - {weight} kg.')


print('Start of the program')

print(f'Factory CAR produced: {Car.counter}')

digit = 33
bmw_car = Car('BMW X7', 2020, 'red')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} '
      f'COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

honda_car = Car('HONDA Fit', 2022, 'blue', 900)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} '
      f'COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}')

toyota_car = Car(penalties=1200, the_year=2009,
                 the_model='Toyota Camry', the_color='white')
print(f'MODEL: {toyota_car.model} YEAR: {toyota_car.year} '
      f'COLOR: {toyota_car.color} PENALTIES: {toyota_car.penalties}')
# toyota_car.color = 'black'
toyota_car.change_color('black')
print(f'MODEL: {toyota_car.model} YEAR: {toyota_car.year} '
      f'NEW COLOR: {toyota_car.color} PENALTIES: {toyota_car.penalties}')
honda_car.drive('Osh')
bmw_car.drive('Kant')
honda_car.drive('Batken')

kamaz_truck = Truck('Kamaz 300', 2000,
                    'orange', 500, 35000)
print(f'MODEL: {kamaz_truck.model} YEAR: {kamaz_truck.year} '
      f'COLOR: {kamaz_truck.color} PENALTIES: {kamaz_truck.penalties} '
      f'LOAD CAPACITY: {kamaz_truck.load_capacity} kg')
kamaz_truck.load_cargo(40000, 'apples')
kamaz_truck.load_cargo(20000, 'potatoes')
kamaz_truck.drive('Tokmok')

boeing_plane = Plane('Boeing 747', 2023, 'green')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} '
      f'COLOR: {boeing_plane.color}')


print(f'Factory CAR produced: {Car.counter}')
print(f'Factory TRUCK produced: {Truck.counter}')
print('End of the program')
