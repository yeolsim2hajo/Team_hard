#230114
def solution(order):
    order = str(order)
    clap = {'3', '6', '9'}
    answer = 0
    for number in order:
        if number in clap:
            answer += 1
    return answer