#230315
# def solution(s):
#     length = len(s)
#     new_s = []
#     start_i = 0
#     for i in range(1, length-1):
#         alp = s[i]
#         if alp == '{':
#             start_i = i+1
#         elif alp == '}':
#             num_list = set(map(int, s[start_i:i].split(',')))
#             new_s.append(num_list)
#     new_s.sort(key= lambda x: len(x))
#     answer = [0] * len(new_s[-1])
#     before = set()
#     index = 0
#     for element in new_s:
#         num_set = element - before
#         answer[index] = num_set.pop()
#         index += 1
#         before = element
#     return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.32ms, 10.3MB)
테스트 6 〉	통과 (0.70ms, 10.4MB)
테스트 7 〉	통과 (12.50ms, 12MB)
테스트 8 〉	통과 (32.96ms, 15.7MB)
테스트 9 〉	통과 (18.21ms, 12.7MB)
테스트 10 〉	통과 (33.61ms, 16MB)
테스트 11 〉	통과 (48.35ms, 18.6MB)
테스트 12 〉	통과 (85.94ms, 22.7MB)
테스트 13 〉	통과 (79.39ms, 22.4MB)
테스트 14 〉	통과 (96.86ms, 22.8MB)
테스트 15 〉	통과 (0.02ms, 10.5MB)
'''


#
# def solution(s):
#     length = len(s)
#     new_s = []
#     start_i = 0
#     for i in range(1, length-1):
#         alp = s[i]
#         if alp == '{':
#             start_i = i+1
#         elif alp == '}':
#             num_list = set(map(int, s[start_i:i].split(',')))
#             new_s.append(num_list)
#     new_s.sort(key= lambda x: len(x))
#     answer = []
#     before = set()
#     for element in new_s:
#         num_set = element - before
#         answer.append(num_set.pop())
#         before = element
#     return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.10ms, 10.3MB)
테스트 5 〉	통과 (0.30ms, 10.4MB)
테스트 6 〉	통과 (0.68ms, 10.5MB)
테스트 7 〉	통과 (10.30ms, 12MB)
테스트 8 〉	통과 (41.12ms, 15.7MB)
테스트 9 〉	통과 (24.26ms, 12.8MB)
테스트 10 〉	통과 (38.42ms, 16MB)
테스트 11 〉	통과 (52.06ms, 18.7MB)
테스트 12 〉	통과 (83.10ms, 22.7MB)
테스트 13 〉	통과 (102.23ms, 22.5MB)
테스트 14 〉	통과 (98.99ms, 22.8MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
'''


#
def solution(s):
    length = len(s)
    new_s = []
    start_i = 0
    for i in range(1, length-1):
        alp = s[i]
        if alp == '{':
            start_i = i+1
        elif alp == '}':
            num_list = set(map(int, s[start_i:i].split(',')))
            new_s.append(num_list)
    new_s.sort(key=lambda x: len(x))
    answer = [0] * len(new_s)
    before = set()
    index = 0
    for element in new_s:
        num_set = element - before
        answer[index] = num_set.pop()
        index += 1
        before = element
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.10ms, 10.4MB)
테스트 5 〉	통과 (0.35ms, 10.4MB)
테스트 6 〉	통과 (0.65ms, 10.5MB)
테스트 7 〉	통과 (11.26ms, 11.8MB)
테스트 8 〉	통과 (56.94ms, 15.7MB)
테스트 9 〉	통과 (33.95ms, 12.8MB)
테스트 10 〉	통과 (41.14ms, 16.2MB)
테스트 11 〉	통과 (89.33ms, 18.7MB)
테스트 12 〉	통과 (141.01ms, 22.6MB)
테스트 13 〉	통과 (124.23ms, 22.6MB)
테스트 14 〉	통과 (144.43ms, 22.9MB)
테스트 15 〉	통과 (0.04ms, 10.4MB)
'''