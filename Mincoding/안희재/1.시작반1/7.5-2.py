arr = [0] * 6

num = list(map(int,input().split()))

for i in num:
    arr[i] = 1

print(*arr)