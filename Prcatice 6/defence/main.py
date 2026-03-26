import os
from functools import reduce

# --- 1. Подготовка: Создаем папку и файлы (если их нет) ---
if not os.path.exists("sales"):
    os.makedirs("sales")
    with open("sales/store1.txt", "w") as f:
        f.write("Laptop,3\nMouse,10\nKeyboard,5")
    with open("sales/store2.txt", "w") as f:
        f.write("Monitor,2\nHeadphones,4\nLaptop,1")
    print("Папка 'sales' и файлы созданы автоматически!")

# --- 2. Чтение файлов ---
products = []
files = os.listdir("sales") # Список всех файлов

for file_name in files:
    path = os.path.join("sales", file_name)
    with open(path, "r") as f:
        for line in f:
            if line.strip():
                name, qty = line.strip().split(",")
                products.append((name, int(qty))) # Превращаем количество в число

# --- 3. Анализ данных ---

# len() - общее количество записей
total_records = len(products)

# sum() - общее количество проданного товара
total_qty = sum(p[1] for p in products)

# max() и min() - лучшие и худшие продажи
highest_sale = max(products, key=lambda x: x[1])
lowest_sale = min(products, key=lambda x: x[1])

# map() - увеличиваем все продажи на 2
boosted = list(map(lambda x: (x[0], x[1] + 2), products))

# filter() - товары, проданные > 5 раз
popular = list(filter(lambda x: x[1] > 5, products))

# reduce() - произведение всех количеств (из functools)
all_qtys = [p[1] for p in products]
product_of_all = reduce(lambda x, y: x * y, all_qtys)

# enumerate() - вывод с индексами
print("\nСписок товаров с индексами:")
for i, (name, qty) in enumerate(products, 1):
    print(f"{i} {name} {qty}")

# zip() - пример объединения списков
names = [p[0] for p in products]
qtys = [p[1] for p in products]
zipped = list(zip(names, qtys))

# sorted() - сортировка по количеству
sorted_list = sorted(products, key=lambda x: x[1], reverse=True)

# --- 4. Сохранение отчета ---
with open("sales_report.txt", "w") as report:
    report.write(f"Total records: {total_records}\n")
    report.write(f"Average quantity sold: {total_qty / total_records:.1f}\n")
    report.write(f"Highest quantity sold: {highest_sale[1]}\n")
    report.write(f"Lowest quantity sold: {lowest_sale[1]}\n\n")
    report.write("Popular products:\n")
    for name, qty in popular:
        report.write(f"{name} {qty}\n")

print("\nГотово! Результат в файле 'sales_report.txt'")