#1166 선물
# N, *box = map(int, input().split())
# min_val = min(box)
# def divide(a):
#     return a/min_val
# calc = list(map(divide, box))
# if calc[0] * calc[1] * calc[2] == N:
#     answer = min_val
#
#
#     start = 1
#     end = min(box)
#     while end >= start:
#
#     print(calc)
# elif box[0] * box[1] * box[2] == N:
#     pass
# else:

# if L * W * H > N:
#     pass
# else:
#     answer = min(L, W, H) / N
# print(answer)


#17266 어두운 굴다리
# N = int(input())
# M = int(input())
# lamp = list(map(int, input().split()))
# min_height = max(lamp[0], N - lamp[-1])
# for i in range(1,M):
#     min_height = max(round((lamp[i] - lamp[i-1])/2), min_height)
# print(min_height)


#2138 전구와 스위치
# N = int(input())
# initial = list(map(str, input()))
# target = list(map(str, input()))
# def bfs():
#     from collections import deque
#     q = deque()
#     q.append((initial, 0))
#     visited = set()
#     visited.add(initial)
#     check = {'0' : '1', '1' : '0'}
#     while q:
#         now, cnt = q.popleft()
#         if now == target:
#             return cnt
#         for i in range(N):
#             new = now[:]
#             for j in range(i-1, i+2):
#                 new[j] = check[new[j]]
#             if new not in visited:
#                 visited.add(new)
#                 q.append(new)
#     return -1
# print(bfs())


#15921 수찬이는 마린보이야
N = int(input())
if N:
    practice = list(map(int, input().split()))
    avg = sum(practice)/N
    check = [0] * 101
    for i in range(N):
        check[practice[i]] += 1
    value = 0
    for i in range(1,101):
        if check[i]:
            value += check[i] * i
    if value:
        print(f'{avg/(value/N):.2f}')
    else:
        print('divide by zero')
else:
        print('divide by zero')
