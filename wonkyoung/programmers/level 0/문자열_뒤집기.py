#230116
def solution(my_string):
    return my_string[::-1]
'''

테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
'''

def solution(my_string):
    answer = ''
    n = len(my_string)
    for i in range(n-1, -1, -1):
        answer += my_string[i]
    return answer
'''

테스트 1 〉	통과 (0.00ms, 9.92MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
'''

def solution(my_string):
    answer = ''
    for alp in my_string:
        answer = alp+answer
    return answer

'''
테스트 1 〉	통과 (0.00ms, 9.93MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
'''