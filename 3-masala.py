from collections import namedtuple

Car = namedtuple('Car', ['brand', 'year', 'mileage'])

car1 = Car(brand='Malibu', year=2022, mileage=250)
car2 = Car(brand='Cobalt', year=2021, mileage=160)
car3 = Car(brand='Tracker', year=2023, mileage=2700)
car4 = Car(brand='BMW', year='2025', mileage=10)
car5 =Car(brand='Mers', year='2025', mileage=100)


cars = [car1, car2, car3, car4, car5]
mil_top = min(cars, key=lambda car: car.mileage)
print(f"Eng kam yurgan mashina brand {mil_top.brand}, mil: {mil_top.mileage}")