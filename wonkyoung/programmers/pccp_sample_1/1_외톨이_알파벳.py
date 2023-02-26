#230226
#1
def solution(input_string):
    answer = []
    N = len(input_string)
    visited = set()
    for i in range(N-1):
        alp = input_string[i]
        if alp not in visited:
            visited.add(alp)
            consequence = alp == input_string[i+1]
            for j in range(i+2, N):
                if consequence:
                    if alp != input_string[j]:
                        consequence = False
                elif alp == input_string[j]:
                    answer.append(alp)
                    break
    if not answer:
        return 'N'
    return ''.join(sorted(answer))