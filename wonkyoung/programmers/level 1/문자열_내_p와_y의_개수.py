#230204
def solution(s):
    s = s.lower()
    answer = s.count('p') == s.count('y')
    return answer

def solution(s):
    s = s.lower()
    p = y = 0
    for alp in s:
        if alp == 'p':
            p += 1
        elif alp == 'y':
            y += 1
    return p == y