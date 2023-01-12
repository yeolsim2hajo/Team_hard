#230112
def solution(n):
    from math import isqrt
    answer = 1 if isqrt(n) ** 2 == n else 2
    return answer
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
'''
def solution(n):
    for i in range(n-1):
        if i**2 > n:
            return 2
        elif i**2 == n:
            return 1
'''
테스트 1 〉	통과 (0.36ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.63ms, 10.1MB)
테스트 6 〉	통과 (0.07ms, 10.1MB)
테스트 7 〉	통과 (0.21ms, 10.3MB)
테스트 8 〉	통과 (0.38ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
'''
def solution(n):
    for i in range(n-1):
        square = i**2
        if square > n:
            return 2
        elif square == n:
            return 1
'''
테스트 1 〉	통과 (0.38ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.20ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.12ms, 10.3MB)
테스트 8 〉	통과 (0.12ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
'''

def solution(n):
    for i in range(1, n):
        square = i ** 2
        if square > n:
            return 2
        elif square == n:
            return 1
    return 1
'''
테스트 1 〉	통과 (0.20ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.20ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.12ms, 10.1MB)
테스트 8 〉	통과 (0.12ms, 10.1MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
'''

def solution(n):
    for i in range(1, n//2+1):
        quot, remain = divmod(n, i)
        if remain == 0:
            if quot < i:
                return 2
            elif quot == i:
                return 1
'''
테스트 1 〉	통과 (0.12ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.11ms, 10.1MB)
테스트 6 〉	통과 (2.30ms, 10.1MB)
테스트 7 〉	통과 (0.13ms, 10.2MB)
테스트 8 〉	통과 (0.08ms, 10.3MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
'''

def solution(n):
    half = n//2+1
    for i in range(1, half):
        quot, remain = divmod(n, i)
        if remain == 0:
            if quot < i:
                return 2
            elif quot == i:
                return 1
    return 1
'''
테스트 1 〉	통과 (0.12ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.12ms, 10.3MB)
테스트 6 〉	통과 (1.14ms, 10.2MB)
테스트 7 〉	통과 (0.13ms, 10.2MB)
테스트 8 〉	통과 (0.08ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
'''
def solution(n):
    for i in range(1, n):
        quot, remain = divmod(n, i)
        if remain == 0:
            if quot < i:
                return 2
            elif quot == i:
                return 1
    return 1
'''
테스트 1 〉	통과 (0.11ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.12ms, 10.1MB)
테스트 6 〉	통과 (1.16ms, 10.2MB)
테스트 7 〉	통과 (0.13ms, 10.3MB)
테스트 8 〉	통과 (0.08ms, 10.1MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
'''