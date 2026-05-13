#Python Special Methods
#Functions are those that can be used in global
#Method is also a func but can be used in a class

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return (f"{self.title} by {self.author}")

b = Book("1984","George Orwell")
print(b)