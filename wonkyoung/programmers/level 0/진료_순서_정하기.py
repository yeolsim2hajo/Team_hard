#230123
def solution(emergency):
    length = len(emergency)
    emergency = list(enumerate(emergency))
    emergency.sort(key=lambda x: -x[1])
    answer = [0] * length
    for i in range(length):
        answer[emergency[i][0]] = i+1
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 9.95MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10MB)
테스트 8 〉	통과 (0.01ms, 9.94MB)
'''

#
# def solution(emergency):
#     numbers = [-1] * 101
#     length = len(emergency)
#     for i in range(length):
#         numbers[emergency[i]] = i
#     answer = [0] * length
#     rank = length
#     for i in range(1, 101):
#         number = numbers[i]
#         if number != -1:
#             answer[number] = rank
#             rank -= 1
#     return answer
'''
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 9.96MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
'''