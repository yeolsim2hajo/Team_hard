#11727 2xn 타일링
# N = int(input())
# case = [1, 1, 3]
# def dfs(total=0, cnt=0):
#     global case
#     if total > N:
#         return
#     if total == N:
#         case += cnt*2
#         return
#     for i in range(1,3):
#         dfs(total+i, cnt+i-1)
# dfs()
# print(case%10007)




# import sys
#
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# points = sorted(map(int, new_input().split()))
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     min_idx, max_idx = 0, N-1
#     cnt = []
#     # 끝 값 찾기
#     while min_idx <= max_idx:
#         idx = (min_idx + max_idx)//2
#         if points[idx] == end:
#             max_idx = idx
#             break
#         elif points[idx] < end:
#             min_idx = idx + 1
#         else:
#             max_idx = idx - 1
#     end_idx = max_idx
#     min_idx = 0
#     while min_idx <= end_idx:
#         idx = (min_idx + end_idx)//2
#         if start == points[idx]:
#             min_idx = idx
#             break
#         elif start < points[idx]:
#             end_idx = idx - 1
#         else:
#             min_idx = idx + 1
#     print(max_idx-end_idx+1)



# students = { int(input()) for _ in range(28)}
# print(*sorted(set(range(1,31)) - students), sep='\n')


# students = { int(input()) for _ in range(28)}
# for i in range(1,31):
#     if i not in students:
#         print(i)

