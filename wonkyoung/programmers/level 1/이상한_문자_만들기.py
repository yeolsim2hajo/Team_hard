# 그 전 (오답)
# def solution(s):
#     answer = []
#     words = s.split()
#     for word in words:
#         new_word = ''
#         for i in range(len(word)):
#             new_word += word[i].lower() if i%2 else word[i].upper()
#         answer.append(new_word)
#     return ' '.join(answer)

# 오답2
# def solution(s):
#     answer = ''
#     space_i = -1
#     n = len(s)
#     for i in range(n):
#         element = s[i]
#         if element.isalpha():
#             new_i = i - space_i - 1
#             answer += element.lower() if new_i%2 else element.upper()
#         else:
#             space_i = i
#             answer += element
#     return answer


#230112
def solution(s):
    answer, index = '', 0
    for alp in s:
        if alp != ' ':
            if index % 2:
                answer += alp.lower()
            else:
                answer += alp.upper()
            index += 1
        else:
            answer += alp
            index = 0
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 9.99MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.04ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.1MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
'''
