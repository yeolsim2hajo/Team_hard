from re import L


arr = [list(input())for _ in range(3)]
max = len(arr[0])
for i in range(3):
    if max < len(arr[i]):
        max = len(arr[i])
    else:
        max = max
    
    if len(arr[i]) == max:
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp

for i in range(3):
    print(''.join(arr[i]))