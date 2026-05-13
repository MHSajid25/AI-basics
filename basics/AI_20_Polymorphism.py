#Poly - Multiple --  Morph - Form
#Different Forms
#Like Animal can have multiple forms like Dog, Cat , Pigeon etc . They all are animals but diff behaviours.
#One object can take diff forms

class Dog:
    def speak(self):
        print("woof")

class Cat:
    def speak(self):
        print("meow")

#We can utilize diff classes
for pet in [Dog(),Cat()]:   #One obj for dog, one for cat and put it in pet:
    pet.speak()

#How function overiding behaves in polymorphism

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")  # Method overiding on move method

car1 = Car()
car1.move()

#Method Overloading
#Use multiple forms

class Calculator:
    def add(self, a, b=0, c=0): #b and c have default arguments
        return a + b + c

calc1 = Calculator()
print(calc1.add(5))
print(calc1.add(5,10))
print(calc1.add(10,10,20))