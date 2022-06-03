#10845 큐
# from collections import deque
# from sys import stdin
# N = int(input())
# q = deque()
# size = 0
# for _ in range(N):
#     command = stdin.readline().rstrip()
#     if command == 'pop':
#         answer = q.popleft() if q else -1
#         size = size - 1 if size else 0
#     elif command == 'size':
#         answer = size
#     elif command == 'empty':
#         answer = 0 if size else 1
#     elif command == 'front':
#         answer = q[0] if q else -1
#     elif command == 'back':
#         answer = q[-1] if q else -1
#     else:
#         q.append(command.split()[1])
#         size += 1
#         continue
#     print(answer)

#10989 수 정렬하기 3
# 딕셔너리 활용
# from sys import stdin
# N = int(input())
# check = {}
# for _ in range(N):
#     key = int(stdin.readline())
#     if check.get(key):
#         check[key] += 1
#     else:
#         check[key] = 1
# keys = sorted(check)
# for key in keys:
#     for _ in range(check[key]):
#         print(key)

# DAT 활용 - 시간 덜 걸림
# from sys import stdin
# N = int(input())
# check = [0] * 10001
# for _ in range(N):
#     idx = int(stdin.readline())
#     check[idx] += 1
# for i in range(1,10001):
#     if check[i]:
#         for _ in range(check[i]):
#             print(i)

# DAT 활용 - 메모리 초과
# from sys import stdin
# N = int(input())
# check = [0] * 10001
# for _ in range(N):
#     idx = int(stdin.readline())
#     check[idx] += 1
# for i in range(1,10001):
#     if check[i]:
#         print(*[i]*check[i],sep='\n')

# 딕셔너리 활용 - 미리 키 값 만들어놓기 - DAT보다 더 걸림 - 첫 번째 방법보다는 덜 걸림
# from sys import stdin
# N = int(input())
# check = {i:0 for i in range(1,10001)}
# for _ in range(N):
#     key = int(stdin.readline())
#     check[key] += 1
# for key,value in check.items():
#     if value:
#         for _ in range(value):
#             print(key)


#18111 마인크래프트
from sys import stdin
N, M, B = map(int,input().split())
new_input = stdin.readline
heights = [0] * 257
start = 256
end = 0
for _ in range(N):
    ground = list(map(int,new_input().split()))
    for j in range(M):
        idx = ground[j]
        heights[idx] += 1
        if start > idx:
            start = idx
        if end < idx:
            end = idx
min_time = 256 * N * M
height = 0
# 높이 범위
for target in range(start, end+1):
    time = 0
    inventory = B
    # DAT 범위
    for idx in range(start,end+1):
        if heights[idx]:
            if target < idx:
                time += (idx-target) * 2 * heights[idx]
            elif target > idx:
                time += (target-idx) * heights[idx]
            inventory += (idx-target) * heights[idx]
    if inventory < 0: continue
    if min_time > time:
        min_time = time
        height = target
    elif min_time == time and height < target:
        height = target
print(min_time, height)

'''
3 4 0
62 64 64 64
62 64 64 64
62 64 64 62

3 4 10
62 64 64 64
62 64 64 64
62 64 64 62
'''

