#230207
def solution(s):
    answer = list(map(str, s))
    answer.sort(reverse=True)
    return ''.join(answer)