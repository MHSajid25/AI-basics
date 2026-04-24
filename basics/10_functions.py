def greet():
    print("Hello World")

greet()

#with name

def greet(name):
    print("Hello" ,name)

greet("Ali")

greet("Sara")

#function with return value

def add(a, b):
    return a + b

result = add(3, 5)
print(result)

def square(num):
    return num*num

result = square(9)
print(result)

#Lamda functions
#For simple, one time tasks
#single line of code

add = lambda a, b: a + b
print(add(3,5))

double_it = lambda n: n*2
print(double_it(9))

nums = [1,2,3,4]
squares = list(map(lambda x: x*x, nums))
print(squares)

numbers = [1,2,3,4,5,6,7,8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)