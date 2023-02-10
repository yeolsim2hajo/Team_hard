#230210
def solution(box, n):
    answer = 1
    for i in range(3):
        answer *= box[i]//n
    return answer