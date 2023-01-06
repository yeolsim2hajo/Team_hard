#230106
def solution(s):
    position = {chr(97+i):-1 for i in range(26)}
    answer = []
    for i in range(len(s)):
        alp = s[i]
        value = position[alp]
        if value == -1:
            answer.append(-1)
        else:
            answer.append(i-value)
        position[alp] = i
    print(answer)
    return answer
solution('banana')