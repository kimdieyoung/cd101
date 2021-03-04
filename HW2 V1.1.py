c = {"comp":[name, last_name, bYear, dYear]}
while True:
    user = input('name, last name, bYear, dYear separeted by space: ').split(' ')
    c.append(user)
    y = input('one more?(y/n): ')
    if y == 'n':
        break
age = int.c[3] - int.c[2]
def sum(a):
    s = 0
    for n in a:
        s = s + n
    avg = s/len(a)
    return avg
print(f"age=" {age} ,"avg=" avg)

# ya pitalsy, ne poluchilos`