#230214
# def solution(n):
#     fibonacci = [0, 1]
#     for i in range(2, n+1):
#         fibonacci.append(fibonacci[-1]+fibonacci[-2])
#     return fibonacci[n]%1234567
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.28ms, 10.2MB)
테스트 8 〉	통과 (0.14ms, 10.2MB)
테스트 9 〉	통과 (0.07ms, 10.3MB)
테스트 10 〉	통과 (0.33ms, 10.1MB)
테스트 11 〉	통과 (0.10ms, 10.2MB)
테스트 12 〉	통과 (0.15ms, 10.3MB)
테스트 13 〉	통과 (447.38ms, 456MB)
테스트 14 〉	통과 (441.70ms, 439MB)
'''

#
def solution(n):
    fibonacci = [0, 1]
    for i in range(2, n+1):
        answer = fibonacci[-1]+fibonacci[-2]
        fibonacci.append(answer%1234567)
    return fibonacci[n]
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.21ms, 10.3MB)
테스트 8 〉	통과 (0.13ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.24ms, 10.1MB)
테스트 11 〉	통과 (0.13ms, 10.2MB)
테스트 12 〉	통과 (0.08ms, 10.1MB)
테스트 13 〉	통과 (14.87ms, 13.7MB)
테스트 14 〉	통과 (14.69ms, 13.8MB)
'''