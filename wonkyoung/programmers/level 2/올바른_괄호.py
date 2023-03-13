#230313
# stack
# def solution(s):
#     stack = []
#     try:
#         for bracket in s:
#             if bracket == '(':
#                 stack.append(bracket)
#             else:
#                 stack.pop()
#     except IndexError:
#         return False
#     if stack:
#         return False
#     return True
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.02ms, 9.96MB)
효율성  테스트
테스트 1 〉	통과 (6.64ms, 10.4MB)
테스트 2 〉	통과 (6.06ms, 10.5MB)
'''

#
def solution(s):
    cnt = 0
    for bracket in s:
        if bracket == '(':
            cnt += 1
        elif cnt:
            cnt -= 1
        else:
            return False
    return cnt == 0
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (5.22ms, 10.2MB)
테스트 2 〉	통과 (5.52ms, 10.2MB)
'''