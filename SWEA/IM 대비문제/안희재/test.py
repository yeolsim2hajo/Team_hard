# 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1
# 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1
# 1 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 1
# 1 0 0 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1
# 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1
# 1 1 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1
# 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1
# 1 0 0 1 0 0 0 0 0 0 0 0 2 0 0 0 0 0 1
arr = [list(map(int,input().split())) for _ in range(8)]

answer = 0
for i in range(19):
    (x, y) = (0, i)
    if arr[0][i] == 1: #이제 여기서부터 시작
        while x < 8:
            x += 1
            if y+1 < 18:
                if arr[x][y+1] == 1: # 끝 사다리의 경우 문제인데..?
                    while arr[x][y] == 0:
                        y += 1
            elif y-1 >= 0:
                if arr[x][y-1] == 1: # 처음 사다리의 경우 문제인데..?
                    while arr[x][y] == 0:
                        y -= 1
        if arr[x][y] == 2:
            answer = i
        
print(answer)
