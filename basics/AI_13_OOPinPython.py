class Car:  #Class = Blueprint
    def __init__(self, color, mileage): #__init__ constructor   #def = Methods/Member function
        self.color = color #Attributes
        self.mileage = mileage #Attributes

    def start(self): #def = Methods/Member function
        print(f"{self.color} car started with {self.mileage} mileage")

# First Object
my_car = Car("red",200) #Object/Instance created from class
my_car.start()

#First Object
my_car = Car("red",5000)
my_car.start()

#Second Object
mybrother_car = Car("white",100)
mybrother_car.start()


#Exercise 1: Mobile Factory

class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = 100

    def Specs(self):
        print(f"Brand of the phone is {self.brand}, Model is {self.model} and Battery Percentage is {self.battery}")

    def use_phone(self):
        self.battery = self.battery - 10
        print(f"Phone use kia battery kam hogae: Current Battery {self.battery}")

Mobile_model = Mobile("Apple","Iphone 17pro Max")
Mobile_model.Specs()

Mobile_model.use_phone()
Mobile_model.use_phone()

#Defining a class and Create Objects

class Mehran: #class
    def drive(self):  #def is method . self is object
        print("The car is moving") #print statement in method

car1 = Mehran() #Object . car1 is an object based on Mehranclass
car1.drive()

#Example with color

class Bike:
    color = "red"
    def drive(self):
        print(f"{self.color} bike is moving")

bike1=Bike()
bike1.drive()

#Example of Setters

class Truck:
    color = "red" #Class Attribute
    def drive(self):
        print(f"{self.color} truck is moving")
    def set_color(self, new_color):
        self.color = new_color

truck1 = Truck()
truck1.set_color("green")
truck1.drive()

#Alternate way of writing this

class Rickshaw:
    def __init__(self,color):
        self.color = color
    def rick(self):
        print(f"{self.color} rickshaw is moving")

Rick = Rickshaw("green")
Rick.rick()