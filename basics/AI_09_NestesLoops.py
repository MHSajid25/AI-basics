#Basic Nested Loop

for i in range(3):
    print("outer loop")
    for j in range(3):
         print("   inner loop")

#Example

i = 4
rows = i
cols = i

matrix = []
for m in range(rows):
    row = []
    for c in range(cols):
        row.append(0)
    matrix.append(row)

for row in matrix:
    print(' '.join(map(str, row))) #map(str, row) converts list to str

#Looping Over DS

for char in 'Python':
    print(char)

#count

count = 0
for char in "banana":
    if char == 'a':
        count += 1
print(count)

#Reverse a string

s = "HAMZA"
rev = ""

for char in s:
    rev = char + rev

print(rev)

#Loops on Dictionaries
#Structure Data like Dictionaries

student = {"name": "Ali", "age": 19, "class": "A-level"}
for i in student:
    print(student[i])

#Loop on Dictionary Q2
student_list = [{"name":"hamza","age":19,"grade":"A"},{"age":20, "grade": "A+" }]

for student in student_list:
    print(f"Name: {student.get('name', '')} | Grade: {student.get('grade', '')}") #Use of '' in get is to avoid None












