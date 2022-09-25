def solution(n):
    answer = 0
    temp = int(n ** 0.5)
    if n == temp ** 2:
        answer = (temp+1) ** 2
    else:
        answer = -1
    return answer
