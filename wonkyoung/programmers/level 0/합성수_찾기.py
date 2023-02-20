#230220
def solution(n):
    if n == 1:
        return 0
    num_set = set(range(2, n+1))
    answer = 0
    for i in range(2, n+1):
        if i in num_set:
            num = i * 2
            while num <= n:
                num_set.discard(num)
                num += i
        else:
            answer += 1
    return answer
'''
테스트 1 〉	통과 (0.04ms, 10MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 9.98MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
'''
def solution(n):
    if n == 1:
        return 0
    num_set = set(range(1, n+1))
    for i in range(2, n+1):
        if i in num_set:
            num = i * 2
            while num <= n:
                num_set.discard(num)
                num += i
    return n - len(num_set)
'''
테스트 1 〉	통과 (0.11ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.19ms, 10MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
'''