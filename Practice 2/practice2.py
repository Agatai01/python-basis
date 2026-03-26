a = [
    {'name': 'Nurasyl', 'id': '001'},
    {'name': 'Dias', 'id': '002'},
    {'name': 'Tamerlan', 'id': '003'}
]

b = [
    {'id': '001', 'gpa': '4.0'},
    {'id': '002', 'gpa': '3.9'},
    {'id': '003', 'gpa': '3.8'}
]

for person in a:
    for grade in b:
        if person['id'] == grade['id']:
            print(person['name'], "-", grade['gpa'])
