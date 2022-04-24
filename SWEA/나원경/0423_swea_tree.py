# 장훈이의 높은 선반
# import sys
# sys.stdin = open('input (7).txt','r')
#
# def dfs(level=0, start=0, total=0):
#     global min_val
#     if total >= B:
#         if min_val > total:
#             min_val = total
#         return
#     for i in range(start, N):
#         if used[i] == False:
#             used[i] = True
#             dfs(level+1,i,total+height[i])
#             used[i] = False
#
# T = int(input())
# for tc in range(1,1+T):
#     N, B = map(int,input().split())
#     height = list(map(int,input().split()))
#     used = [False]*N
#     min_val = 2e5
#     dfs()
#     print(f'#{tc} {min_val - B}')