"""
3 classes 
product
degitial product
physycal product
in product class atribut name and price
2 behavior 1-messad get info
2-get total products
total products=0
additional atribut file.size
physical product additional atribut class weight 
using 3 classes show anderstanding super function 
"""
class Product:
    total_products = 0 

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1

    def getInfo(self):
        return f"Product name: {self.name}, Price: {self.price}tg"

    @classmethod
    def getTotalProducts(cls):
        return f"Total products: {cls.total_products}"

class DigitalProduct(Product):

    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def getInfo(self):  
        parent_info = super().getInfo()
        return f"{parent_info}, File size: {self.file_size}MB"


class PhysicalProduct(Product):

    def __init__(self, name, price, weight):
        super().__init__(name, price) 
        self.weight = weight

    def getInfo(self):
        parent_info = super().getInfo()
        return f"{parent_info}, Weight: {self.weight}kg"

p1 = DigitalProduct("NUrasyl", 10000, 5)
p2 = PhysicalProduct("Laptop", 4500000, 2.5)
p3 = PhysicalProduct("Iphone", 1000000, 0.4)

print(p1.getInfo())
print(p2.getInfo())
print(p3.getInfo())

print(Product.getTotalProducts())