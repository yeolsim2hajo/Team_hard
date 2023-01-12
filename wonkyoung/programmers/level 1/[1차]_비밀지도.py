#230113
# def solution(n, arr1, arr2):
#     answer = []
#     for i in range(n):
#         element, num1, num2 = '', arr1[i], arr2[i]
#         for _ in range(n):
#             num1, remain1 = divmod(num1, 2)
#             num2, remain2 = divmod(num2, 2)
#             element += '#' if remain1 or remain2 else ' '
#         answer.append(element[::-1])
#     return answer
'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
'''

# 앞에 추가
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        element, num1, num2 = '', arr1[i], arr2[i]
        for _ in range(n):
            num1, remain1 = divmod(num1, 2)
            num2, remain2 = divmod(num2, 2)
            element = '#' + element if remain1 or remain2 else ' ' + element
        answer.append(element)
    return answer
'''

테스트 1 〉	통과 (0.03ms, 10.1MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
'''