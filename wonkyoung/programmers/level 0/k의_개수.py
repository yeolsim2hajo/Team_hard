#230228
def solution(i, j, k):
    answer = 0
    str_k = str(k)
    for num in range(i, j+1):
        answer += str(num).count(str_k)
    return answer
'''
테스트 1 〉	통과 (42.49ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (2.57ms, 10.2MB)
테스트 5 〉	통과 (1.48ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.20ms, 10.3MB)
테스트 8 〉	통과 (10.85ms, 10.2MB)
'''