#Inheritance

class Animal:
    def speak(self):
        print("some sound")

class Dog(Animal):   #Animal class functions and data will be available in Dog class
    pass #pass works as placeholder that we dont want to write anything yet

dog1 = Dog()

dog1.speak()  #Object. Dog class inherits speak function from Animal Class

class Dog(Animal):
    def bark(self):
        print("Woof")

childdog = Dog()
childdog.bark()
childdog.speak()
Animal1 = Animal()
Animal1.speak()