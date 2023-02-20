#230221
def solution(n):
    if n < 4: return n
    before = 2
    answer = 3
    for _ in range(4, n+1):
        answer, before = (answer + before)%1234567, answer
    return answer