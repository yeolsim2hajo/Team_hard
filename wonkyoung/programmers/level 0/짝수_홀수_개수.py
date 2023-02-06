#230206
def solution(num_list):
    answer = [0]*2
    for num in num_list:
        index = num%2
        answer[index] += 1
    return answer
'''
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
'''

def solution(num_list):
    answer = [0]*2
    for num in num_list:
        answer[num%2] += 1
    return answer
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
'''