# 아기상어
# 메모리 초과
T = int(input())
def find_range(y,x,number):
    arr = set()
    for i in range(-number, number+1):
        for j in range(-number, number+1):
            if abs(i) + abs(j) <= number:
                if 1 <= y+i <= N and 1 <= x+j <= N:
                    arr.add((y+i, x+j))
    return arr

def attack(y,x,power):
    global impossible
    for nest in nest_info:
        if (y,x) in nest[1]:
            if power <= nest[0]:
                impossible = True
                return 0
            else:
                power -= nest[0]
    return power

def bfs():
    global min_path, impossible
    visited = set(baby)
    q = [*baby,M,0]
    while q:
        y,x,power,cnt = q.pop(0)
        if [y,x] == mom:
            min_path = cnt
            return
        for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
            ny, nx = y+dy, x+dx
            if 1 <= ny <= N and 1 <= nx <= N:
                if (ny,nx) not in visited:
                    visited.add((ny,nx))
                    new_power = attack(ny,nx,power)
                    if not new_power:
                        continue
                    q.append((ny,nx,new_power,cnt+1))

for tc in range(1,1+T):
    N, M, K = map(int,input().split())
    baby = list(map(int,input().split()))
    mom = list(map(int,input().split()))
    nest_info = []
    for _ in range(M):
        nest_y, nest_x, around, hard = map(int,input().split())
        nest_info.append([hard, find_range(nest_y, nest_x, around)])
    min_path = -1
    M = attack(*baby, M)
    if M:
        bfs()
    print(f'#{tc} {min_path}')



#다시
T = int(input())
def bfs():
    global min_path, impossible
    visited = set(baby)
    q = [*baby,M,0]
    while q:
        y,x,power,cnt = q.pop(0)
        if [y,x] == mom:
            min_path = cnt
            return
        for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
            ny, nx = y+dy, x+dx
            if 1 <= ny <= N and 1 <= nx <= N:
                if sea[ny][nx] != -1:
                    if sea[ny][nx] < power:
                        q.append((ny,nx,power-sea[ny][nx],cnt+1))
                    sea[ny][nx] = -1

for tc in range(1,1+T):
    N, M, K = map(int,input().split())
    sea = [[0] * N for _ in range(N)]
    baby = list(map(int,input().split()))
    mom = list(map(int,input().split()))
    for _ in range(M):
        nest_y, nest_x, around, hard = map(int,input().split())
        for i in range(-around, around + 1):
            for j in range(-around, around + 1):
                if abs(i) + abs(j) <= around:
                    ny, nx = nest_y + i, nest_x + j
                    if 1 <= ny <= N and 1 <= nx <= N:
                        sea[ny][nx] += hard
    min_path = -1
    if sea[baby[0]][baby[1]] < M:
        M -= sea[baby[0]][baby[1]]
        sea[baby[0]][baby[1]] = -1
        bfs()
    print(f'#{tc} {min_path}')


#수목원
# T = int(input())
# def calc_score(y,x,name,cnt,total):
#     global max_score, winner
#
#     for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
#         ny,nx = y+dy, x+dx
#         if 0 <= ny < 5 and 0 <= nx < 8:
#             value = board[ny][nx]
#             if value[0] ==
#             if visited[ny][nx] is False:
#                 visited[ny][nx] = True
#
#
#     if max_score < total:
#         max_score = total
#         winner = name
#     return 0
#
# def find_road(tree, name):
#     for i in range(5):
#         for j in range(8):
#             if board[i][j][0] == tree:
#                 calc_score(i,j,name,0,1)
# for tc in range(1,1+T):
#     N = int(input())
#     players = [input().split() for _ in range(N)]
#     board = [input().split() for _ in range(5)]
#     visited = [[False] * 8 for _ in range(5)]
#     winner = ''
#     max_score = 0
#     for player in players:
#         find_road(*player)
#     print(f'#{tc} {winner}')


#우리
# def find_answer(arg,start=0):
#     global min_student
#     if min_student != -1:
#         return
#     if arg == i:
#         for k in range(number):
#             result = set()
#             for element in path:
#                 result.update(element)
#             if result == set(range(N)):
#                 min_student = i
#         return
#     for j in range(start,N):
#         path.append(position[j])
#         find_answer(arg+1, j+1)
#         path.pop()
#
# for _ in range(50):
#     N = int(input())
#     answer = input()
#     number = len(answer)
#     min_student = -1
#     position = [set() for _ in range(N)]
#     for i in range(N):
#         student = input()
#         if min_student != 1 and answer == student:
#             min_student = 1
#         elif min_student ==  -1:
#             for j in range(number):
#                 if answer[j] == student[j]:
#                     position[i].add(j)
#
#     if min_student == -1:
#         for i in range(2,N+1):
#             path = []
#             find_answer(0)
#             if min_student != -1:
#                 break
#     print(min_student)


#아파트
T = int(input())
for tc in range(1,1+T):
    F, N = map(int, input().split())
    position = list(map(int,input().split()))
    length = len(position)
    # check = {}
    # for element in position:
    #     if check.get(element):
    #         check[element] += 1
    #     else:
    #         check[element] = 1
    bucket = [0] * (N+1)
    for element in position:
        bucket[element] += 1
    aliens = {}
    max_arm = 0
    for i in range(1,N+1):
        if aliens.get(bucket[i]):
            aliens[bucket[i]].add(i)
        else:
            aliens[bucket[i]] = {i}
            if bucket[i] > max_arm:
                max_arm = bucket[i]
    cnt = 0
    while cnt < F:
        if aliens[max_arm]:
            if position[0] not in aliens:
                position.append(position.pop(0))
            else:
                val = position.pop(0)
                aliens.get(max_arm-1).add(aliens[max_arm].remove(val))
        else:
            del aliens[max_arm]
            max_arm = max(aliens)
            if position[0] not in aliens:
                position.append(position.pop(0))
            else:
                val = position.pop(0)
                aliens.get(max_arm-1).add(aliens[max_arm].remove(val))

        cnt += 1
    print(f'#{tc} {position[0]}')

