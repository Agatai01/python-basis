names = ["Ali","Dana","Aruzhan"]
scores = [80,90,95]

# Example 1 enumerate
for i,name in enumerate(names):
    print(i,name)

# Example 2 enumerate start index
for i,name in enumerate(names,start=1):
    print(i,name)

# Example 3 zip
for n,s in zip(names,scores):
    print(n,s)

# Example 4 zip to list
print(list(zip(names,scores)))

# Example 5 type conversion
num="25"
print(int(num))
print(float(num))