arr = list(map(int, input().split()))

flag = 0
for i in range(1, len(arr), 1):
    if abs(arr[i-1] - arr[i]) >= 3: # 0, 1/1, 2/2, 3/3, 4/4, 5
        flag = 1
if flag :
    print('재배치필요')
else:
    print('완벽한배치')