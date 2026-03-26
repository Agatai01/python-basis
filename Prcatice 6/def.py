import os

folder = "defence"

files = os.listdir(folder)

print("Files:", files)

products = []

for file in files:
    with open(os.path.join(folder, file), "r") as f:
        for line in f:
            name, qty = line.strip().split(",")
            products.append((name, int(qty)))

print(products)

print("Total records:", len(products))

highest = max(products, key=lambda x: x[1])
lowest = min(products, key=lambda x: x[1])

print("Highest:", highest)
print("Lowest:", lowest)

increased = list(map(lambda x: (x[0], x[1]+2), products))
print(increased)

popular = list(filter(lambda x: x[1] > 5, products))
print(popular)

from functools import reduce

product_all = reduce(lambda a,b: a*b, [q for n,q in products])
print(product_all)

for i, (name, qty) in enumerate(products, 1):
    print(i, name, qty)

names = [p[0] for p in products]
quantities = [p[1] for p in products]

combined = list(zip(names, quantities))

print(combined)

sorted_products = sorted(products, key=lambda x: x[1])
print(sorted_products)

average = total_quantity / len(products)

with open("sales_report.txt", "w") as f:
    f.write(f"Total records: {len(products)}\n")
    f.write(f"Average quantity sold: {average}\n")
    f.write(f"Highest quantity sold: {highest[1]}\n")
    f.write(f"Lowest quantity sold: {lowest[1]}\n\n")

    f.write("Popular products:\n")
    for name, qty in popular:
        f.write(f"{name} {qty}\n")