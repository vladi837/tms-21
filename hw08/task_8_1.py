'''Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел'''

n = int(input('enter n: '))


def fact2(n):
    if n == 0:
        print(1)
        return 1
    else:
        print(n)
        return n * fact2(n - 1)


print(fact2(n))