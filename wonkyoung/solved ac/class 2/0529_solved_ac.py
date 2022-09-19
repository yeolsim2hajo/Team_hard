# N = int(input())
# def find_series():
#     number = 6
#     cnt = 1
#     length = 2
#     while cnt < N:
#         if cnt == 1 or str(number)[length] != '6':
#             cnt += 1
#             number += 10
#             if str(number)[0] == '0':
#
#             if str(number)[length] == '6':
#                 cnt -= 1
#         else:
#             number -= 6
#             cnt += 1
#             while str(number)[0] != '7':
#                 if cnt == N:
#                     print('66' + str(number))
#                     return
#                 cnt += 1
#                 number += 1
#             number += 6
#
#     print(str(number)+'66')
# find_series()

N = int(input())
cnt = 1
number = 666
while cnt < N:
    number += 1
    series = str(number)
    length = len(series)
    for i in range(length-3, -1, -1):
        if '666' == series[i:3+i]:
            cnt += 1
            break
print(number)
