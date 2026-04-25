class Student:
    def __init__(self, name, age, grade):  #3 Arguments
        self.name = name  #Instance variables / starts with self.
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student grade: {self.grade}")

    def is_eligible(self):
        if self.age >= 15:
            print(self.name, "is eligible for admission.")
        else:
            print(self.name, "is not eligible for admission.")

#Instance objects

#Creating Students
student1 = Student("Ali",16,"10th")
student2 = Student("Hamza",10,"4th")

#Accessing Attributes
print(student1.name)
print(student2.grade)

#calling methods
student1.display_info()
student2.is_eligible()

