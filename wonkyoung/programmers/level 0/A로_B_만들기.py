#230209
def solution(before, after):
    alp_list = [chr(i+97) for i in range(26)]
    alp_cnt = {alp_list[i]:0 for i in range(26)}
    length = len(before)
    for i in range(length):
        alp_cnt[before[i]] += 1
        alp_cnt[after[i]] -= 1
    for alp in alp_list:
        if alp_cnt[alp]:
            return 0
    return 1
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.18ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.06ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.18ms, 10.2MB)
테스트 12 〉	통과 (0.18ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.04ms, 10.3MB)
테스트 16 〉	통과 (0.09ms, 10.2MB)
테스트 17 〉	통과 (0.08ms, 10.3MB)
테스트 18 〉	통과 (0.18ms, 10.2MB)
테스트 19 〉	통과 (0.18ms, 10.1MB)
테스트 20 〉	통과 (0.17ms, 10.1MB)
테스트 21 〉	통과 (0.17ms, 10.1MB)
테스트 22 〉	통과 (0.01ms, 10.1MB)
테스트 23 〉	통과 (0.01ms, 10.4MB)
'''

#
def solution(before, after):
    alp_cnt = {chr(i+97):0 for i in range(26)}
    for alp in before:
        alp_cnt[alp] += 1
    for alp in after:
        if alp_cnt[alp] >= 1:
            alp_cnt[alp] -= 1
        else:
            return 0
    return 1
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.15ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.1MB)
테스트 11 〉	통과 (0.13ms, 10.2MB)
테스트 12 〉	통과 (0.16ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.04ms, 10.3MB)
테스트 16 〉	통과 (0.07ms, 10.1MB)
테스트 17 〉	통과 (0.06ms, 10.2MB)
테스트 18 〉	통과 (0.17ms, 10.2MB)
테스트 19 〉	통과 (0.17ms, 10.4MB)
테스트 20 〉	통과 (0.13ms, 10.2MB)
테스트 21 〉	통과 (0.11ms, 10.2MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
'''

def solution(before, after):
    alp_cnt = {}
    for alp in before:
        if alp_cnt.get(alp):
            alp_cnt[alp] += 1
        else:
            alp_cnt[alp] = 1
    for alp in after:
        if alp_cnt.get(alp):
            alp_cnt[alp] -= 1
        else:
            return 0
    return 1
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.22ms, 10.4MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.07ms, 10.3MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.18ms, 10.1MB)
테스트 12 〉	통과 (0.21ms, 10.3MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.08ms, 10.2MB)
테스트 16 〉	통과 (0.20ms, 10.3MB)
테스트 17 〉	통과 (0.08ms, 10.4MB)
테스트 18 〉	통과 (0.18ms, 10.2MB)
테스트 19 〉	통과 (0.19ms, 10.2MB)
테스트 20 〉	통과 (0.18ms, 10.2MB)
테스트 21 〉	통과 (0.14ms, 10.2MB)
테스트 22 〉	통과 (0.00ms, 10.3MB)
테스트 23 〉	통과 (0.00ms, 10.2MB)
'''