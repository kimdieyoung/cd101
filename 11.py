n = [1, 2, 65, 44, 47, 67, 0]
for x in n:
    if x % 2 != 0:
        print(f"1st odd: {x}")
        break # остановить цикл

for x in n:
    if x % 2 != 0:
        print(f"1st odd: {x}")
        continue # перейти на следующую итерацию