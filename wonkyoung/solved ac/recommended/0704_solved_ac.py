#2156 포도주 시식
# import sys
# from collections import deque
# N = int(input())
# new_input = sys.stdin.readline
# wine = [int(new_input()) for _ in range(N)]
# max_wine = 0
# q = deque([(wine[0], wine[0], 1, 1), (0,0,0,1)])
# while q:
#     now, total, cnt, start = q.popleft()
#     print(now, total, cnt, start)
#     if total > max_wine:
#         max_wine = total
#     for i in range(start, N):
#         if i != start:
#             q.append((wine[i], total+wine[i], 1, i+1))
#         elif cnt <= 1:
#             q.append((wine[i], total+wine[i], cnt+1, i+1))
#     q.append((now, total, cnt, 1))
# print(max_wine)


#17266 어두운 굴다리
# 틀림
# N = int(input())
# M = int(input())
# lamp = list(map(int, input().split()))
# min_height = max(lamp[0], N - lamp[-1])
# for i in range(1,M):
#     min_height = max(round((lamp[i] - lamp[i-1])/2), min_height)
# print(min_height)


#20291 파일 정리
import sys
N = int(input())
cnt = {}
new_input = sys.stdin.readline
for _ in range(N):
    file = new_input().rstrip().split('.')
    cnt.setdefault(file[-1], 0)
    cnt[file[-1]] += 1
# keys = sorted(cnt)
keys = sorted(cnt.keys())
for key in keys:
    print(key,cnt[key])



