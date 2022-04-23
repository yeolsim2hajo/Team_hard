#96 넓은 텃밭 만들기 - 다시

#97 택배 배달
# def solution(n,l):
#     now = [l[:n]]
#     second = 0
#     idx = n
#     while now:
#         yeolsim = now.pop(0)
#         if yeolsim.count(0) == n:
#             return second
#         second += 1
#         for i in range(n):
#             if yeolsim[i] > 0:
#                 yeolsim[i] -= 1
#             elif yeolsim[i] == 0:
#                 if idx != len(l)-1:
#                     yeolsim[i] = l[idx]
#                     idx += 1
#         now.append(yeolsim)
#
# people = 3
# parcel = [1,2,1,3,3,3]
#
# print(solution(people,parcel))


#98 청길이의 패션 대회
# def solution(info):
#     unique = []
#     length = len(info)
#     idx = 0
#     while idx < length:
#         if info[idx] == ',':
#             idx += 1
#             if info[idx] not in unique:
#                 unique.append(info[idx])
#         elif info[idx] == '번':
#             idx += 3
#             if info[idx] not in unique:
#                 unique.append(info[idx])
#         else:
#             idx += 1
#     unique = list(map(int,unique))
#     return unique
#
# print(solution('1번: 4,2,3 2번: 3 3번: 2,3,4,1 4번: 2,3'))
# print(solution('1번: 3,1 2번: 4 3번: 2,1,3 4번: 2,1,3,4'))