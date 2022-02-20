map = [[3,3,5,3,1], [2,2,4,2,6], [4,9,2,3,4], [1,1,1,1,1], [3,3,5,9,2]]

dx = [-1,-1,1,1] # 11시 시작, 시계방향 , x는 행
dy = [-1,1,-1,1] # y는 열

def sum(x,y):
    sum1 = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < 5 and 0 <= ny and ny < 5:
            sum1 += map[nx][ny]
    return sum1

max = 0
max_position = (0,0)
for i in range(5):
    for j in range(5):
        if sum(i,j) > max:
            max = sum(i,j)
            max_position = (i,j)

print(*max_position)

# 원경 코드 - 1중포문으로 전부 해결 ㄷㄷㄷ;;
# --------------------------------------------
# arr = ['33531','22426','49234','11111','33592']
# map_arr = [list(map(int,arr[i])) for i in range(5)]

# def sum(y,x):
#     dy = [-1,1,-1,1]
#     dx = [-1,1,1,-1]
#     sum_data = 0
#     for j in range(4):
#         if 0 <= y+dy[j] < 5 and 0 <= x+dx[j] < 5:
#             sum_data += map_arr[y+dy[j]][x+dx[j]]
#     return sum_data

# sum(1,2)

# max_data = 0
# for index in range(25):
#     if max_data < sum(index//5,index%5):
#         max_data = sum(index//5,index%5)
#         ans = index
# print(ans//5, ans%5)
# --------------------------------------------