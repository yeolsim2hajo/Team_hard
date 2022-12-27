# #221227
# T = int(input())
# for _ in range(T):
#     gene = input()
#     answer = 'Good'
#     alp_list = {'A', 'B', 'C', 'D', 'E', 'F'}
#     condition = [False] * 5
#     index = 0
#     for index in range(len(gene)):
#         alp = gene[index]
#         if index == 0:
#             if alp == 'A':
#                 condition[1] = True
#             elif alp not in alp_list:
#                 break
#             condition[0] = True
#
#         elif not condition[1]:
#             if alp == 'A':
#                 condition[1] = True
#             else:
#                 break
#         elif not condition[2]:
#             if alp == 'A':
#                 condition[1] = True
#             elif alp == 'F':
#                 condition[2] = True
#             else:
#                 break
#         elif not condition[3]:
#             if alp == 'A':
#                 condition[1] = True
#             elif alp == 'F':
#                 condition[2] = True
#             elif alp == 'C':
#                 condition[3] = True
#             else:
#                 break
#         elif not condition[4]:
#             if alp == 'C':
#                 condition[3] = True
#             elif alp in alp_list:
#                 condition[4] = True
#             else:
#                 break
#         else:
#             break
#         index += 1
#     else:
#         answer = 'Infected!'
#     print(answer)


#221227
T = int(input())
for _ in range(T):
    gene = input()
    answer = 'Good'
    alp_list = {'A', 'B', 'C', 'D', 'E', 'F'}
    alp_match = {'A': 1, 'F': 2, 'C': 3}
    alp_set = [set(), {'A'}, {'A', 'F'}, {'F', 'C'}, alp_match]
    condition = [False] * 5
    index = 0
    for index in range(len(gene)):
        alp = gene[index]
        if index == 0:
            if alp == 'A':
                condition[1] = True
            elif alp not in alp_list:
                break
            condition[0] = True

        elif not condition[1]:
            if alp == 'A':
                condition[1] = True
            else:
                break
        else:
            for i in range(2, 4):
                if not condition[i]:
                    if alp in alp_set[i]:
                        condition[alp_match[alp]] = True
                    else:
                        break
            if not condition[4]:
                if alp == 'C':
                    condition[3] = True
                elif alp in alp_list:
                    condition[4] = True
                else:
                    break
            else:
                break
        index += 1
    else:
        answer = 'Infected!'
    print(answer)