arr = []
for i in range(5):
    arr.append(list(map(int,input().split())))

# direct쓰는건가?
dx = [-1,-1,-1,0,0,1,1,1] # 11시부터 1렬 쭈욱, 그 다음 행 1렬 쭈욱 ...
dy = [-1,0,1,-1,1,-1,0,1]

def check(x,y):
    status = ''
    for i in range(8):
        status = 'good'
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0<= ny < 4:
            if arr[nx][ny] == 1:
                status = 'bad'
                break
    return status

def check2():
    result = '안정된 상태'
    for i in range(5):
        for j in range(4):
            if arr[i][j] == 1:
                if check(i,j) == 'bad':
                    result = '불안정한 상태'
    return result
# 함수 하나 더 만들어서 break 이중탈출 해결함 ^^:;

print(check2())
