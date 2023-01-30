# 220917
# 틀림
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

#230124
def solution(k, dungeons):
    answer = 0
    length = len(dungeons)
    visited = [False] * length
    def dfs(level, now):
        nonlocal answer
        if level > answer:
            answer = level
        for i in range(length):
            if dungeons[i][0] <= now and not visited[i]:
                visited[i] = True
                dfs(level+1, now - dungeons[i][1])
                visited[i] = False
    dfs(0, k)
    return answer
'''
테스트 1 〉	통과 (0.03ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.23ms, 10.2MB)
테스트 5 〉	통과 (0.91ms, 10.3MB)
테스트 6 〉	통과 (2.56ms, 10.1MB)
테스트 7 〉	통과 (16.24ms, 10.2MB)
테스트 8 〉	통과 (43.14ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.86ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (1.87ms, 10.1MB)
테스트 13 〉	통과 (0.25ms, 10.1MB)
테스트 14 〉	통과 (0.08ms, 10.2MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.06ms, 10.1MB)
테스트 17 〉	통과 (0.16ms, 10.1MB)
테스트 18 〉	통과 (0.02ms, 10.1MB)
테스트 19 〉	통과 (0.07ms, 10.1MB)
'''