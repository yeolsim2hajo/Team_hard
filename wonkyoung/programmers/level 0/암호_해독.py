#230201
def solution(cipher, code):
    answer = ''
    length = len(cipher)
    for i in range(code-1, length, code):
        answer += cipher[i]
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.08ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.1MB)
테스트 10 〉	통과 (0.03ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
'''
