#230215
def solution(rsp):
    answer = ''
    win = {'2':'0', '0':'5', '5':'2'}
    for each in rsp:
        answer += win[each]
    return answer
'''
테스트 1 〉	통과 (0.00ms, 10.4MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
'''

def solution(rsp):
    win = {'2':'0', '0':'5', '5':'2'}
    answer = [win[each] for each in rsp]
    return ''.join(answer)
'''
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
'''