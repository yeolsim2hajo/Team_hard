#230310
# def solution(n, left, right):
#     answer = []
#     for i in range(left, right+1):
#         answer.append(max(i//n, i%n)+1)
#     return answer
'''
테스트 1 〉	통과 (19.54ms, 16.3MB)
테스트 2 〉	통과 (24.19ms, 18.9MB)
테스트 3 〉	통과 (24.59ms, 19.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (23.13ms, 18.4MB)
테스트 7 〉	통과 (24.92ms, 18.9MB)
테스트 8 〉	통과 (20.90ms, 17.6MB)
테스트 9 〉	통과 (24.67ms, 18.7MB)
테스트 10 〉	통과 (24.61ms, 18.6MB)
테스트 11 〉	통과 (23.10ms, 18.4MB)
테스트 12 〉	통과 (25.91ms, 18MB)
테스트 13 〉	통과 (29.61ms, 18.5MB)
테스트 14 〉	통과 (28.41ms, 18.3MB)
테스트 15 〉	통과 (27.24ms, 18.2MB)
테스트 16 〉	통과 (33.62ms, 18.4MB)
테스트 17 〉	통과 (28.90ms, 18.6MB)
테스트 18 〉	통과 (39.44ms, 19MB)
테스트 19 〉	통과 (29.33ms, 18.7MB)
테스트 20 〉	통과 (26.36ms, 18MB)
'''

#
def solution(n, left, right):
    answer = []
    quot, remain = divmod(left, n)
    num = max(quot, remain)+1
    for i in range(left, right+1):
        answer.append(num)
        remain += 1
        if remain == n:
            remain = 0
            quot += 1
            num = quot+1
        elif remain > quot:
            num += 1
    return answer
'''
테스트 1 〉	통과 (9.77ms, 16MB)
테스트 2 〉	통과 (23.95ms, 18.9MB)
테스트 3 〉	통과 (24.28ms, 19.4MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (10.20ms, 15.8MB)
테스트 7 〉	통과 (12.86ms, 17.8MB)
테스트 8 〉	통과 (11.89ms, 17.6MB)
테스트 9 〉	통과 (12.64ms, 17.2MB)
테스트 10 〉	통과 (13.22ms, 18.3MB)
테스트 11 〉	통과 (11.09ms, 16.1MB)
테스트 12 〉	통과 (10.75ms, 17.5MB)
테스트 13 〉	통과 (11.39ms, 17.3MB)
테스트 14 〉	통과 (9.36ms, 15.9MB)
테스트 15 〉	통과 (11.88ms, 18MB)
테스트 16 〉	통과 (12.65ms, 18.4MB)
테스트 17 〉	통과 (9.39ms, 15.5MB)
테스트 18 〉	통과 (14.27ms, 19.1MB)
테스트 19 〉	통과 (13.03ms, 18.6MB)
테스트 20 〉	통과 (9.70ms, 15.5MB)
'''