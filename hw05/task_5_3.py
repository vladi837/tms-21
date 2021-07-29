'''Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]'''

limit = 300
pairs = {}


def divisors_sum(number):
    return sum(x for x in range(1, (number // 2) + 1) if number % x == 0)


for i in range(200, limit + 1):
    aggr = divisors_sum(i)
    if i == divisors_sum(aggr) and i != aggr:
        if i and aggr not in pairs:
            pairs[i] = aggr
print(pairs)