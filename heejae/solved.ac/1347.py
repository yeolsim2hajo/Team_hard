import sys

input = sys.stdin.readline

N = int(input())
action = input().strip()

# 0,0 부터 좌표 구하기
loc_list = [(0, 0)] 
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상 우 하 좌/ 북 동 남 서
status = 2
for a in action:
    if a == 'R':
        # 오른쪽
        status = (status + 1) % 4
    elif a == 'L':
        # 왼쪽
        status = (status - 1) if status != 0 else 3
    else:
        x = loc_list[-1][0] + dx[status]
        y = loc_list[-1][1] + dy[status]
        loc_list.append((x, y))
        
# x, y 의 최대 최소 구하기
x_sort = sorted(loc_list, key=lambda x: x[0])
y_sort = sorted(loc_list, key=lambda x: x[1])
x_min, x_max = x_sort[0][0], x_sort[-1][0]
y_min, y_max = y_sort[0][1], y_sort[-1][1]

# 2차원 배열 만들기
maze = [['#' for y in range(y_min, y_max + 1)] for x in range(x_min, x_max + 1)]

# 음수가 나올 수 있으므로 최소값만큼 더해주기 ( 양수로 바꾸기 )
for i in range(len(loc_list)):
    loc_list[i] = (loc_list[i][0] - x_min, loc_list[i][1] - y_min)

# 좌표로 길 만들기
for i, j in loc_list:
    maze[i][j] = '.'

# 답
for row in maze:
    print(''.join(row))