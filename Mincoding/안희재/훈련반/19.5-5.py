arr = [[0] * 4 for _ in range(4)]

def paint(direct, num):
    for i in range(4):
        if direct == 'G':
            arr[num][i] = 1
        else:
            arr[i][num] = 1

for i in range(3):
    a, b = input().split()
    b = int(b)
    paint(a, b)

for i in range(4):
    print(*arr[i])