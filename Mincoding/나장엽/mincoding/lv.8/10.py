arr = [[4,3,1,1],[3,1,2,1],[0,0,1,2]]

n = int(input())


cnt = 0
for i in range(3):
    for k in range(4):
        if arr[i][k] == n:
            cnt += 1
print(f'{cnt}개 존재합니다')