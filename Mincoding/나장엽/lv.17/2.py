arr = [5,9,4,6,1,5,8,9]

index, target = list(map(int, input().split()))
offset = 0

for idx in range(index, len(arr), 1):
    if arr[idx] != target:
        offset = offset + 1
    else:
        break


print(offset)