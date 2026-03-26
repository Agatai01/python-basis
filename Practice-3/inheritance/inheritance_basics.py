# 1. Basic inheritance
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()


# 2. Child class with its own method
class Cat(Animal):
    def meow(self):
        print("Meow")

c = Cat()
c.speak()
c.meow()


# 3. Inheriting attributes
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Nurasyl")
print(s.name)


# 4. Using inherited method
class Bird(Animal):
    pass

b = Bird()
b.speak()


# 5. Multiple child classes
class Teacher(Person):
    pass

t = Teacher("Ali")
print(t.name)
