numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
  print(f"Número actual: {number}")

print()
for i in range(1, 4):
  print(f"Iteración número: {i}")

print()
fruits = ["manzana", "banana", "cereza", "durazno", "mango", "pera"]
for fruit in fruits:
  if fruit == "cereza":
    print("¡Encontré la cereza!")
    break
  print(f"Fruta actual: {fruit}")

print()
x = 0
while x < 5:
  if x == 3:
    break
  print(f"Valor de x: {x}")
  x += 1