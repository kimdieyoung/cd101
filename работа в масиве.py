a = [111, 22, 3, 4]
b = a
a[0] = 0
print(a, b)

a = [111, 22, 3, 4]
b = a[:] #slyce копирование
a[0] = 0
print(a, b)

a = [111, 22, 3, 4]
b = a[1:len(a) - 1] #slyce копирование
a[0] = 0
print(a, b)

a = [111, 22, 3, 4]
b = a.pop(2) # удаление по индеку
print(a, b)

a = [111, 22, 3, 4]
b = a.remove(22) # удаление по значению
print(a)
print(b)