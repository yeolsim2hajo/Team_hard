#230122
def solution(num, k):
    try:
        answer = str(num).index(str(k)) + 1
    except Exception:
        answer = -1
    return answer
solution(29183, 1)
solution(29183, 1)
solution(123456, 7)
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10MB)
테스트 8 〉	통과 (0.00ms, 9.99MB)
'''
def solution(num, k):
    num, k = str(num), str(k)
    for i in range(len(num)):
        if num[i] == k:
            return i+1
    return -1
'''
테스트 1 〉	통과 (0.00ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
'''
