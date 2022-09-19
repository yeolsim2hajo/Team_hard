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


# 같은 숫자는 싫어
def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

def solution(arr):
    num = arr[0]
    answer = [num]
    for i in range(1,len(arr)):
        if arr[i] != num:
            answer.append(arr[i])
            num = arr[i]
    return answer