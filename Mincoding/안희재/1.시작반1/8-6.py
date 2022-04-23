def Input():
    num = int(input())
    arr = [[0] * 4 for _ in range(3)]
    
    tmp = num
    for i in range(3):
        for j in range(4):
            arr[i][j] = tmp
            tmp += 1

    return arr

def process():
    arr2 = Input()

    for i in range(3):
        for j in range(4):
            arr2[i][j] += 1

    return arr2

def output():
    arr3 = process()
    for i in range(3):
        print(*arr3[i])

output()