#230120
# def solution(my_string):
#     answer = 0
#     i, do, length = 0, '', len(my_string)
#     while i < length:
#         if my_string[i].isdigit():
#             for j in range(i, length):
#                 if not my_string[j].isdigit():
#                     break
#             else:
#                 j += 1
#             number = int(my_string[i:j])
#             answer += number if do != '-' else -number
#             i = j+1
#         else:
#             do = my_string[i]
#             i += 2
#     return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
'''

def solution(my_string):
    answer = 0
    my_string = my_string.split(' + ')
    for element in my_string:
        if element.isdigit():
            answer += int(element)
        else:
            element = element.split(' - ')
            answer += int(element[0])
            for i in range(1, len(element)):
                answer -= int(element[i])
    return answer
solution('3 - 4 - 1 - 7 + 4 - 1')
'''
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.5MB)
테스트 4 〉	통과 (0.02ms, 10.5MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.4MB)
'''