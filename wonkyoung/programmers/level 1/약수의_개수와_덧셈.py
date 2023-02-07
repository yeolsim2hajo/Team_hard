#230207
def solution(left, right):
    from math import isqrt
    answer = 0
    for i in range(left, right+1):
        root = isqrt(i)
        if root * root == i:
            answer -= i
        else:
            answer += i
    return answer
'''
테스트 1 〉	통과 (0.15ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 9.99MB)
테스트 5 〉	통과 (0.12ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
'''

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        start, end = 1, i
        while start <= end:
            mid = (start+end)//2
            square = mid * mid
            if square < i:
                start = mid + 1
            elif square > i:
                end = mid - 1
            else:
                answer -= i
                break
        else:
            answer += i
    return answer
'''
테스트 1 〉	통과 (1.02ms, 10.1MB)
테스트 2 〉	통과 (0.29ms, 10.2MB)
테스트 3 〉	통과 (0.39ms, 10.3MB)
테스트 4 〉	통과 (0.07ms, 10.1MB)
테스트 5 〉	통과 (1.06ms, 10.1MB)
테스트 6 〉	통과 (0.14ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
'''

def solution(left, right):
    answer = sum(range(left, right+1))
    for i in range(left, right+1):
        start, end = 1, i
        while start <= end:
            mid = (start+end)//2
            square = mid * mid
            if square < i:
                start = mid + 1
            elif square > i:
                end = mid - 1
            else:
                answer -= 2*i
                break
    return answer
'''
테스트 1 〉	통과 (1.50ms, 10.3MB)
테스트 2 〉	통과 (0.29ms, 10.1MB)
테스트 3 〉	통과 (0.38ms, 10.2MB)
테스트 4 〉	통과 (0.07ms, 10.1MB)
테스트 5 〉	통과 (0.88ms, 10.3MB)
테스트 6 〉	통과 (0.08ms, 10.1MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
'''

def solution(left, right):
    from math import isqrt
    answer = sum(range(left, right+1))
    for i in range(left, right+1):
        root = isqrt(i)
        if root * root == i:
            answer -= 2*i
    return answer
'''
테스트 1 〉	통과 (0.13ms, 9.98MB)
테스트 2 〉	통과 (0.04ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.11ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
'''

def solution(left, right):
    answer = sum(range(left, right+1))
    num_set = set(range(left, right+1))
    for i in range(1, right+1):
        square = i * i
        if square > right:
            return answer
        if square in num_set:
            answer -= 2*square
'''
테스트 1 〉	통과 (0.11ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.06ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
'''