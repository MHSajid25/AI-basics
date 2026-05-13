class Student:
    def __init__(self,name,grade):
        self.__grade = grade #Private Attribute

#student1 = Student("Ali", 90)
#print(student1.__grade)  #Error

#----------------#

class Student1:
    def __init__(self, grade, name):
        self.__grade = grade

    def get_grade(self): #Private method is returned as method
        return self.__grade

student2 = Student1("Ali",90)
print(student2.get_grade())

#----------------#

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # PRIVATE Variable (Encapsulated)

    # GETTER: Balance dekhne ke liye
    def get_balance(self):
        return f"Current Balance: {self.__balance}"

    # SETTER: Balance badalne ke liye (with Security Check)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposit ho gaya.")
        else:
            print("Ghalat rakam! Amount positive honi chahiye.")

# --- Testing ---
acc = BankAccount("Ali", 1000)

# 1. Direct access ki koshish (Error ayega ya kaam nahi karega)
# print(acc.__balance) ❌

# 2. Proper rasta (Getter/Setter)
print(acc.get_balance()) # ✅ Output: 1000
acc.deposit(500)         # ✅ Output: 500 deposit ho gaya.
print(acc.get_balance()) # ✅ Output 1500 Rs

#Assignment:

class FuelTank:
    def __init__(self, capacity, fuel):
        self.capacity = capacity
        # Private variable takay koi bahar se direct change na kar sakay
        self.__fuel = fuel

    def get_fuel_status(self):
        print(f"Current Fuel: {self.__fuel} Litres / Capacity: {self.capacity} Litres")

    def refill(self, amount):
        if amount <= 0:
            print("Ghalti: Amount positive honi chahiye!")
        elif self.__fuel + amount > self.capacity:
            # Check kar rahe hain ke kahin tank bhar kar bahar na gir jaye
            print(f"Ghalti: Tank bhar jaye ga! Sirf {self.capacity - self.__fuel}L ki jagah hai.")
        else:
            self.__fuel += amount
            print(f"{amount}L refill ho gaya.")

    def consume_fuel(self, amount):
        if amount > self.__fuel:
            # Check kar rahe hain ke jitna fuel hai us se zyada kharch na ho
            print("Ghalti: Itna fuel nahi hai! Gari ruk jaye gi.")
        else:
            self.__fuel -= amount
            print(f"{amount}L fuel kharch ho gaya.")

# --- Testing the Logic ---

# 1. 50L capacity wala tank banayein jis mein 20L fuel ho.
my_car_tank = FuelTank(50, 20)

# 2. Status check karein
my_car_tank.get_fuel_status()

# 3. 40L refill karne ki koshish (Ye mana hona chahiye kyunke 20+40=60)
my_car_tank.refill(40)

# 4. 10L refill karein (Ye ho jana chahiye)
my_car_tank.refill(10)

# 5. 100L kharch karne ki koshish (Mana hona chahiye)
my_car_tank.consume_fuel(100)

# 6. Final status
my_car_tank.get_fuel_status()