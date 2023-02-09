#230209
def solution(my_string, n):
    answer = ''
    for alp in my_string:
        answer += alp * n
    return answer