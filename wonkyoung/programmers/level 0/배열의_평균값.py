#230211
def solution(numbers):
    return sum(numbers)/len(numbers)
'''
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10MB)
'''

def solution(numbers):
    length = total = 0
    for number in numbers:
        length += 1
        total += number
    return total/length
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10MB)
테스트 4 〉	통과 (0.00ms, 10MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
'''