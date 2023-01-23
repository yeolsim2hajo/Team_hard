#230123
# def solution(my_string):
#     answer = ''
#     vowels = {'a','e','i','o','u'}
#     for each_str in my_string:
#         if each_str not in vowels:
#             answer += each_str
#     return answer
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10MB)
'''
def solution(my_string):
    vowels = {'a','e','i','o','u'}
    answer = [alp for alp in my_string if alp not in vowels]
    return ''.join(answer)
'''
테스트 1 〉	통과 (0.01ms, 9.99MB)
테스트 2 〉	통과 (0.00ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10MB)
테스트 6 〉	통과 (0.01ms, 10MB)
'''