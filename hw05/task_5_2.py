n = int(input('Введите число: '))

sum = 0
mult = 1

while n > 0:
    digit = n % 10
    suma = sum + digit
    mult = mult * digit
    n = n // 10

print("Сумма:", sum)
print("Произведение:", mult)