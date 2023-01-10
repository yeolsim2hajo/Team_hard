#230110
def solution(n):
    answer = 0
    match = {str(i):i for i in range(10)}
    n = str(n)
    for number in n:
        answer += match[number]
    return answer

# int - 시간 더 걸림
def solution(n):
    answer = 0
    n = str(n)
    for number in n:
        answer += int(number)
    return answer