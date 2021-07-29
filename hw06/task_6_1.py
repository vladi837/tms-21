import random # создаем матрицу(1задание)
def createArray():
    r=0
    n = int(input('Enter first index matrix: '))
    m = int(input('Enter second index matrix: '))
    array = []

    for i in range(n):
        array.append([])
        for j in range(m):
            array[i].append(random.randint(0,100))
            r+=1
    min = array[0][0] #находим минимум и максимум(2,3 задание)
    max = 0
    for i in range(n):
        for j in range(n):
            if (array[i][j] < min):
                min = array[i][j]
            elif (array[i][j] > max):
                max = array[i][j]
    for i in range(n):
        print(array[i])
    print(max, min)
createArray()



