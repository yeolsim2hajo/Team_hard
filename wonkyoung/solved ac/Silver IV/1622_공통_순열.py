#230312
# check = {chr(97+i):0 for i in range(26)}
# answer = []
# while True:
#     try:
#         a = input()
#         b = input()
#         if len(a) > len(b):
#             a, b = b, a
#
#         for alp in a:
#             check[alp] += 1
#
#         for alp in b:
#             if check[alp]:
#                 check[alp] -= 1
#                 answer.append(alp)
#
#         answer.sort()
#         print(''.join(answer))
#
#         for alp in a:
#             check[alp] = 0
#         answer.clear()
#     except Exception:
#         break

#
check = {chr(97+i):0 for i in range(26)}
answer = []
while True:
    try:
        a = input()
        b = input()
        if len(a) > len(b):
            a, b = b, a

        for alp in a:
            check[alp] += 1

        for alp in b:
            if check[alp]:
                check[alp] -= 1
                answer.append(alp)

        answer.sort()
        print(''.join(answer))

        for alp in a:
            check[alp] = 0
        answer.clear()
    except EOFError:
        break


