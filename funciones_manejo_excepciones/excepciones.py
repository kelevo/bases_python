try:
  divisor = int(input("Ingrese un numero para dividisor: "))
  resultado = 100 / divisor
  print("El resultado es:", resultado)
except ZeroDivisionError as e:
  print("Error: No se puede dividir por cero.")
  print("Detalles del error:", e)
except ValueError as e:
  print("Error: Entrada invalida. Por favor ingrese un numero entero.")
  print("Detalles del error:", e)