# 1
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))


# 2
def find_max(*numbers):
    return max(numbers)

print(find_max(5, 8, 2))


# 3
def student_info(**info):
    print(info)

student_info(name="Nurasyl", age=20)


# 4
def print_info(**data):
    for key, value in data.items():
        print(key, ":", value)

print_info(name="Ali", city="Astana")


# 5
def example(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

example(1, 2, 3, name="Nurasyl")
