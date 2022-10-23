# 220916
# 시간 초과
# def solution(nums):
#     answer = 1
#     half = len(nums)//2
#     phone = {i: 0 for i in nums}
#     for i in nums:
#         phone[i] += 1
#     keys = phone.keys()
#     visited = []
#     def dfs(level):
#         nonlocal answer
#         if answer == half:
#             return
#         if level == half:
#             cnt = len(set(visited))
#             answer = max(answer, cnt)
#             return
#         for i in keys:
#             if phone[i] >= 1:
#                 phone[i] -= 1
#                 visited.append(i)
#                 dfs(level+1)
#                 visited.pop()
#                 phone[i] += 1
#     dfs(0)
#     return answer

# 딕셔너리만 이용하자!
def solution(nums):
    half = len(nums)//2
    phone = {i: 0 for i in nums}
    for i in nums:
        phone[i] += 1
    answer = min(len(phone), half)
    return answer