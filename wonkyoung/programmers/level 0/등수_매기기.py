#230202
# 틀림
# def solution(score):
#     length = len(score)
#     sorted_result = [[sum(score[i])//2, length-i] for i in range(length)]
#     sorted_result.sort()
#     answer = [0] * length
#     answer[sorted_result[0][1]] = 1
#     cnt = 0
#     for i in range(1, length):
#         avg, j = sorted_result[i]
#         if sorted_result[i-1][0] == avg:
#             sorted_result[i][1] = sorted_result[i-1][1]
#             answer[j-1] = i-cnt
#             cnt += 1
#         else:
#             answer[j-1] = i+1
#             cnt = 0
#     return answer

#230221
def solution(score):
    length = len(score)
    sorted_result = [[sum(score[i]), i] for i in range(length)]
    sorted_result.sort(reverse=True)
    answer = [0] * length
    answer[sorted_result[0][1]] = 1
    rank = 1
    cnt = 0
    for i in range(1, length):
        avg, j = sorted_result[i]
        if sorted_result[i-1][0] != avg:
            rank += 1 + cnt
            cnt = 0
        else:
            cnt += 1
        answer[j] = rank
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
'''