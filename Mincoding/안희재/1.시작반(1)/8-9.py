arr = [[0] * 3 for _ in range(2)]

def Input():
    num = list(map(int,input().split()))
    tmp = 0
    for i in range(2):
        for j in range(3):
            arr[i][j] = num[tmp]
            tmp += 1

def process():
    sum = 0
    for i in range(2):
        for j in range(3):
            sum += arr[i][j]
    return sum

def output():
    Input()
    print(process())

output()