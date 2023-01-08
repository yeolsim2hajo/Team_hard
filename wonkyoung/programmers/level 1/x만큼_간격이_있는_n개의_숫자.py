#230108
def solution(x, n):
    answer = []
    element = x
    for i in range(n):
        answer.append(element)
        element += x
    return answer