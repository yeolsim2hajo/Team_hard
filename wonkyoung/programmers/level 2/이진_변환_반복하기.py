#230209
# def solution(s):
#     # 이진 변환 횟수, 제거된 0의 개수
#     answer = [0] * 2
#     s = list(map(int, s))
#     while True:
#         length = len(s)
#         if length == 1:
#             return answer
#         zero_cnt = 0
#         for num in s:
#             if num == 0:
#                 zero_cnt += 1
#         answer[0] += 1
#         answer[1] += zero_cnt
#         temp = length - zero_cnt
#         s.clear()
#         while temp:
#             s.append(temp%2)
#             temp //= 2
'''
테스트 1 〉	통과 (0.06ms, 10.3MB)
테스트 2 〉	통과 (20.81ms, 11.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.12ms, 10.4MB)
테스트 7 〉	통과 (0.37ms, 10.2MB)
테스트 8 〉	통과 (0.12ms, 10.4MB)
테스트 9 〉	통과 (12.05ms, 11MB)
테스트 10 〉	통과 (17.90ms, 11.2MB)
테스트 11 〉	통과 (16.46ms, 11.5MB)
'''


#
def solution(s):
    # 이진 변환 횟수, 제거된 0의 개수
    answer = [0] * 2
    length = zero_cnt = 0
    for num in s:
        if num == '0':
            zero_cnt += 1
        length += 1
    while True:
        if length == 1:
            return answer
        for i, value in (0, 1), (1, zero_cnt):
            answer[i] += value

        temp = length - zero_cnt
        zero_cnt = length = 0
        while temp:
            if temp%2 == 0:
                zero_cnt += 1
            temp //= 2
            length += 1

print(solution(	"110010101001"))
'''
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (22.57ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.08ms, 10.2MB)
테스트 7 〉	통과 (0.19ms, 10MB)
테스트 8 〉	통과 (0.10ms, 10.3MB)
테스트 9 〉	통과 (14.02ms, 10.2MB)
테스트 10 〉	통과 (13.71ms, 10.4MB)
테스트 11 〉	통과 (15.96ms, 10.3MB)
'''