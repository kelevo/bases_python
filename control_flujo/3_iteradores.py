# Ejemplo de iterador

# Crear lista
my_list = [10, 20, 30, 40]

# Obtener el iterador
my_iter = iter(my_list)

# Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print()
text = "Hola mundo"
text_iter = iter(text)
print(next(text_iter))
print(next(text_iter))