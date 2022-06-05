#1003 피보나치 함수
# import sys
# T = int(input())
# new_input = sys.stdin.readline
# numbers = [[1,0],[0,1]]
# for _ in range(T):
#     N = int(new_input())
#     if N > 1:
#         zero = one = 0
#         number = len(numbers)
#         while number <= N:
#             zero = numbers[number-1][0] + numbers[number-2][0]
#             one = numbers[number-1][1] + numbers[number-2][1]
#             numbers.append([zero, one])
#             number += 1
#     print(*numbers[N])


#1012 유기농 배추
# set 이용
# import sys
# T = int(input())
#
# def bfs(*args):
#     global earthworm
#     earthworm += 1
#     q = [args]
#     while q:
#         y,x = q.pop(0)
#         for dy,dx in (-1,0), (1,0), (0,1), (0,-1):
#             ny,nx = y+dy, x+dx
#             if (ny,nx) in position:
#                 position.remove((ny,nx))
#                 q.append((ny,nx))
#
# for _ in range(T):
#     M, N, K = map(int,input().split())
#     new_input = sys.stdin.readline
#     position = set()
#     for _ in range(K):
#         X, Y = map(int,new_input().split())
#         position.add((Y,X))
#     earthworm = 0
#     while position:
#         Y,X = position.pop()
#         bfs(Y,X)
#     print(earthworm)

# 원래 하던 방법 - 위와 큰 차이가 나지는 않음
import sys
T = int(input())
def bfs(*args):
    global earthworm
    earthworm += 1
    q = [args]
    while q:
        y,x = q.pop(0)
        for dy,dx in (-1,0), (1,0), (0,1), (0,-1):
            ny,nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M:
                if ground[ny][nx]:
                    ground[ny][nx] = 0
                    q.append((ny,nx))

for _ in range(T):
    M, N, K = map(int,input().split())
    ground = [[0] * M for _ in range(N)]
    new_input = sys.stdin.readline
    for _ in range(K):
        X, Y = map(int,new_input().split())
        ground[Y][X] = 1
    earthworm = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j]:
                ground[i][j] = 0
                bfs(i,j)
    print(earthworm)



