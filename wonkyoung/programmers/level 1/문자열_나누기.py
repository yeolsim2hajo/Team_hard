#230204
def solution(s):
    i = answer = 0
    length = len(s)
    while i < length:
        first_alp = s[i]
        equal, unequal = 1, 0
        for j in range(i+1, length):
            if first_alp == s[j]:
                equal += 1
            else:
                unequal += 1
            if equal == unequal:
                i = j+1
                answer += 1
                break
        else:
            answer += 1
            break
    return answer