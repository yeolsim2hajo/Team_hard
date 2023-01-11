#230111
def solution(my_string):
    answer = 0
    for string in my_string:
        if string.isdigit():
            answer += int(string)
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
'''

#
def solution(my_string):
    answer = 0
    for string in my_string:
        if string.isdecimal():
            answer += int(string)
    return answer
'''
테스트 1 〉	통과 (0.03ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.5MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
'''

#
def solution(my_string):
    answer = 0
    numbers = set(str(i) for i in range(1,10))
    for string in my_string:
        if string in numbers:
            answer += int(string)
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
'''
