arr = [3,4,2,5,7,9]

a, b = map(int,input().split())

arr[a], arr[b] = arr[b], arr[a]

print(*arr)