n = [1, 2, 65, 44, 47, 67, 0]
# if n:
#     print('yeah')
o = []
e = []
for n in n:
    if n % 2 == 0:
        e.append(n) #имя массива.append(значение) - добавить в массив
    else:
        o.append(n)
print(f"even {e}, odd {o}")