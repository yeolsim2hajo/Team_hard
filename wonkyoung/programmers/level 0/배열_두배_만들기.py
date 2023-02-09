#230209
def solution(numbers):
    answer = list(map(lambda x: 2*x, numbers))
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.16ms, 10.3MB)
테스트 7 〉	통과 (0.17ms, 10.2MB)
테스트 8 〉	통과 (0.09ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.07ms, 10.3MB)
'''
def solution(numbers):
    return list(map(lambda x: 2*x, numbers))
'''
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.09ms, 10.1MB)
테스트 7 〉	통과 (0.10ms, 10.2MB)
테스트 8 〉	통과 (0.18ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.07ms, 10.2MB)
'''

def solution(numbers):
    numbers = list(map(lambda x: 2*x, numbers))
    return numbers
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 9.94MB)
테스트 6 〉	통과 (0.11ms, 10.1MB)
테스트 7 〉	통과 (0.09ms, 10.2MB)
테스트 8 〉	통과 (0.10ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.07ms, 10.1MB)
'''

def solution(numbers):
    length = len(numbers)
    for i in range(length):
        numbers[i] *= 2
    return numbers
'''
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10MB)
테스트 6 〉	통과 (0.08ms, 10.3MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.16ms, 10.5MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.10ms, 10.2MB)
'''