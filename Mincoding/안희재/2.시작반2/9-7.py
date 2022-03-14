arr = [list(map(int,input().split())) for _ in range(6)]

cnt = 0
for i in range(6):
    if arr[i][0] < arr[i][1]:
        arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
        cnt += 1

for i in range(6):
    print(*arr[i])
print(f'{cnt}명')
