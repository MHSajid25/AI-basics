#Setters and Getters

class Student:
    @property
    def grade(self):
        return self.__grade
    def __init__(self,name,grade):
        self.name = name
        self.__grade = grade
    def get_grade(self):
        return self.__grade
    def set_grade(self,grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid Grade")

student1 = Student("Ali", 90)
student1.set_grade(95)
print(student1.get_grade())