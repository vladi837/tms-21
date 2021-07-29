'''Дан список словарей. Каждый словарь
описывает машину(серийный номер и год
выпуска). Создать новый список со всеми
машинами, год выпуска которых больше n'''

a = [{'serial number' : '1954231', 'year' : 1990},
     {'serial number' : '94445', 'year' : 2008},
     {'serial number' : '67546', 'year' : 2007},
     {'serial number' : '45564', 'year'  : 2020}]
n = int(input('Введите год: '))
dict_1 = [avto for avto in a if avto['year'] > n ]
print(dict_1)
