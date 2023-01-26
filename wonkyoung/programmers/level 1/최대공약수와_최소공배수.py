#230125
# def solution(n, m):
#     def find_divisor(a, b):
#         while a:
#             a %= b
#             if a == 0:
#                 return b
#             a, b = b, a
#     if n < m:
#         n, m = m, n
#     max_divisor = find_divisor(n, m)
#     min_multiple = n * m // max_divisor
#     return [max_divisor, min_multiple]
'''
테스트 1 〉	통과 (0.00ms, 10MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 9.92MB)
테스트 14 〉	통과 (0.00ms, 10MB)
테스트 15 〉	통과 (0.00ms, 10.1MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
'''

# for문 이용
def solution(n, m):
    def find_divisor(a, b):
        start = answer = 2 if a%2 == b%2 == 0 else 1
        for i in range(start+2, b+1, 2):
            if a%i == b%i == 0:
                answer = i
        return answer
    if n < m:
        n, m = m, n
    max_divisor = find_divisor(n, m)
    min_multiple = n * m // max_divisor
    return [max_divisor, min_multiple]
'''
테스트 1 〉	통과 (0.01ms, 9.98MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 9.97MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 9.97MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.04ms, 10.1MB)
테스트 12 〉	통과 (0.17ms, 10.2MB)
테스트 13 〉	통과 (0.10ms, 10.1MB)
테스트 14 〉	통과 (0.16ms, 10.3MB)
테스트 15 〉	통과 (0.07ms, 10.1MB)
테스트 16 〉	통과 (0.07ms, 10.1MB)
'''

def solution(n, m):
    def find_divisor(a, b):
        start = answer = 2 if a%2 == b%2 == 0 else 1
        for i in range(start+2, b+1, 2):
            if b%i == 0:
                if a%i == 0:
                    answer = i
        return answer
    if n < m:
        n, m = m, n
    max_divisor = find_divisor(n, m)
    min_multiple = n * m // max_divisor
    return [max_divisor, min_multiple]
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.06ms, 10.1MB)
테스트 13 〉	통과 (0.07ms, 10.1MB)
테스트 14 〉	통과 (0.11ms, 9.92MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.04ms, 10.1MB)
'''

def solution(n, m):
    def find_divisor(a, b):
        from math import isqrt
        answer = 1
        end = isqrt(b) + 1
        for i in range(1, end):
            quot = b//i
            if b % quot == 0:
                if a % quot == 0:
                    return quot
            if b % i == 0:
                if a % i == 0:
                    answer = i
        return answer
    if n < m:
        n, m = m, n
    max_divisor = find_divisor(n, m)
    min_multiple = n * m // max_divisor
    return [max_divisor, min_multiple]
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
'''
def solution(n, m):
    def find_divisor(a, b):
        from math import isqrt
        answer = 1
        end = isqrt(b) + 1
        for i in range(1, end):
            quot = b//i
            if b % quot == 0 and a % quot == 0:
                return quot
            elif b % i == 0 and a % i == 0:
                answer = i
        return answer
    if n < m:
        n, m = m, n
    max_divisor = find_divisor(n, m)
    min_multiple = n * m // max_divisor
    return [max_divisor, min_multiple]
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.03ms, 10.1MB)
테스트 14 〉	통과 (0.02ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.1MB)
'''