# from collections import defaultdict
# N, M = map(int, input().split())
# subject = [1] * (N+1)
# match = defaultdict(set)
# for _ in range(M):
#     A, B = map(int, input().split())
#     match[B].add(A)
# for i in range(1,N+1):
#     pre = match.get(i)
#     for next in pre:
#         subject[i] = max(subject[i], subject[next] + 1)
# print(*subject[1:])




# N, M = map(int, input().split())
# subject = [1] * (N+1)
# match = [set() for _ in range(N+1)]
# for _ in range(M):
#     A, B = map(int, input().split())
#     match[A].add(B)
# for i in range(1,N):
#     for j in range(i+1, N+1):
#         if j in match[i]:
#             subject[j] =
#     for next in match[i]:
#         subject[next] = max(subject[next], subject[i] + 1)
# print(*subject[1:])


#1015 수열 정렬
# N = int(input())
# order = list(map(int, input().split()))
# numbers = [N] * N
# position = 1
# initial = 0
# def loop(outer_limit, inner_start):
#     global initial
#     for j in range(outer_limit):
#         for k in range(inner_start, N):
#             if order[k] == position and numbers[k] > i:
#                 numbers[k] = i
#                 initial = k
#                 return 1
#     return 0
# for i in range(N):
#     result = loop(1, initial+1)
#     if not result:
#         loop(N+1, 0)
# print(*numbers)


#1212 8진수 2진수
# N = input()
# match = ['000', '001', '010', '011', '100', '101', '110', '111']
# answer = ''
# for i in N:
#     target = int(i)
#     answer += match[target]
# print(int(answer))


#1837 암호제작
# P, K = map(int, input().split())
# if P%2 == 0:
#     print('BAD 2')
# else:
#     limit = min(K, P)
#     for i in range(3, limit+1, 2):
#         if P%i == 0:
#             print(f'BAD {i}')
#             break
#     else:
#         print('GOOD')


#11365 !밀비 급일
# while True:
#     sentence = input()
#     if sentence == 'END':
#         break
#     print(sentence[::-1])



# import sys
#
# new_input = sys.stdin.readline
# while True:
#     sentence = new_input().rstrip()
#     if sentence == 'END':
#         break
#     print(sentence[::-1])


# def main():
#     import sys
#
#     new_input = sys.stdin.readline
#     while True:
#         sentence = new_input().rstrip()
#         if sentence == 'END':
#             return
#         print(sentence[::-1])
# main()

