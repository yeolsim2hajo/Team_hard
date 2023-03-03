#230303
# def solution(n, results):
#     answer = 0
#     score_board = [[-1] * (n+1) for _ in range(n+1)]
#     for winner, loser in results:
#         score_board[winner][loser] = 1
#         score_board[loser][winner] = 0
#     for mid_person in range(1, n+1):
#         for person1 in range(1, n+1):
#             if person1 != mid_person:
#                 for person2 in range(1, n+1):
#                     if score_board[person1][person2] == -1:
#                         if score_board[person1][mid_person] == score_board[mid_person][person2] != -1:
#                             score_board[person1][person2] = score_board[person1][mid_person]
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i != j:
#                 if score_board[i][j] == -1:
#                     break
#         else:
#             answer += 1
#     return answer

'''
2, 5
 [[-1, -1, -1, -1, -1, -1],
 [-1, -1, 1, -1, -1, 1],
 [-1, 0, -1, 0, 0, 1],
 [-1, -1, 1, -1, 0, 1],
 [-1, -1, 1, 1, -1, 1],
 [-1, 0, 0, 0, 0, -1]]
'''
'''
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (0.10ms, 10.1MB)
테스트 4 〉	통과 (1.06ms, 10.2MB)
테스트 5 〉	통과 (1.77ms, 10.3MB)
테스트 6 〉	통과 (4.53ms, 10.1MB)
테스트 7 〉	통과 (23.11ms, 10.4MB)
테스트 8 〉	통과 (50.95ms, 10.4MB)
테스트 9 〉	통과 (95.97ms, 10.6MB)
테스트 10 〉	통과 (62.90ms, 10.5MB)
'''

#
# def solution(n, results):
#     answer = 0
#     score_board = [[-1] * (n+1) for _ in range(n+1)]
#     for winner, loser in results:
#         score_board[winner][loser] = 1
#         score_board[loser][winner] = 0
#     for mid_person in range(1, n+1):
#         for person1 in range(1, n):
#             if person1 != mid_person:
#                 for person2 in range(person1+1, n+1):
#                     if score_board[person1][person2] == -1:
#                         if score_board[person1][mid_person] == score_board[mid_person][person2] != -1:
#                             score_board[person1][person2] = score_board[person1][mid_person]
#                             score_board[person2][person1] = 1 - score_board[person1][mid_person]
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i != j:
#                 if score_board[i][j] == -1:
#                     break
#         else:
#             answer += 1
#     return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.10ms, 10MB)
테스트 4 〉	통과 (0.64ms, 10.2MB)
테스트 5 〉	통과 (1.02ms, 10.2MB)
테스트 6 〉	통과 (2.33ms, 10.4MB)
테스트 7 〉	통과 (10.93ms, 10.5MB)
테스트 8 〉	통과 (37.71ms, 10.4MB)
테스트 9 〉	통과 (30.67ms, 10.6MB)
테스트 10 〉	통과 (33.66ms, 10.8MB)
'''

#
def solution(n, results):
    answer = 0
    score_board = [[-1] * (n+1) for _ in range(n+1)]
    for winner, loser in results:
        score_board[winner][loser] = 1
        score_board[loser][winner] = 0
    for mid_person in range(1, n+1):
        for person1 in range(1, n):
            if person1 != mid_person:
                for person2 in range(person1+1, n+1):
                    if score_board[person1][person2] == -1:
                        one_to_mid = score_board[person1][mid_person]
                        mid_to_two = score_board[mid_person][person2]
                        if one_to_mid == mid_to_two != -1:
                            score_board[person1][person2] = one_to_mid
                            score_board[person2][person1] = 1 - one_to_mid
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                if score_board[i][j] == -1:
                    break
        else:
            answer += 1
    return answer
'''
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (1.24ms, 10.2MB)
테스트 5 〉	통과 (1.66ms, 10.2MB)
테스트 6 〉	통과 (2.44ms, 10.2MB)
테스트 7 〉	통과 (11.78ms, 10.3MB)
테스트 8 〉	통과 (22.87ms, 10.6MB)
테스트 9 〉	통과 (28.44ms, 10.7MB)
테스트 10 〉	통과 (29.05ms, 10.6MB)
'''