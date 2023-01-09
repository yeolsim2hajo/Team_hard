#230109
def solution(s, n):
    push = {}
    for i in range(25):
        push[chr(i+65)] = chr(i+66)
        push[chr(i+97)] = chr(i+98)
    push[chr(90)] = 'A'
    push[chr(122)] = 'a'
    push[' '] = ' '
    for _ in range(n):
        answer = ''
        for alp in s:
            answer += push[alp]
        s = answer
    return answer

