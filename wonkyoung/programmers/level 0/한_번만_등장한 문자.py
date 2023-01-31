#230201
def solution(s):
    answer = ''
    alp_keys = [chr(97+i) for i in range(26)]
    alp_dict = {alp:0 for alp in alp_keys}
    for alp in s:
        alp_dict[alp] += 1
    for alp in alp_keys:
        if alp_dict[alp] == 1:
            answer += alp
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
'''

def solution(s):
    answer = ''
    alp_dict = {}
    for alp in s:
        if alp_dict.get(alp, -1) == -1:
            alp_dict[alp] = 1
        else:
            alp_dict[alp] += 1
    alp_keys = alp_dict.keys()
    for alp in alp_keys:
        if alp_dict[alp] == 1:
            answer += alp
    return ''.join(sorted(answer))
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
'''