arr = list(map(int, input().split()))
flag = 0

for i in range(1, len(arr)):

    if abs(arr[i-1] - arr[i]) == 1:
        if arr[i-1] < arr[i]:
            flag = 1
        if arr[i-1] > arr[i]:
            flag = 0
    
    else:
        flag = -1
        break

if flag == 1:
    print('ascending')
elif flag == 0:
    print('descending')
else:
    print('mixed') 