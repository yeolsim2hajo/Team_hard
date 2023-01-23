#230123
def solution(hp):
    answer = hp
    for start in (5,3):
        cnt = 0
        left_hp = hp
        for i in range(start, 2, -2):
            if left_hp:
                cnt += left_hp // i
                left_hp %= i
            else:
                break
        if left_hp:
            cnt += left_hp
        if cnt < answer:
            answer = cnt
    return answer
'''
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
'''
def solution(hp):
    answer = hp
    for start in (5,3):
        cnt = 0
        left_hp = hp
        for i in range(start, 2, -2):
            if left_hp:
                cnt += left_hp // i
                left_hp %= i
        if left_hp:
            cnt += left_hp
        if cnt < answer:
            answer = cnt
    return answer
'''
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
'''

def solution(hp):
    answer = hp
    for start in (5,3):
        cnt = 0
        left_hp = hp
        for i in range(start, 2, -2):
            if left_hp:
                cnt += left_hp // i
                left_hp %= i
        cnt += left_hp
        if cnt < answer:
            answer = cnt
    return answer
'''
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.4MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
'''