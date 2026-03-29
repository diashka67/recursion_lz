def perfect(chislo,deliteli,vse):
    deliteli += 1 #идя по рекурсии подбираем делители
    if chislo % deliteli == 0:
        vse += deliteli #Подхдящие делители
    if deliteli >= chislo // 2 : #для сокращения работы рекурсии
        return vse #конец рекурсии
    else:
        return perfect(chislo,deliteli,vse) #рекурсия


chislo = int(input('Введите ваше число '))
deliteli = 0
vse = 0
print(perfect(chislo,vse,deliteli) == chislo)
