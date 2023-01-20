#230120
# map
# def solution(array):
#     array = list(map(str, array))
#     answer = 0
#     for number in array:
#         for element in number:
#             if element == '7':
#                 answer += 1
#     return answer
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
'''

# str
# def solution(array):
#     answer = 0
#     for number in array:
#         for element in str(number):
#             if element == '7':
#                 answer += 1
#     return answer
'''
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 9.95MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
'''
def solution(array):
    answer = 0
    for number in array:
        split_list = str(number).split('7')
        answer += len(split_list) - 1
    return answer
# solution(['7717', '7777', '7','7145', '7167', '711187', '13273'])
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
'''