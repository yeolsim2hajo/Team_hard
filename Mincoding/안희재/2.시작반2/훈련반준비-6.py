arr = [0] * 9

for i in range(3):
    a, b = map(int,input().split())
    for j in range(a,b+1):
        arr[j] += 1

print(*arr)