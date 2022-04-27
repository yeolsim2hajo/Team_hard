# 내 ㅈ같은 코드는 버려라
# 0,0,0
# 0,1,2
# 2,2,2 
# ....o
# ...o.
# ..o..
# .o...
# o....
# https://felix0708.tistory.com/26?category=883926
N = int(input())
board = [list(input()) for _ in range(N)]
res = 0

di = [0,1,1,1] #애초에, 위에서, 그리고 왼쪽에서 스타트하기 때문에 8방향 중, 4방향만 보면 됨
dj = [1,1,0,-1] 

for i in range(N):
    for j in range(N):
        if board[i][j] == 'o':
            for k in range(4):
                cnt = 1
                ni, nj = i + di[k], j + dj[k]
                while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':
                    cnt += 1
                    ni, nj = ni + di[k], nj + dj[k]
                if cnt >= 5:
                    res = 1
                    break
            if res:
                break
    if res: # if board[i][j] == 'o'인 경우, 굳이 깨서 나올 필요가 없지 애초에.
        break

if res:
    print('YES')
else:
    print('NO')

# break로 빠져나오는거 봐라; 캬;
# 이거 꼭 보기
