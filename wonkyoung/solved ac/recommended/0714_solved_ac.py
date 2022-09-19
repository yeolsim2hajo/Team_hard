#17451 평행 우주 - 시간초과
# N = int(input())
# planet = list(map(int, input().split()))
# speed = planet[-1]
# def find_speed():
#     global speed
#     def multiple_speed():
#         global speed
#         multiple = 2
#         while True:
#             new_speed = planet[i] * multiple
#             if speed <= new_speed:
#                 speed = new_speed
#                 return
#             multiple += 1
#
#     for i in range(N-2, -1, -1):
#         if speed <= planet[i]:
#             speed = planet[i]
#         else:
#             multiple_speed()
#
# find_speed()
# print(speed)


#
# N = int(input())
# planet = list(map(int, input().split()))
# speed = planet[0]
# multiple = 2
# def find_speed():
#     global multiple
#     new_speed = speed
#     for i in range(1,N):
#         if planet[i] <= new_speed:
#             new_speed -= new_speed%planet[i]
#         else:
#             return 0
#     return 1
#
# def multiple_speed():
#     global speed
#     while True:
#         if find_speed():
#             return
#         speed = planet[0] * multiple
#         multiple += 1
#
# multiple_speed()
# print(speed)


#17413 단어 뒤집기 2
# 정답
# S = input()
# new_word = ''
# idx = 0
# length = len(S)
# while idx < length:
#     alp = S[idx]
#     if alp == '<':
#         if new_word:
#             print(new_word[::-1], end='')
#             new_word = ''
#         while True:
#             print(alp, end='')
#             if alp == '>':
#                 break
#             idx += 1
#             alp = S[idx]
#     elif alp == ' ':
#         print(new_word[::-1],'', end='')
#         new_word = ''
#     elif idx == length-1:
#         new_word += alp
#         print(new_word[::-1], end='')
#     else:
#         new_word += alp
#     idx += 1


# S = input().split('<')
# for word in S:
#     if word == '':
#         continue
#     elif word[-1] == '>':
#         print('<' + word, end='')
#     elif '>' not in word:
#         for string in word.split():
#             print(string[::-1], end=' ')
#     else:
#         length = len(word)
#         for i in range(length):
#             if word[i] == '>':
#                 print('<' + word[:i+1],end='')
#                 new_word = word[i+1:].split()
#                 for j in range(len(new_word)):
#                     new_word[j] = new_word[j][::-1]
#                 print(' '.join(new_word), end='')
