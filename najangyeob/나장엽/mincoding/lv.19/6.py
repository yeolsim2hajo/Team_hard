arr = [['_','_','_','_','_'],['_','_','_','_','_'],['_','_','_','_','_'],['_','_','_','_','_',]]


# 폭탄이 투하될 좌표 2개 입력받고
# 폭탄 투하된 좌표 8방향으로 폭탄이 터짐~
# direct를 사용해보자~

#(0,0) (0,1) (0,2) 
#(1,0) (1,1) (1,2)          (1,1)에 폭탄이 투하되면~?
#(2,0) (2,1) (2,2)

#(-1,-1) (-1,0) (-1,1)
#(0,-1)        (0,1)
#(1,-1) (1,0) (1,1)

#왼위 위 오위 왼 오 왼아 아 오아 
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

# 좌표값이 입력되면 for문 돌려서 ny, nx~ arr[ny][nx]에 # 저장~


y, x = map(int, input().split())
for z in range(8):
    ny = y + dy[z]
    nx = x + dx[z]
    if 0<= nx < 5 and 0<= ny < 4:
        arr[ny][nx] = '#'


y, x = map(int, input().split())
for s in range(8):
    ny = y + dy[s]
    nx = x + dx[s]
    if 0 <= nx < 5 and 0 <= ny < 4:
        arr[ny][nx] = '#'


for row in range(4):
    for col in range(5):
        print(arr[row][col], end=' ')
    print()