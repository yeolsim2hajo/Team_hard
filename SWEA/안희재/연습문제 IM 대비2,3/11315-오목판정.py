# 오목: 가로 5개이상 or 세로 5개 이상 or 대각선 5개 이상!
# .를 기준으로 split해서, 길이가 5이상인 것(ooooo etc)
# 아, 근데 split말고 다른걸로 풀어보자 - 1만나면 그때서야 카운트+=1하는데,
# 0만나면 다시 0으로 만들어버리는 것 / cnt가 5가되면 break

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 90도 회전시킨 것
    ret = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[j][N-1-i] = arr[i][j]

    def diag(): # 대각선체크(오른쪽 위, 왼쪽아래, 정대각선 모두) 
        result = 0
        # 오른쪽 위
        for i in range(N):
            cnt = 0
            x, y = -1, i-1
            for j in range(N-i):
                x += 1
                y += 1
                if arr[x][y] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = 1 # 대각선 체크 성공하면, 1리턴
                else:
                    cnt = 0
        # 왼쪽 아래
        for i in range(N):
            cnt = 0
            x, y = -1, i-1
            for j in range(N-i):
                x += 1
                y += 1
                if arr[y][x] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = 1
                else:
                    cnt = 0
        
        # 90도 회전한 후, 오른쪽 위
        for i in range(N):
            cnt = 0
            x, y = -1, i-1
            for j in range(N-i):
                x += 1
                y += 1
                if ret[x][y] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = 1
                else:
                    cnt = 0    
        # 90도 회전한 후, 왼쪽 아래
        for i in range(N):
            cnt = 0
            x, y = -1, i-1
            for j in range(N-i):
                x += 1
                y += 1
                if ret[y][x] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = 1
                else:
                    cnt = 0   
        return result

    def check():
        result = 'NO' # 기본상태 : NO
        # step1 - 가로체크
        for i in range(N):
            cnt = 0
            for j in range(N):
                if arr[i][j] == 'o':
                    cnt +=1
                    if cnt == 5: # 오목 5개
                        result = 'YES'
                else: # 연속된 5개의 돌이어야 하므로, '.'만나면 바로 0으로 초기화
                    cnt = 0
        # step2 - 세로체크
        for i in range(N):
            cnt = 0
            for j in range(N):
                if arr[j][i] == 'o':
                    cnt +=1
                    if cnt == 5:
                        result = 'YES'
                else:
                    cnt = 0
        # step3 - 대각선 체크
        if diag():
            result = 'YES'
        
        return result

    print(f'#{tc}', check())

# 아. 오른쪽아래방향 대각선만 검사함..ㅋㅋㅋㅋㅋㅋㅋㅋ
# 존나 골때리네.. 음.. 90도 회전하면 되긴하느데 이렇게까지..?

0,0,0
0,1,2
2,2,2

....o
...o.
..o..
.o...
o....