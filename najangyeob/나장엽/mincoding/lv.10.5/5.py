n = list(map(int, input().split()))
arr = [[0]*4 for _ in range(3)]


n1 = n[0]
n2 = n[1]
n3 = n[2]
for k in range(4):
    arr[0][k] += n1
    arr[1][k] += n2
    arr[2][k] += n3
    
    n1 += 1
    n2 += 1
    n3 += 1

for i in range(3):
    print(*arr[i], sep=' ')