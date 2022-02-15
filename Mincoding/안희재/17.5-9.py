arr = list(map(int,input().split()))
mask = [1,0,1,0,1,0]

for i in range(len(mask)):
    if mask[i] != 1:
        arr[i] = 999


min_number = min(arr)
min_idx = 0
for i in range(len(arr)):
    if min(arr) == arr[i]:
        min_idx = i

print(f'arr[{min_idx}]={min_number}')
