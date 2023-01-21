#230121
# def solution(my_string, num1, num2):
#     answer = list(map(str, my_string))
#     answer[num1], answer[num2] = answer[num2], answer[num1]
#     return ''.join(answer)
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
'''

def solution(my_string, num1, num2):
    answer = ''
    for i in range(len(my_string)):
        if i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += my_string[num1]
        else:
            answer += my_string[i]
    return answer
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
'''