#230202
def solution(n, s):
    if s < n:
        return [-1]
    if s == n:
        return [1] * n
    answer = [s//n] * n
    remain = s%n
    if remain == 0:
        return answer
    for i in range(-1, -remain-1, -1):
        answer[i] += 1
    return answer