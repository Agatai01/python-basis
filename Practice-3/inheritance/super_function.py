# 1. Using super() in constructor
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

e = Employee("Nurasyl", 300000)
print(e.name, e.salary)


# 2. Calling parent method using super()
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")

d = Dog()
d.speak()


# 3. Extending parent functionality
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is ready")

c = Car()
c.start()


# 4. Adding new attributes with super()
class User:
    def __init__(self, username):
        self.username = username

class Admin(User):
    def __init__(self, username, role):
        super().__init__(username)
        self.role = role

a = Admin("Ali", "Moderator")
print(a.username, a.role)


# 5. Using super() in deeper hierarchy
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

b = B()
b.show()
