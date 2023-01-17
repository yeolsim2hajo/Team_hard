#230117
def solution(num_list, n):
    answer = []
    limit = len(num_list)//n
    for i in range(limit):
        answer.append(num_list[i*n:(i+1)*n])
    return answer


def solution(num_list, n):
    limit = len(num_list)//n
    answer = [[] for _ in range(limit)]
    for i in range(limit):
        answer[i] = num_list[i*n:(i+1)*n]
    return answer