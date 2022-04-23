arr = list(map(int, input().split()))

max = arr[0]
min = arr[0]

for i in range(len(arr)):
    if max < arr[i]:
        max = arr[i]
    else:
        max = max
    if min > arr[i]:
        min = arr[i]
    else:
        min = min 
    
print(f'MAX={max}')
print(f'MIN={min}')