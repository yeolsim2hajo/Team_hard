#230316
# 틀림
# def solution(number, k):
#     length = len(number)
#     answer = ''
#     start = 0
#     while k:
#         max_num = '0'
#         max_i = start
#         if start + k + 1 > length:
#             break
#         for i in range(start, start+k+1):
#             if number[i] > max_num:
#                 max_num = number[i]
#                 max_i = i
#                 if max_num == '9':
#                     break
#         k -= max_i - start
#         start = max_i + 1
#         answer += number[max_i]
#     else:
#         return answer + number[start:]



#
def solution(number, k):
    length = len(number)
    if length == k+1:
        return max(map(str, number))
    answer = ''
    left = length - k
    start, end = 0, k+1
    while k and left:
        max_num = '0'
        max_i = start
        for i in range(start, end):
            if number[i] > max_num:
                max_num = number[i]
                max_i = i
                if max_num == '9':
                    break
        k -= max_i - start
        start = max_i + 1
        answer += number[max_i]
        left -= 1
        if start + k + 1 < length - k:
            end = start + k + 1
        elif start < length - left + 1:
            end = length - left + 1
        else:
            break
    if left:
        return answer + number[start:]
    return answer
print(solution('345682145', 5))
'''
345682145
2
'''
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.02ms, 9.97MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.06ms, 10.2MB)
테스트 6 〉	통과 (2.51ms, 10.1MB)
테스트 7 〉	통과 (1.78ms, 10.2MB)
테스트 8 〉	통과 (5.73ms, 10.4MB)
테스트 9 〉	통과 (0.33ms, 11.6MB)
테스트 10 〉	통과 (36.04ms, 11.5MB)
테스트 11 〉	통과 (0.00ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
'''

