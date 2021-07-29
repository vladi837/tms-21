'''Дан словарь, создать новый словарь, поменяв местам
ключ и значение'''
old_dict = {'a' : 5, 'b' : 19, 'c' : 55}
new_dict = {value : key for key, value in old_dict.items()}
print(new_dict)