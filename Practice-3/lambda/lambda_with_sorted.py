students = [("Ali", 85), ("Dana", 92), ("Arman", 78)]

# 1
print(sorted(students, key=lambda x: x[1]))

# 2
print(sorted(students, key=lambda x: x[1], reverse=True))

# 3
print(sorted(students, key=lambda x: x[0]))

# 4
numbers = [5,1,9,2]
print(sorted(numbers, key=lambda x: -x))

# 5
words = ["apple", "banana", "kiwi"]
print(sorted(words, key=lambda x: len(x)))
