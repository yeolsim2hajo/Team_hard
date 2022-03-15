arr = [['P','O','T','I','O'],['A','B','C','D','E'],['Y','O','U','R','E']]

a, b = map(int, input().split())


for i in range(3):
    for k in range(a, b+1, 1):
        print(arr[i][k], end='')