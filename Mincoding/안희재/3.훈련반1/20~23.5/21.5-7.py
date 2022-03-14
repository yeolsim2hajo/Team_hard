# 흰 바둑돌은 1, 검은 바둑돌은 2, 비어있으면 0
# 7 * 7
arr = [[0,0,0,0,0,0,0], [0,0,1,0,1,0,0], [0,1,2,0,2,1,0], [0,0,1,2,1,0,0], [0,0,2,1,0,1,0], [0,1,1,0,0,0,0], [0,0,0,0,0,0,0]]

white_x, white_y = map(int,input().split())

arr[white_x][white_y] = 1

direct_x = [-1,0,0,1] # 12시,9시,3시,6시 순
direct_y = [0,-1,1,0]

def check(x,y):
    cnt = 0
    for i in range(4):
        dx = x+direct_x[i]
        dy = y+direct_y[i]
        if arr[dx][dy] == 1:
            cnt += 1
    if cnt == 4:
        return 1 # 잡아먹기 성공!
    else:
        return 0

answer = 0
for i in range(7):
    for j in range(7):
        if arr[i][j] == 2:
            if check(i,j):
                answer +=1

print(answer)

