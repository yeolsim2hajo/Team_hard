n = int(input())

def process(n):
    arr = [[0]*3 for _ in range(3)]
    for i in range(3):
        for k in range(3):
            arr[i][k] = n
            n += 1
            print(arr[i][k], end= ' ')
        print()


process(n)