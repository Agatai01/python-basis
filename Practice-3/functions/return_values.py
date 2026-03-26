# 1
def add(a, b):
    return a + b

result = add(3, 4)
print(result)


# 2
def get_user():
    return "Nurasyl", 20

name, age = get_user()
print(name, age)


# 3
def check_number(num):
    if num > 0:
        return "Positive"
    else:
        return "Negative"

print(check_number(-5))


# 4
def get_numbers():
    return [1, 2, 3, 4]

print(get_numbers())


# 5
def is_adult(age):
    return age >= 18

print(is_adult(20))
