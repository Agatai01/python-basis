
import json
import math

with open('rectangle.json', 'r') as file:
    data = json.load(file)


a = data.get('A')
b = data.get('B')

perimeter = 2 * (a + b)

division_result = perimeter / 3

ceil_result = math.ceil(division_result)
result_data = {"ceil_value": ceil_result}

with open('result.json', 'w') as file:
    json.dump(result_data, file)
