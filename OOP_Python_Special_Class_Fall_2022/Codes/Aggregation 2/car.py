from tyre import *
from ac import *
from heater import *
from engine import *

class Car:
    def __init__(self, car_company, engine_company, engine_transmission, seating_capacity, price, tyre_comapny, tyre_size):
        self.car_company = car_company
        self.engine = Engine(engine_company, engine_transmission)
        self.seating_capacity = seating_capacity
        self.price = price
        self.tyre = Tyre(tyre_comapny, tyre_size)
        self.ac = None
        self.heater = None

    def __str__(self):
        s = f'Car Compnay: {self.car_company}\nEngine: {self.engine}\n'
        s += f'Seating Capacity: {self.seating_capacity}\nPrice: {self.price}\n'
        s += f'Tyres: {self.tyre}\n'
        if self.ac is None:
            s += f'No AC installed\n'
        else:
            s += f'AC: {self.ac}\n'
        if self.heater is None:
            s += f'No Heater installed\n'
        else:
            s += f'Heater: {self.heater}\n'
        return s

    def add_ac(self, ac_company, ac_size):
        self.ac = AC(ac_company, ac_size)

    def add_heater(self, heater_company, heater_size):
        self.heater = Heater(heater_company, heater_size)

    def remove_ac(self):
        del self.ac
        self.ac = None

    def remove_heater(self):
        del self.heater
        self.heater = None

    def __del__(self):
        print (f'del function called for Car')

def main():
    c1 = Car('Toyota', 'Toyota', 'Manual', 4, 5500000, 'Yokohama', 16)
    print(c1)
    print ('------------------------')
    c1.add_ac('Denso', 1.5)
    print(c1)
    print('------------------------')
    c1.remove_ac()
    c1.add_heater('ABC_Heater', 2)
    print(c1)

main()
