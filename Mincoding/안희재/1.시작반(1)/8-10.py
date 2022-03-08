arr = [[4,3,1,1], [3,1,2,1], [0,0,1,2]]

num = int(input())

cnt = 0
for i in range(3):
    for j in range(4):
        if arr[i][j] == num:
            cnt +=1

print(f'{cnt}개 존재합니다')