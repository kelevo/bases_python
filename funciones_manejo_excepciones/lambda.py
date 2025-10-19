add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Cannot divide by zero"

print("Suma: ", add(10, 5))
print("Resta: ", subtract(10, 5))
print("Multiplicacion: ", multiply(10, 5))
print("Division: ", divide(10, 0))

# Cuadrado de cada numero
numbers = range(1, 11)
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Números al cuadrado: ", squared_numbers)

# Pares
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Números pares: ", even_numbers)