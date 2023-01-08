#230108
def solution(a, b):
    answer = 0
    length = len(a)
    for i in range(length):
        answer += a[i]*b[i]
    return answer