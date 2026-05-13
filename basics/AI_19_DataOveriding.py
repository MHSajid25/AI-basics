#Method Overiding

class Animal:
    def speak(self):
        print("some sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

dog1 = Dog()
dog1.speak()
Animal1 = Animal()
Animal1.speak()