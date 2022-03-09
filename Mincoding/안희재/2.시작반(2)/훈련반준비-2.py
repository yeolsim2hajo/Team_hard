arr = [[5,1,4,2,6], [3,5,0,0,7], [9,9,8,3,1]]
num = int(input())

cnt = 0
for i in range(3):
    for j in range(5):
        if arr[i][j] > num:
            cnt += 1

print(f'{cnt}개')