ab = list(map(int,input().split()))

arr = [[[0] * 3 for _ in range(2)]  for _ in range(3)]

def abc(level):
    if level == 2:
        for i in range(3):
            for j in range(2):
                print(*arr[i][j])
            print()
        return

    for i in range(3):
        for j in range(3):
            arr[i][level][j] = ab[level]

    abc(level+1)

abc(0)