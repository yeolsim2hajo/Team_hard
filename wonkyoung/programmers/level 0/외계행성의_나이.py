#230117
def solution(age):
    alp_age = {str(i):chr(97+i) for i in range(10)}
    answer = ''
    age = str(age)
    for num in age:
        answer += alp_age[num]
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
'''
def solution(age):
    answer = ''
    age = str(age)
    for num in age:
        answer += chr(97+int(num))
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
'''
def solution(age):
    alp_age = {i: chr(97 + i) for i in range(10)}
    answer = ''
    while age:
        answer = alp_age[age%10]+answer
        age = age//10
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
'''
def solution(age):
    alp_age = [chr(97 + i) for i in range(10)]
    answer = ''
    while age:
        answer = alp_age[age%10]+answer
        age = age//10
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
'''
