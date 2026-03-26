# 1. Class variable shared by all objects
class Student:
    school = "AITU"  # class variable

s1 = Student()
s2 = Student()
print(s1.school, s2.school)


# 2. Instance variable unique per object
class Person:
    def __init__(self, name):
        self.name = name  # instance variable

p1 = Person("Nurasyl")
p2 = Person("Ali")
print(p1.name, p2.name)


# 3. Changing class variable
class Car:
    wheels = 4

Car.wheels = 6
print(Car.wheels)


# 4. Instance variable overriding class variable
class Animal:
    type = "Wild"

a1 = Animal()
a1.type = "Domestic"  # overrides only for this instance
print(a1.type)
print(Animal.type)


# 5. Access class variable inside method
class Company:
    company_name = "TechCorp"

    def show_company(self):
        print(self.company_name)

c1 = Company()
c1.show_company()
