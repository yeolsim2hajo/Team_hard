arr = []
for i in range(9):
    arr.append(int(input()))

Max = -98765432
idx = 0
for i in range(len(arr)):
    if Max < arr[i]:
        Max = arr[i]
        idx = i

print(Max)
print(idx+1)