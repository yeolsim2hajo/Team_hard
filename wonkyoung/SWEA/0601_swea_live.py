# 세제곱근을 찾아라
# T = int(input())
# for tc in range(1,1+T):
#     N = int(input())
#     if N == 1:
#         answer = 1
#     else:
#         start = 1
#         end = N // 2
#         answer = -1
#         while start <= end:
#             mid = (start + end) // 2
#             calc = mid ** 3
#             if calc == N:
#                 answer = mid
#                 break
#             elif calc < N:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#     print(f'#{tc} {answer}')


# 정사각형 방 - dfs
# T = int(input())
# def move(y,x, cnt, number):
#     global max_cnt, room
#     if cnt > max_cnt:
#         max_cnt = cnt
#         room = number
#     elif cnt == max_cnt and room > number:
#         room = number
#
#     for dy,dx in (-1,0), (1,0), (0,-1), (0,1):
#         ny, nx = y+dy, x+dx
#         if 0 <= ny < N and 0 <= nx < N:
#             if rooms[ny][nx] == rooms[y][x] + 1:
#                 move(ny,nx, cnt+1, number)
#                 break
#
#
# for tc in range(1,1+T):
#     N = int(input())
#     rooms = [list(map(int,input().split())) for _ in range(N)]
#     max_cnt = 1
#     room = 0
#     for i in range(N):
#         for j in range(N):
#             if rooms[i][j] != N ** 2:
#                 move(i,j,1,rooms[i][j])
#     print(f'#{tc} {room} {max_cnt}')


#정사각형 방 - DAT
# T = int(input())
# for tc in range(1,1+T):
#     N = int(input())
#     numbers = [0] * (N**2+1)
#     for i in range(N):
#         rooms = list(map(int,input().split()))
#         for j in range(N):
#             idx = rooms[j]
#             numbers[idx] = (i,j)
#     max_cnt = cnt = 1
#     room = 1
#     for i in range(1,N**2): # 0과 마지막 숫자 뺌
#         if cnt == 1:
#             start = i
#         now_y, now_x = numbers[i]
#         next_y, next_x = numbers[i+1]
#         if (now_y - next_y, now_x - next_x) in {(-1,0), (1,0), (0,1), (0,-1)}:
#             cnt += 1
#         else:
#             if cnt > max_cnt:
#                 max_cnt = cnt
#                 room = start
#             cnt = 1
#     if cnt > max_cnt:
#         max_cnt = cnt
#         room = start
#
#     print(f'#{tc} {room} {max_cnt}')


#장훈이의 높은 선반
T = int(input())
def find_dif(total=0, start=0):
    global max_sum, min_dif
    if min_dif == 0:
        return
    if total == min_dif:
        min_dif = 0
        return
    elif total < min_dif:
        if max_sum < total:
            max_sum = total
    else:
        return
    for i in range(start,N):
        path.append(heights[i])
        find_dif(total+heights[i],i+1)
        path.pop()

for tc in range(1,1+T):
    N, B = map(int,input().split())
    heights = list(map(int, input().split()))
    total = sum(heights)
    min_dif = total - B
    max_sum = 0
    path = []
    if min_dif:
        find_dif()
        if min_dif:
            min_dif -= max_sum
    print(f'#{tc} {min_dif}')