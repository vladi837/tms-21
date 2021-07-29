a = input('Введите строку ')
a_lng = len(a)
if a_lng > 0:
    a_mid = a[a_lng // 2:a_lng // 2 + 1:]
    print('Центральная буква:', a_mid)
    if a[0] == a_mid:
        print(a[1:a_lng - 1:])
    else:
        print('!!!')