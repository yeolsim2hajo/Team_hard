#230117
def solution(n):
    answer = length = 0
    three = ''
    while n > 0:
        length += 1
        three += str(n%3)
        n = n//3
    for i in range(length):
        answer += int(three[i]) * 3**(length-1-i)
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.5MB)
테스트 7 〉	통과 (0.03ms, 10.5MB)
테스트 8 〉	통과 (0.04ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.4MB)
'''

def solution(n):
    answer = 0
    three = ''
    while n > 0:
        three += str(n%3)
        n = n//3
    length = len(three)
    for i in range(length):
        answer += int(three[i]) * 3**(length-1-i)
    return answer

'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.04ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.05ms, 10.3MB)
'''

def solution(n):
    answer = 0
    three = ''
    while n > 0:
        three += str(n%3)
        n = n//3
    three.lstrip('0')
    length = len(three)
    for i in range(length):
        answer += int(three[i]) * 3**(length-1-i)
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
'''

def solution(n):
    answer = 0
    three = ''
    while n > 0:
        three += str(n%3)
        n = n//3
    three = int(three)
    three = str(three)
    length = len(three)
    for i in range(length):
        answer += int(three[i]) * 3**(length-1-i)
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.04ms, 10.4MB)
'''

def solution(n):
    answer = 0
    three = ''
    while n > 0:
        three += str(n%3)
        n = n//3
    three = str(int(three))
    length = len(three)
    for i in range(length):
        answer += int(three[i]) * 3**(length-1-i)
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
'''

def solution(n):
    answer = 0
    three = ''
    while n > 0:
        three += str(n%3)
        n = n//3
    three = three.lstrip('0')
    length = len(three)
    for i in range(length):
        answer += int(three[i]) * 3**(length-1-i)
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
'''

def solution(n):
    str_remain = {str(i):i for i in range(3)}
    answer = 0
    three = ''
    while n > 0:
        three += str(n%3)
        n = n//3
    three= three.lstrip('0')
    length = len(three)
    for i in range(length):
        answer += str_remain[three[i]] * 3**(length-1-i)
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
'''

def solution(n):
    str_remain = {str(i):i for i in range(3)}
    answer = 0
    three = ''
    while n > 0:
        three += str(n%3)
        n = n//3
    three = str(int(three))
    length = len(three)
    for i in range(length):
        answer += str_remain[three[i]] * 3**(length-1-i)
    return answer
'''
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.4MB)
'''