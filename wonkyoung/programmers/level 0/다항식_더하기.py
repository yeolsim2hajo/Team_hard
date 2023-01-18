#230118
# def solution(polynomial):
#     answer = ''
#     length = len(polynomial)
#     index = x = not_x = 0
#     while index < length:
#         element = polynomial[index]
#         if element.isdigit():
#             number = element
#             for i in range(index+1, length):
#                 next_element = polynomial[i]
#                 if next_element.isdigit():
#                     number += next_element
#                 else:
#                     index = i-1
#                     number = int(number)
#                     if polynomial[index + 1] == 'x':
#                         x += number
#                         index += 1
#                     else:
#                         not_x += number
#                     break
#             else:
#                 not_x += int(number)
#                 break
#         elif element == 'x':
#             x += 1
#         index += 4
#     if x != 1:
#         answer += f'{x}x'
#     else:
#         answer += 'x'
#     if not_x:
#         answer += f' + {not_x}'
#     return answer

def solution(polynomial):
    polynomial = polynomial.split(' + ')
    x = not_x = 0
    for element in polynomial:
        if element.isdigit():
            not_x += int(element)
        elif element != 'x':
            x += int(element[:-1])
        else:
            x += 1
    if x == 0:
        answer = ''
        if not_x:
            answer += f'{not_x}'
    else:
        if x == 1:
            answer = 'x'
        else:
            answer = f'{x}x'
        if not_x:
            answer += f' + {not_x}'
    return answer
'''
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.5MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (1.49ms, 10.4MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
'''

# 정리
def solution(polynomial):
    polynomial = polynomial.split(' + ')
    x = not_x = 0
    for element in polynomial:
        if element.isdigit():
            not_x += int(element)
        elif element != 'x':
            x += int(element[:-1])
        else:
            x += 1
    if x == 0:
        answer = f'{not_x}'
    else:
        if x == 1:
            answer = 'x'
        else:
            answer = f'{x}x'
        if not_x:
            answer += f' + {not_x}'
    return answer
solution('3x + 7 + 0x + 99')
solution('7x + x + x + 11 + x + 2x + 3')
'''
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.5MB)
테스트 7 〉	통과 (0.03ms, 10.5MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.4MB)
'''