#가로 세로 색칠하기
# 4x4 배열
# G 3  입력받으면  arr[3][0 ~ 3] 을 1로 바꿔~ 
# S 2  입력받으면  arr[0 ~ 3][2]를 색칠하기~


arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for t in range(3):
    a, b = input().split()
    b = int(b)


    for j in range(4):
        if a == 'G':
            arr[b][j] = 1
        if a == 'S':
            arr[j][b] = 1

for i in range(4):
    for k in range(4):
        print(arr[i][k], end=' ')
    print()