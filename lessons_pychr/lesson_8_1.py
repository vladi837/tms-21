'''Дан список слов. Сгенерировать новый список с перевернутыми словами'''

a = 'В лесу родилась ёлочка'

words = a.split()
reversed_words = [word[::-1] for word in words]
print(' '.join(reversed_words))
