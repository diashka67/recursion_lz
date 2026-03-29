def notation(list1, num, k):  #функция остатков от евклида, самого числа и счетности системы
    ostatok = int(num % k)
    n = (num - ostatok) / k    #находим остаток в алгоритме евклида

    if ostatok == 10:        #первод чисел в буквы
        ostatok = 'A'
    elif ostatok == 11:
        ostatok = 'B'
    elif ostatok == 12:
        ostatok = 'C'
    elif ostatok == 13:
        ostatok = 'D'
    elif ostatok == 14:
        ostatok = 'E'
    elif ostatok == 15:
        ostatok = 'F'

    ostatok = str(ostatok)   #перводим в строчный и пихаем в лист остатков
    list1.append(ostatok)

    
    if n < 1:
        return list1          
    else:
        return notation(list1, n, k)   #рекурсия
list1 = []
num = int(input("ваше число: "))
k = int(input('Ваша система счисленния (до 16): '))
list1 = notation(list1, num, k)
result = "".join(list1)
print(result)