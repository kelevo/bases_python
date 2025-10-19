def suma_numeros_naturales(n):
  if n < 0:
    raise ValueError("El numero debe ser un natural (0 o mayor)")
  if n == 0:
    return 0
  else:
    return n + suma_numeros_naturales(n - 1)
  
numero = 20
print("La suma de los numeros naturales hasta", numero, "es:", suma_numeros_naturales(numero))