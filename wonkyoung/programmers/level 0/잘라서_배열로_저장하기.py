#230124
def solution(my_str, n):
    answer = []
    start = 0
    length = len(my_str)
    while start < length:
        answer.append(my_str[start:start+n])
        start += n
    return answer