N, W, H = map(int,input().split()) # H가 행, W가 열임.. / N은 쏘는 구슬 개수
arr = [list(map(int,input().split())) for _ in range(H)]

def gravity():
    for i in range(W):
        start = -1
        while 1:
            if arr[start][i] != 0:
                start -= 1
                if abs(start) == H+1:
                    break
            else: # 0이면, 이제 여기에다 위의 0아닌 벽돌들을 떨어트릴 것. 여기가 시작점임. 그 아래는 이미 채워져있으니 중력ㄴㄴ
                break
        if abs(start) == H+1:
            continue
        else:
            now,space = start, start
            while 1:
                if arr[now][i] == 0:
                    now -= 1
                else:
                    arr[now][i],arr[space][i] = arr[space][i],arr[now][i]
                    space -= 1
                if abs(now) == H+1:
                    break

gravity()
print(arr)