a = [1,2,3,4,5]
b = a
print(a)
print(b)

print()
del a[0]
print(id(a))
print(id(b))

print()
c = a[:]
print(id(a))
print(id(b))
print(id(c))

print()
a.append(6)
print(a)
print(b)
print(c)