squares = [x**2 for x in range(10)]
print("Cuadrados: ", squares)

celsius = [0, 10, 20, 30, 40]
farenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Celsius: ", celsius)
print("Farenheit: ", farenheit)

print()

# Numeros pares
evens = [x for x in range(20) if x % 2 == 0]
print("Números pares: ", evens)

print()

# Transpuesta de una matriz
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix))]
print("Matriz original: ", matrix)
print("Matriz transpuesta: ", transposed)

# Ejemplo con varias lineas de codigo
transposed_verbose = []
for i in range(len(matrix)):
  new_row = []
  for row in matrix:
    new_row.append(row[i])
  transposed_verbose.append(new_row)

print("Matriz transpuesta (verbose): ", transposed_verbose)