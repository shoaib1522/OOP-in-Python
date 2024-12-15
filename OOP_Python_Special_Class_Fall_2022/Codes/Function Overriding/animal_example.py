class Animal:
    def make_sound(self):
        print("The animal makes a generic sound.")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows.")

def main():
    animal = Animal()
    dog = Dog()
    cat = Cat()

    animal.make_sound()
    dog.make_sound()
    cat.make_sound()

main()