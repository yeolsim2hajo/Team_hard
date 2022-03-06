arr = list(map(int, input().split()))

result = sum(arr)

for i in range(result):
    for k in range(len(arr)):
        print(arr[k], end= ' ')
    print()