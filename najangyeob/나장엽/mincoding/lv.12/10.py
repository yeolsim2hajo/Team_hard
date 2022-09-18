idx, str = input().split()
arr = [[0]*5 for _ in range(5)]
str = ord(str)
idx = int(idx) - 1
for i in range(4, -1, -1):
    arr[idx][i] = chr(str)
    str += 1


for i in range(5):
    print(*arr[i], sep='')