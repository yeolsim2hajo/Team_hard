#230122
def solution(str1, str2):
    answer = 1 if str2 in str1 else 2
    return answer
'''
테스트 1 〉	통과 (0.00ms, 9.86MB)
테스트 2 〉	통과 (0.00ms, 9.85MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 9.87MB)
테스트 5 〉	통과 (0.00ms, 9.93MB)
테스트 6 〉	통과 (0.00ms, 10MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 9.83MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.00ms, 9.98MB)
테스트 11 〉	통과 (0.00ms, 10.1MB)
'''
def solution(str1, str2):
    index = 0
    length, limit = len(str1), len(str2)
    for i in range(length):
        if str1[i] == str2[index]:
            index += 1
            if index == limit:
                return 1
        else:
            index = 0
    return 2
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
'''
def solution(str1, str2):
    length, limit = len(str1), len(str2)
    for i in range(length-limit+1):
        if str1[i:i+limit] == str2:
                return 1
    return 2
'''
테스트 1 〉	통과 (0.00ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
'''