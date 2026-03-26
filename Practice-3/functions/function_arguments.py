# 1. Positional arguments
def introduce(name, age):
    print("Name:", name, "Age:", age)

introduce("Nurasyl", 20)


# 2. Keyword arguments
introduce(age=20, name="Ali")


# 3. Default argument
def power(number, exponent=2):
    print(number ** exponent)

power(5)
power(5, 3)


# 4. Required + default бірге
def register(username, country="Kazakhstan"):
    print(username, country)

register("Nurasyl")
register("Ali", "Turkey")


# 5. Argument order example
def info(city, university):
    print(city, university)

info("Astana", "AITU")
