# 1
class Person:
    pass

p1 = Person()
print(type(p1))


# 2
class Student:
    name = "Unknown"

s1 = Student()
print(s1.name)


# 3
class Car:
    brand = "Toyota"
    year = 2022

c1 = Car()
print(c1.brand, c1.year)


# 4
class Book:
    pass

b1 = Book()
b1.title = "Python"
print(b1.title)


# 5
class Animal:
    species = "Dog"

a1 = Animal()
a2 = Animal()
print(a1.species, a2.species)
