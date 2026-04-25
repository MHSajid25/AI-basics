#Constructor with default value

class Dog:
    def __init__(self):
        self.name = "buddy"
    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog()
dog1.bark()

#Constructor with multiple arguments

class Car:
    def __init__(self,brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota","Red")
print(car1.brand)
print(car1.color)

car1.color = "Blue"
car2 = Car("Honda", "White")
print(car2.color)
print(car2.brand)
print(car1.color)