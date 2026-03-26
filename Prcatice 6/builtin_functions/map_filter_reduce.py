from functools import reduce

numbers = [1,2,3,4,5]

# Example 1 map
print(list(map(lambda x: x*2, numbers)))

# Example 2 map square
print(list(map(lambda x: x**2, numbers)))

# Example 3 filter even
print(list(filter(lambda x: x%2==0, numbers)))

# Example 4 filter greater than 3
print(list(filter(lambda x: x>3, numbers)))

# Example 5 reduce sum
print(reduce(lambda a,b: a+b, numbers))