''' В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы. [02-4.1-BL19]'''

from random import randint

maximum1 = 0


def is_even_let(_x):  # Вложенная функция проверки числа х на чётность
    global maximum1  # Чтение внешней переменной
    if _x % 2 == 0:  # Если число чётное
        return maximum1  # Вернуть внешнюю переменную
    else:  # Иначе
        return _x  # Вернуть входную переменную х


numbers = [randint(1, 99) for _ in range(19)]  # Генерация списка из 19 элементов со случайными числами от[1;99]
print(numbers)  # Вывод списка
maximum1 = max(numbers)  # Поиск макчимума в списке
print(' maximum=', maximum1)  # Вывод максимума
li1 = list(map(is_even_let, numbers))  # Создать список в котором четные элементы заменены на максимум
<<<<<<< HEAD
print(li1)  # Вывод списка ( для сверки изменений )
=======
print(li1)  # Вывод списка ( для сверки изменений )
>>>>>>> 6a7b3c28683b32acbe46a3d9ab7df541655eb294
