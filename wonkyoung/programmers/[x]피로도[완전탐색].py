# 220917
# 피로도 - 완전탐색
# def solution(k, dungeons):
#     answer = 0
#     dungeons = [element for element in dungeons if element[0] <= k]
#     print(dungeons)
#     limit = len(dungeons)
#     def dfs(level, now, cnt):
#         nonlocal answer
#         if answer == limit or now <= 0:
#             return
#         if level == limit:
#             answer = max(cnt, answer)
#             return
#         for min_need, use in dungeons:
#             if min_need <= now:
#                 dfs(level+1, now - use, cnt+1)
#             dfs(level+1, now, cnt)
#
#     dfs(0, k, 0)
#     return answer
