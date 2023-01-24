#230124
def solution(record):
    answer = []
    match = {}
    for info in record:
        if info.startswith('Leave'):
            command, uid = info.split()
            answer.append([uid, '님이 나갔습니다.'])
        else:
            command, uid, nickname = info.split()
            if command == 'Enter':
                answer.append([uid, '님이 들어왔습니다.'])
            match[uid] = nickname
    length = len(answer)
    for i in range(length):
        uid = answer[i][0]
        answer[i][0] = match[uid]
        answer[i] = ''.join(answer[i])
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.60ms, 10.4MB)
테스트 6 〉	통과 (0.66ms, 10.2MB)
테스트 7 〉	통과 (0.50ms, 10.4MB)
테스트 8 〉	통과 (0.77ms, 10.4MB)
테스트 9 〉	통과 (0.85ms, 10.5MB)
테스트 10 〉	통과 (0.67ms, 10.5MB)
테스트 11 〉	통과 (0.37ms, 10.2MB)
테스트 12 〉	통과 (0.38ms, 10.4MB)
테스트 13 〉	통과 (0.64ms, 10.4MB)
테스트 14 〉	통과 (0.76ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.07ms, 10.2MB)
테스트 18 〉	통과 (0.06ms, 10.2MB)
테스트 19 〉	통과 (0.71ms, 10.5MB)
테스트 20 〉	통과 (0.52ms, 10.3MB)
테스트 21 〉	통과 (0.52ms, 10.2MB)
테스트 22 〉	통과 (0.50ms, 10.2MB)
테스트 23 〉	통과 (0.74ms, 10.4MB)
테스트 24 〉	통과 (0.72ms, 10.5MB)
테스트 25 〉	통과 (88.24ms, 47.2MB)
테스트 26 〉	통과 (128.41ms, 51.4MB)
테스트 27 〉	통과 (119.64ms, 54.8MB)
테스트 28 〉	통과 (108.83ms, 57MB)
테스트 29 〉	통과 (105.77ms, 57MB)
테스트 30 〉	통과 (70.46ms, 43.5MB)
테스트 31 〉	통과 (78.65ms, 54.1MB)
테스트 32 〉	통과 (70.01ms, 46.5MB)
'''

# 함수화 => 시간 더 걸림
# def solution(record):
#     def fill_answer():
#         for info in record:
#             if info.startswith('Leave'):
#                 command, uid = info.split()
#                 answer.append([uid, '님이 나갔습니다.'])
#             else:
#                 command, uid, nickname = info.split()
#                 if command == 'Enter':
#                     answer.append([uid, '님이 들어왔습니다.'])
#                 match[uid] = nickname
#     answer = []
#     match = {}
#     fill_answer()
#     length = len(answer)
#     for i in range(length):
#         uid = answer[i][0]
#         answer[i][0] = match[uid]
#         answer[i] = ''.join(answer[i])
#     return answer


# message 변수로 => 시간 더 걸림
# def solution(record):
#     answer = []
#     match = {}
#     for info in record:
#         messages = ['님이 나갔습니다.', '님이 들어왔습니다.']
#         if info.startswith('Leave'):
#             command, uid = info.split()
#             answer.append([uid, messages[0]])
#         else:
#             command, uid, nickname = info.split()
#             if command == 'Enter':
#                 answer.append([uid, messages[1]])
#             match[uid] = nickname
#     length = len(answer)
#     for i in range(length):
#         uid = answer[i][0]
#         answer[i][0] = match[uid]
#         answer[i] = ''.join(answer[i])
#     return answer


# 나중에 append
def solution(record):
    answer, match = [], {}
    for info in record:
        if not info.startswith('Leave'):
            command, uid, nickname = info.split()
            match[uid] = nickname
    for info in record:
        if info.startswith('Leave'):
            command, uid = info.split()
            answer.append(f'{match[uid]}님이 나갔습니다.')
        elif info.startswith('Enter'):
            command, uid, nickname = info.split()
            answer.append(f'{match[uid]}님이 들어왔습니다.')
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.60ms, 10.3MB)
테스트 6 〉	통과 (0.63ms, 10.4MB)
테스트 7 〉	통과 (0.53ms, 10.4MB)
테스트 8 〉	통과 (0.63ms, 10.3MB)
테스트 9 〉	통과 (0.79ms, 10.4MB)
테스트 10 〉	통과 (0.64ms, 10.4MB)
테스트 11 〉	통과 (0.41ms, 10.3MB)
테스트 12 〉	통과 (0.41ms, 10.3MB)
테스트 13 〉	통과 (0.64ms, 10.3MB)
테스트 14 〉	통과 (0.83ms, 10.4MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.07ms, 10.3MB)
테스트 18 〉	통과 (0.06ms, 10.1MB)
테스트 19 〉	통과 (0.68ms, 10.4MB)
테스트 20 〉	통과 (0.56ms, 10.3MB)
테스트 21 〉	통과 (0.54ms, 10.3MB)
테스트 22 〉	통과 (0.56ms, 10.3MB)
테스트 23 〉	통과 (0.65ms, 10.5MB)
테스트 24 〉	통과 (0.68ms, 10.4MB)
테스트 25 〉	통과 (71.13ms, 38.9MB)
테스트 26 〉	통과 (84.45ms, 39.6MB)
테스트 27 〉	통과 (92.74ms, 41.2MB)
테스트 28 〉	통과 (94.75ms, 42.5MB)
테스트 29 〉	통과 (96.63ms, 42.4MB)
테스트 30 〉	통과 (68.85ms, 36.6MB)
테스트 31 〉	통과 (83.65ms, 41.2MB)
테스트 32 〉	통과 (63.89ms, 38.3MB)
'''