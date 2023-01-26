#230126
def solution(number):
    answer = 0
    length = len(number)
    for i in range(length-2):
        for j in range(i+1, length-1):
            two = number[i]+number[j]
            for k in range(j+1, length):
                if two+number[k] == 0:
                    answer += 1
    return answer
'''
테스트 1 〉	통과 (0.04ms, 10MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.1MB)
테스트 5 〉	통과 (0.05ms, 10MB)
테스트 6 〉	통과 (0.06ms, 10.1MB)
테스트 7 〉	통과 (0.04ms, 10.1MB)
테스트 8 〉	통과 (0.07ms, 10.1MB)
테스트 9 〉	통과 (0.04ms, 9.98MB)
테스트 10 〉	통과 (0.05ms, 10.1MB)
테스트 11 〉	통과 (0.05ms, 9.98MB)
테스트 12 〉	통과 (0.04ms, 10.1MB)
테스트 13 〉	통과 (0.04ms, 10.1MB)
'''
