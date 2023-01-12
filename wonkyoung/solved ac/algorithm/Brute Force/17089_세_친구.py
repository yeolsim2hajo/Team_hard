#221012
# N, M = map(int, input().split())
# relation = [set() for _ in range(1+N)]
# for _ in range(M):
#     one, two = map(int, input().split())
#     relation[one].add(two)
#     relation[two].add(one)
# total = 3*N
# for i in range(1, N-1):
#     for j in relation[i]:
#         for k in relation[j]:
#             if k in relation[i]:
#                 total = min(len(relation[i]) + len(relation[j]) + len(relation[k]), total)
# if total == 3*N:
#     total = -1
# else:
#     total -= 6
# print(total)





# sys 사용 - 시간 더 걸림
import sys

new_input = sys.stdin.readline
N, M = map(int, new_input().split())
relation = [set() for _ in range(1+N)]
for _ in range(M):
    one, two = map(int, new_input().split())
    relation[one].add(two)
    relation[two].add(one)
total = 3*N
for i in range(1, N-1):
    for j in relation[i]:
        for k in relation[j]:
            if k in relation[i]:
                total = min(len(relation[i]) + len(relation[j]) + len(relation[k]), total)
if total == 3*N:
    total = -1
else:
    total -= 6
print(total)

