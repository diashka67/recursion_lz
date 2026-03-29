def pascal(x):
    if x == 1:
        return[[1], [1,1]]   #рекурсия закончилась
    else:
        last = pascal(x-1)  # Получаем треугольник для предыдущего
        last_element = last[-1]   # Берем последний ряд
        first_element = [1]   # Начинаем новый ряд с единицы
        for i in range(1, len(last_element)):
            first_element.append(last_element[i-1] + last_element[i])
        first_element.append(1)
        return last + [first_element]
r = int(input('до какого ряда:'))
func = pascal(r)
for r in func:
    print(r)