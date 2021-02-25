n = []
a =[]
while True:
    o = input('name, age separeted by space: ').split(' ')
    n.append (o[0])
    a.append (int(o[1]))
    y = input('one more?(y/n): ')
    if y == 'n':
        break
for idx, val in enumerate(n):
    print(f"user {idx}: {val}, {a[idx]}")
sum = 0
for n in a: #цикл
    sum = sum + n #сумма всех 
avg = sum/len(a)
print(f"avg age = {avg}")
