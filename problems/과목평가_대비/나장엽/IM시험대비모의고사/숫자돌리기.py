
t = int(input())
def degree(n, arr):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            result[i][k] = arr[n-k-1][i]
    return result

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    result90 = degree(n, arr)
    result180 = degree(n, result90)
    result270 = degree(n, result180)
    print('#{0}'.format(tc))
    for i in range(n):
        for k in range(n):
            print(result90[i][k], end='')
        print(end=' ')
        for j in range(n):
            print(result180[i][j], end='')
        print(end=' ')
        for m in range(n):
            print(result270[i][m], end='')
        print()