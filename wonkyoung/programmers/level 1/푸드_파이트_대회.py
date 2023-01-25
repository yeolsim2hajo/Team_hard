#230125
def solution(food):
    answer = ''
    length = len(food)
    for i in range(1, length):
        answer += str(i) * (food[i]//2)
    return answer + '0' + answer[::-1]
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 9.99MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
'''

# deque
def solution(food):
    from collections import deque
    answer = deque(['0'])
    length = len(food)
    for i in range(length-1, 0, -1):
        half, str_i = food[i]//2, str(i)
        for _ in range(half):
            answer.append(str_i)
            answer.appendleft(str_i)
    return ''.join(answer)
'''
테스트 1 〉	통과 (0.17ms, 10.2MB)
테스트 2 〉	통과 (0.15ms, 10.1MB)
테스트 3 〉	통과 (0.13ms, 10.2MB)
테스트 4 〉	통과 (0.38ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.2MB)
테스트 6 〉	통과 (0.21ms, 10.2MB)
테스트 7 〉	통과 (0.45ms, 10.2MB)
테스트 8 〉	통과 (0.24ms, 10.2MB)
테스트 9 〉	통과 (0.15ms, 10.1MB)
테스트 10 〉	통과 (0.16ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.72ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.1MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
'''