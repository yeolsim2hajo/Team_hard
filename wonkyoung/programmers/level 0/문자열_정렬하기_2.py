#230206
def solution(my_string):
    my_list = sorted(map(str, my_string.lower()))
    return ''.join(my_list)
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
'''
#dict
def solution(my_string):
    answer = ''
    alp_to_index = {chr(i+97):0 for i in range(26)}
    for alp in my_string:
        alp_to_index[alp.lower()] += 1
    for key, value in alp_to_index.items():
        answer += key * value
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
'''

#
def solution(my_string):
    answer = ''
    alp_to_index = {}
    for alp in my_string:
        alp = alp.lower()
        if alp_to_index.get(alp):
            alp_to_index[alp] += 1
        else:
            alp_to_index[alp] = 1
    for key, value in sorted(alp_to_index.items()):
        answer += key * value
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
'''

def solution(my_string):
    answer = ''
    alp_to_index = {}
    for alp in my_string:
        alp = alp.lower()
        if alp_to_index.get(alp):
            alp_to_index[alp] += 1
        else:
            alp_to_index[alp] = 1
    for key in sorted(alp_to_index.keys()):
        answer += key * alp_to_index[key]
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
'''

#
def solution(my_string):
    answer = ''
    alp_to_index = {}
    keys = []
    for alp in my_string:
        alp = alp.lower()
        if alp_to_index.get(alp):
            alp_to_index[alp] += 1
        else:
            alp_to_index[alp] = 1
            keys.append(alp)
    keys.sort()
    for key in keys:
        answer += key * alp_to_index[key]
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
'''