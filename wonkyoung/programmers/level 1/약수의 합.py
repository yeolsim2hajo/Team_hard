#230203
def solution(n):
    from math import isqrt
    answer = 0
    root = isqrt(n)
    for i in range(1, root+1):
        if n%i == 0:
            answer += i + n//i
    if root * root == n:
        answer -= root
    return answer