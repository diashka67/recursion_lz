def Evclid(first, second):
    ostatok = first % second
    if ostatok == 0:
        return second
    else:
        return Evclid(second, ostatok)#рекурсия
first = int(input('введите первое:'))
second = int(input('введите второе:'))
print(Evclid(first, second))