class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("The car is driving.")

class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is cycling.")

class Train(Vehicle):
    def move(self):
        print("The train is running on tracks.")

def travel(vehicle):
    vehicle.move()

def main():
    vehicle = Vehicle()
    car = Car()
    bicycle = Bicycle()
    train = Train()

    travel(vehicle)
    travel(car)
    travel(bicycle)
    travel(train)

main()