vect = [[0] * 3 for _ in range(4)]

for i in range(4):
    arr = list(map(int,input().split()))
    vect[arr[0]][arr[1]] = 5
    print(*vect[i])