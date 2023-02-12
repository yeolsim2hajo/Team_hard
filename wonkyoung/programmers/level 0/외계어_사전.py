#230129
# 틀림
# def solution(spell, dic):
#     length = len(spell)
#     for word in dic:
#         possible = False
#         check = [False] * length
#         if len(word) == length:
#             for alp in dic:
#                 for i in range(length):
#                     if alp == spell[i]:
#                         if not check[i]:
#                             check[i] = True
#                             possible = True
#                             break
#                         else:
#                             break
#                 else:
#                     break
#                 if not possible:
#                     break
#         if possible:
#             return 1
#     return 2


# 220213
# def solution(spell, dic):
#     length, answer = len(spell), ''.join(sorted(spell))
#     for word in dic:
#         if len(word) == length and ''.join(sorted(word)) == answer:
#             return 1
#     return 2
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
'''

# def solution(spell, dic):
#     length = len(spell)
#     for word in dic:
#         check = {alp: False for alp in spell}
#         if len(word) == length:
#             for alp in word:
#                 if check.get(alp, -1):
#                     break
#                 else:
#                     check[alp] = True
#             else:
#                 return 1
#     return 2
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
'''

# def solution(spell, dic):
#     from itertools import permutations
#     cases = permutations(spell)
#     length = len(spell)
#     for word in dic:
#         if len(word) == length and tuple(map(str, word)) in cases:
#                 return 1
#     return 2
'''
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (2030.53ms, 595MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10MB)
'''