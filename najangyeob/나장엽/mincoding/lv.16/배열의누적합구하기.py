arr = list(map(int, input().split()))

for i in range(0, 5):
    arr[i+1] = arr[i] + arr[i+1]

for j in arr:
    print(j, end=' ')