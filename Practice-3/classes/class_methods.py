# 1. Instance method
class Dog:
    def bark(self):
        print("Woof!")

d1 = Dog()
d1.bark()


# 2. Method using instance variable
class Car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

c1 = Car("Toyota")
c1.show_brand()


# 3. Method with parameters
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 3))


# 4. Updating instance variable
class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

counter = Counter()
counter.increase()
print(counter.count)


# 5. Class method using @classmethod
class University:
    name = "KBTU"

    @classmethod
    def get_university_name(cls):
        return cls.name

print(University.get_university_name())
