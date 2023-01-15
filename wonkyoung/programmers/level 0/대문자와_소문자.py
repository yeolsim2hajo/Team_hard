#230115
# def solution(my_string):
#     answer = ''
#     for alp in my_string:
#         answer += alp.swapcase()
#     return answer
'''
테스트 1 〉	통과 (0.01ms, 9.96MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 9.95MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.10ms, 10MB)
테스트 6 〉	통과 (0.12ms, 10.2MB)
테스트 7 〉	통과 (0.12ms, 10.3MB)
'''

# def solution(my_string):
#     answer = ''
#     match  = {}
#     for i in range(26):
#         large, small = chr(i+65), chr(i+97)
#         match[large] = small
#         match[small] = large
#     for alp in my_string:
#         answer += match[alp]
#     return answer

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 9.97MB)
테스트 5 〉	통과 (0.07ms, 10.1MB)
테스트 6 〉	통과 (0.08ms, 10.2MB)
테스트 7 〉	통과 (0.09ms, 10MB)
'''