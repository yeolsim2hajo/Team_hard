# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# trees = list(map(int, input().split()))

# meter = 1
# index = 0
# take_tree = 0

# while True:
#     if take_tree == M:
#         break

#     temp = 0
#     for i in range(N):
#         if trees[i] <= meter:
#             temp +=  0
#         else:
#             temp += trees[i] - meter
        
#         if temp > M:
#             break

#     take_tree = temp
#     if take_tree != M:
#         meter += 1

# print(meter)

# # 시간초과


# 이분탐색 알고리즘 쓰기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start+end) // 2
    cutting = 0

    for tree in trees:
        if tree > mid:
            cutting += tree - mid
        
    if cutting >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)




