numbers = {1:"one", 2:"two", 3:"three"}
print(numbers[2])

print()
information = {"nombre": "Juan", "apellido": "Perez", "edad": 28}
del information["edad"]
print(information)
claves = information.keys()
print(claves)
values = information.values()
print(values)
pairs = information.items()
print(pairs)

print()
print()
contacts = {"Chabe": {"apellido": "Hernandez", "edad": 29, "altura": 1.80},
            "Juan": {"apellido": "Perez", "edad": 28, "altura": 1.75}}
print(contacts)
print(contacts["Chabe"])