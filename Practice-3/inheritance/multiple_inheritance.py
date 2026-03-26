# 1. Basic multiple inheritance
class Father:
    def skills(self):
        print("Programming")

class Mother:
    def hobby(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.hobby()


# 2. Inheriting attributes from multiple parents
class A:
    def __init__(self):
        self.a = "Class A"

class B:
    def __init__(self):
        self.b = "Class B"

class C(A, B):
    pass


# 3. Resolving method order
class X:
    def show(self):
        print("X")

class Y:
    def show(self):
        print("Y")

class Z(X, Y):
    pass

z = Z()
z.show()  # Follows MRO


# 4. Multiple inheritance with super()
class Base1:
    def greet(self):
        print("Hello from Base1")

class Base2:
        def greet(self):
            print("Hello from Base2")

class Derived(Base1, Base2):
    pass

d = Derived()
d.greet()


# 5. Checking method resolution order
print(Child.__mro__)
