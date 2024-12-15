class Animal:
    def sound(self):
        pass                #no output

class Dog(Animal):
    def sound(self):
        print("The dog barks.")

class Cat(Animal):
    def sound(self):
        print("The cat meows.")

def make_animal_sound(animal):
    animal.sound()

def main():
    animal = Animal()
    dog = Dog()
    cat = Cat()

    make_animal_sound(animal)
    make_animal_sound(dog)
    make_animal_sound(cat)

main()