def iinput():
    num = int(input())
    return num

arr = [[0] * 3 for _ in range(3)]

def process(arr):
    tmp = iinput() - 1
    for i in range(3):
        for j in range(3):
            arr[i][j] = tmp + 1
            tmp = arr[i][j]
        
    return arr

def output():
    process(arr)
    for i in range(3):
        print(*arr[i])

output()