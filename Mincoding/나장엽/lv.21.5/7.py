from types import DynamicClassAttribute


arr = [ 
    [0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0],
    [0,1,2,0,2,1,0],
    [0,0,1,2,1,0,0],
    [0,0,2,1,0,1,0],
    [0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0]
]

y, x = map(int, input().split())
# arr[y][x] = 1
# # 상 하 좌 우
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# result = 0
# cnt = 0
# for i in range(7):
#     for k in range(7):
#         if arr[i][k] == 2:
#             if arr[i-1][k] and arr[i+1][k] and arr[i][k-1] and arr[i][k+1] == 1:
#                 cnt += 1
                
# print(cnt)



def eat(y, x):
    direct = [
        #상 우 하 좌 
        [-1, 0, 1, 0],
        [0, 1, 0, -1]
    ]
    for i in range(4):
        ny = y + direct[0][i]
        nx = x + direct[1][i]
        if ny < 0 or nx < 0 or ny >= 7 or nx >= 7:
            return 0
        if arr[ny][nx] != 1:
            return 0
    return 1

arr[y][x] = 1
cnt = 0
for i in range(7):
    for k in range(7):
        if arr[i][k] == 2:
            f = eat(i,k)
            if f == 1:
                cnt+= 1
print(cnt)