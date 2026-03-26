# 1. Basic __init__ constructor
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Nurasyl")
print(s1.name)


# 2. Constructor with multiple parameters
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b1 = Book("Python Basics", "John Smith")
print(b1.title, b1.author)


# 3. Default parameter in constructor
class Laptop:
    def __init__(self, brand, ram=8):
        self.brand = brand
        self.ram = ram

l1 = Laptop("HP")
l2 = Laptop("Dell", 16)
print(l1.brand, l1.ram)
print(l2.brand, l2.ram)


# 4. Calculated attribute inside __init__
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height  # calculated property

r1 = Rectangle(4, 5)
print(r1.area)


# 5. Using input values to initialize object
class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

u1 = User("Ali", 21)
print(u1.username, u1.age)
