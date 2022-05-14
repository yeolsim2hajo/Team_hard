#4153 직각삼각형
# while True:
#     A, B, C = sorted(map(int, input().split()))
#     if A == B == C == 0:
#         break
#     if A**2 + B**2 == C**2:
#         print('right')
#     else:
#         print('wrong')

#4949 균형잡힌 세상
# 딕셔너리
# pair = {
#     '(':[],
#     '[':[],
#     ')':'(',
#     ']':'[',
# }
# answer = 'yes'
# while True:
#     sentence = input()
#     if sentence == '.':
#         break
#     for i in range(len(sentence)):
#         alp = sentence[i]
#         if alp in {'(', '['}:
#             pair[alp].append(i)
#         elif alp in {')', ']'}:
#             index = min(pair['('][-1],pair['['][-1]) if pair['('] and pair['['] else pair['('][-1] or pair['['][-1]
#             # print(index)
#             if index == pair[pair[alp]][-1]:
#                 print(alp, pair[alp], pair[pair[alp]])
#                 pair[pair[alp]].pop()
#             else:
#                 answer = 'no'
#                 break
#         if answer == 'no':
#             break
#     else:
#         print('yes')

# 스택
open_brackets = ['(', '[']
close_brackets = [')', ']']
while True:
    sentence = input()
    if sentence == '.':
        break
    answer = 'yes'
    stack = []
    for alp in sentence:
        if alp in open_brackets:
            stack.append(alp)
        elif alp in close_brackets:
            if stack:
                top = stack.pop()
                if open_brackets.index(top) != close_brackets.index(alp):
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break
    if stack:
        answer = 'no'
    print(answer)