# 아.. 이거.........개에바야..다시..
arr = list(map(int,input().split()))
pivot = arr[0]
# 4 1 7 9 6 3 3 6
a, b = 0, 0
for i in range(1,len(arr)):
    if arr[i] > pivot:
        a = i
        break
for i in range(len(arr)-1,0,-1):
    if arr[i] < pivot:
        b = i
        break

while a < b:
    arr[a], arr[b] = arr[b], arr[a]

    for i in range(a+1,len(arr)):
        if arr[i] > pivot:
            a = i
            break
    for i in range(b-1,0,-1):
        if arr[i] < pivot:
            b = i
            break

arr[0], arr[b] = arr[b], arr[0]

print(*arr)