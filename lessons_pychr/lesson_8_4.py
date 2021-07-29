'''Описать функцию is_power_n( k , n ) логического типа, возвращающую
True, если целый параметр k (> 0) является степенью числа n (> 1), и False
в противном случае. Дано число n (> 1) и набор из 10 целых положитель-
ных чисел. С помощью функции is_power_n найти количество степеней чис-
ла N в данном наборе.'''


def is_power_n(k, n):
    while True:
        if k % n == 0 and k > 1:
            k = k / n
        elif k == 1:
            print(True)
            break
        else:
            print(False)
            break


k = int(input('k = '))
n = int(input('n = '))


def main():
    is_power_n(k, n)


if __name__ == '__main__':
    main()
