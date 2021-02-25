'''
def qqq(x, y): #функция и перменные
    t = x + y
    return t #возврат на место вызова
yo = qqq(22,44) #вызов функции с переменными
print(yo)
'''
def sum(a):
    s = 0
    for n in a:
        s = s + n
    avg = s/len(a)
    return avg