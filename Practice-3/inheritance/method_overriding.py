# 1. Basic method overriding
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()


# 2. Overriding with different behavior
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 4 * 4

sq = Square()
print(sq.area())


# 3. Overriding without calling parent
class Person:
    def introduce(self):
        print("Hello")

class Student(Person):
    def introduce(self):
        print("Hi, I am a student")

s = Student()
s.introduce()


# 4. Overriding with additional logic
class Vehicle:
    def move(self):
        print("Moving")

class Bike(Vehicle):
    def move(self):
        print("Bike is moving fast")

b = Bike()
b.move()


# 5. Overriding built-in method
class Book:
    def __str__(self):
        return "Book object"

book = Book()
print(book)
