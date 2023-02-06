#230119
# 시간 많이 걸림
# import sys
# new_input = sys.stdin.readline
# def cnt_letter(N):
#     cnt = 0
#     def dfs(level, half, whole):
#         nonlocal cnt
#         if level == 2*N-1:
#             cnt += 1
#             return
#         if half:
#             dfs(level+1, half-1, whole)
#         if whole:
#             dfs(level+1, half+1, whole-1)
#
#     dfs(1, 1, N-1)
#     return cnt
# while True:
#     N = int(new_input())
#     if N == 0:
#         break
#     print(cnt_letter(N))


#230127
# import sys
# new_input = sys.stdin.readline
# memoization = [0] * 31
# def cnt_letter(N):
#     if memoization[N]:
#         return memoization[N]
#     cnt = 0
#     def find_before(level):
#         nonlocal cnt
#         if memoization[level-1]:
#             return memoization[level-1]
#         else:
#             cnt = find_before(level-1)
#
#
#     def dfs(level, half, whole):
#         nonlocal cnt
#         cnt = find_before(level)
#
#     dfs(N, N-1, N-2)
#     return cnt
# while True:
#     N = int(new_input())
#     if N == 0:
#         break
#     print(cnt_letter(N))

#230202
# import sys
# new_input = sys.stdin.readline
# cases = [0] * 31
# cases[1], cases[2] = 1, 2
# def cnt_letter(N):
#     if cases[N]:
#         return cases[N]
#     cnt = alpha = 0
#     path = ['w', 'w']
#     # cnt = [2, 1]
#     def dfs(level, half, whole, limit):
#         nonlocal alpha
#         # print(level, half, whole, path)
#         if level == limit:
#             alpha += 1
#             # print(path)
#             return
#         new_whole, new_half = whole-1, half-1
#         if new_whole >= 0:
#             path.append('w')
#             dfs(level+1, half, new_whole, limit)
#             path.pop()
#         if half >= whole:
#             path.append('h')
#             dfs(level+1, new_half, whole, limit)
#             path.pop()
#
#     def find_before(level):
#         nonlocal cnt, alpha
#         if cases[level-1] == 0:
#             find_before(level - 1)
#         cnt = cases[level-1]
#         if alpha: alpha = 0
#         dfs(3, level-1, level-2, 2*level)
#         cases[level] = cnt + alpha
#     find_before(N)
#     return cases[N]
# while True:
#     N = int(new_input())
#     if N == 0:
#         break
#     print(cnt_letter(N))



# 16% 시간 초과
# import sys
# new_input = sys.stdin.readline
# cases = [0] * 31
# cases[1], cases[2] = 1, 2
# def cnt_letter(N):
#     if cases[N]:
#         return cases[N]
#     alpha = 0
#     def dfs(level, half, whole, limit):
#         nonlocal alpha
#         if level == limit:
#             alpha += 1
#             return
#         if whole >= 1:
#             dfs(level+1, half, whole-1, limit)
#         if half >= whole:
#             dfs(level+1, half-1, whole, limit)
#
#     def find_before(level):
#         nonlocal cnt, alpha
#         if cases[level-1] == 0:
#             find_before(level - 1)
#         if alpha: alpha = 0
#         dfs(3, level-1, level-2, 2*level)
#         cases[level] = cases[level-1] + alpha
#     find_before(N)
#     return cases[N]
# while True:
#     N = int(new_input())
#     if N == 0:
#         break
#     print(cnt_letter(N))

# 직접 계산
from math import factorial
def cnt_cases():
    if N <= 2:
        return N
    fact = factorial(N-1)
    # w...xxx...h
    total = factorial(2*N-2)// (fact * fact)
    # whh....xxx...h
    # i = 1
    minus = factorial(2*N-4)//(fact * factorial(N-3))
    total -= minus
    for i in range(2, N-2):
        minus = minus//(N-2-i)
        fact //= (N-i+1)
        total -= factorial(2*N-2-2*i) // (fact * minus)
    if N >= 4:
        total -= 2
    # i = 2
    # wwhhh...xxx...h
    return total

from sys import stdin
new_input = stdin.readline
while True:
    N = int(new_input())
    if N == 0:
        break
    print(cnt_cases())

    'ww/w/w/w/w/h'
    'wwhh'
    'wh'
    'wwhh'
    'wwhhh'
    'whhwwh'
    'wwhhhw'
    'whh'
    'wwwhhhh'
    '''
    (2*n-2)!//(n-1)!(n-1)! - 2
    '''

