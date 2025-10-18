# Fibonacci
# 0 1 1 2 3 5 8 13 21...

def fibonacci_gen(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b

for number in fibonacci_gen(100):
  print(number)