

def rotate(arr):
    N = len(arr)
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for k in range(N):
            temp[k][N-1-i] = arr[i][k]

    return temp


def merge(arr, temp):
    N = len(arr)
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for k in range(N):
            result[i][k] = arr[i][k] + temp[i][k]
    return result


def func():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())

    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for k in range(N):
            temp[i][k] = arr[i][k]
    
    for i in range(K):
        arr = rotate(arr)
    
    result = merge(arr, temp)
    for i in range(len(result)):
        print(*result[i], sep = ' ')


func()