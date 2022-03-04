arr = input().split()

for i in range(len(arr)):
    if arr[i].isupper(): #대문자라면,
        arr[i] = arr[i].lower()
    else:
        arr[i] = arr[i].upper()

print(*arr)
