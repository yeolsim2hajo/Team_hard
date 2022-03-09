arr = [0]*6


temp = list(map(int, input().split()))
for i in range(3):
    arr[i] = temp[i]

x = int(input())
for k in range(3, 6):
    arr[k] = x
    x = x+1

print(*arr)