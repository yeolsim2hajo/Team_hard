#230120
def solution(s1, s2):
    answer = set(s1) & set(s2)
    return len(answer)
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
'''
def solution(s1, s2):
    s1.sort()
    s2.sort()
    s1_i = s2_i = answer = 0
    s1_len, s2_len = len(s1), len(s2)
    while s1_i < s1_len and s2_i < s2_len:
        s1_el, s2_el = s1[s1_i], s2[s2_i]
        if s1_el == s2_el:
            answer += 1
            s1_i += 1
            s2_i += 1
        elif s1_el < s2_el:
            s1_i += 1
        else:
            s2_i += 1
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10MB)
'''