arr = list(map(int,input().split()))
pivot = arr[0]
# 4 1 7 9 6 3 3 6
a, b = 1, 7

while 1:
    if arr[a] < pivot:
        while 1:
            a += 1
            if arr[a] > pivot:
                break
    if arr[b] > pivot:
        while 1:
            b -= 1
            if arr[b] < pivot:
                break

    if a > b:
        arr[0], arr[b] = arr[b], arr[0]
        break    

    arr[a], arr[b] = arr[b], arr[a]

print(*arr)

# 그래, 이게 훨씬 깔끔하지!