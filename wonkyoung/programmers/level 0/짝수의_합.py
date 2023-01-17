#230117
def solution(n):
    answer = 0
    for i in range(2, n+1, 2):
        answer += i
    return answer

def solution(n):
    answer = 0
    half = n//2
    for i in range(1, half+1):
        answer += i*2
    return answer

def solution(n):
    half = n//2
    answer = sum(range(1, half+1))*2
    return answer

def solution(n):
    answer = sum(range(2, n+1, 2))
    return answer

def solution(n):
    half = n // 2
    answer = half*(half+1)
    return answer