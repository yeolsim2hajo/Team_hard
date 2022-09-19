#85 숫자 놀이
# def dfs(arg=1):
#     global ans,path
#     if arg == n:
#         print(*ans,sep='')
#         return
#     ans = []
#     for i in range(1,max(path)+1):
#         j = first = 0
#         while j < len(path):
#             if path[j] == i and first == 0:
#                 ans.append(i)
#                 first = 1
#                 ans.append(path.count(i))
#                 j += 2
#             else:
#                 j += 1
#     path = ans[:]
#     dfs(arg+1)
#
# n = int(input())
# path = [1]
# ans = []
# dfs()


#86 회전 초밥 - 다시
# def rot(arg=0):
#     global cnt
#     if arg == dish:
#         return
#     for i in range(length+1):
#         if check[i]:
#             check[i] -= 1
#             for j in range(length):
#                 
# 
# point = list(map(int,input().split()))
# dish = int(input())
# length = len(point)
# check = [0]*(length+1)
# visited = [0]*length
# for i in range(length):
#     check[point[i]] += 1
# cnt = 0
# rot()
# print(cnt)