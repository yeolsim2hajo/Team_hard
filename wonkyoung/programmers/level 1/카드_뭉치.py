#230220
# def solution(cards1, cards2, goal):
#     cards1 = cards1[::-1]
#     cards2 = cards2[::-1]
#     for element in goal:
#         if cards1 and cards1[-1] == element:
#             cards1.pop()
#         elif cards2 and cards2[-1] == element:
#             cards2.pop()
#         else:
#             return 'No'
#     return 'Yes'
'''
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.00ms, 9.97MB)
테스트 3 〉	통과 (0.00ms, 10MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10MB)
테스트 13 〉	통과 (0.00ms, 10MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 9.98MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.00ms, 10MB)
테스트 20 〉	통과 (0.01ms, 10.1MB)
테스트 21 〉	통과 (0.00ms, 10.1MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.00ms, 10MB)
테스트 24 〉	통과 (0.01ms, 10.2MB)
테스트 25 〉	통과 (0.01ms, 10.3MB)
'''
def solution(cards1, cards2, goal):
    from collections import deque
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for element in goal:
        if cards1 and cards1[0] == element:
            cards1.popleft()
        elif cards2 and cards2[0] == element:
            cards2.popleft()
        else:
            return 'No'
    return 'Yes'
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 9.98MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.02ms, 10MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.1MB)
테스트 20 〉	통과 (0.01ms, 10.1MB)
테스트 21 〉	통과 (0.01ms, 10.1MB)
테스트 22 〉	통과 (0.02ms, 10.1MB)
테스트 23 〉	통과 (0.01ms, 10MB)
테스트 24 〉	통과 (0.01ms, 10.1MB)
테스트 25 〉	통과 (0.01ms, 10.3MB)
'''