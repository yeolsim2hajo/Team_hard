#79 순회하는 리스트
# def rot():
#     temp = new_l.pop()
#     new_l.insert(0,temp)
#
# l = [10,20,25,27,34,35,39]
# new_l = l[:]
# n = int(input())
# for _ in range(n):
#     rot()
# min_dif = 100
# for i in range(7):
#     dif = abs(l[i] - new_l[i])
#     if min_dif > dif:
#         min_dif = dif
#         idx = i
# print('index : {}\nvalue : {}, {}'.format(idx,l[idx],new_l[idx]))


# 문제
# l = [10,20,25,27,34,35,39]
# n = int(input('순회 횟수는 : '))
#
# def rotate(inL,inN):
#     for i in range(inN):
#         last = inL.pop()
#         inL.insert(0,last)
#     min_dif = 100
#     length = len(inL)
#     for i in range(length):
#         dif = abs(inL[(i+inN)%length] - inL[i])
#         if min_dif > dif:
#             min_dif = dif
#             idx = i
#     print('index : %d\nvalue : %d, %d' % (idx,inL[(idx+inN)%length],inL[idx]))
#
# rotate(l,n)


#80 순열과 조합 - 나중에
# def comb(arg=0):
#     if arg == n:
#         output.append((''.join(path))
#         return
#     
#
# lst = input().split(',')
# n = int(input())
# path = ['']*n
# output = []
# comb()



