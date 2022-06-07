#1389 케빈 베이컨의 6단계 법칙
# import sys
# new_input = sys.stdin.readline
# N, M = map(int,input().split())
# link = [set() for _ in range(N+1)]
# for _ in range(M):
#     x,y = map(int, new_input().split())
#     link[x].add(y)
#     link[y].add(x)
# min_cnt = N ** 2
# user_number = 0
# def find_min(user,number):
#     for i in link[user]:
#
#
#
# def find_number(user):
#     global min_cnt
#     cnt = 0
#     for i in range(1,N+1):
#         if i != user:
#             if i in link[user]:
#                 cnt += 1
#             else:
#                 cnt += find_min(user,i)
#     if cnt < min_cnt:
#         min_cnt = cnt
#
# for i in range(1,N+1):
#     find_number(i)


#1463 1로 만들기
# X = int(input())
# min_cnt = 0
# def calc(arg):
#     global min_cnt
#     visited = set()
#     q = [(arg,0)]
#     visited.add(arg)
#     while q:
#         number, cnt = q.pop(0)
#         if number == 1:
#             min_cnt = cnt
#             return
#         result = [divmod(number,3), divmod(number,2), number-1]
#         if result[0][1] == 0 and result[0][0] not in visited:
#             q.append((result[0][0], cnt+1))
#             visited.add(result[0][0])
#         if result[1][1] == 0 and result[1][0] not in visited:
#             q.append((result[1][0], cnt+1))
#             visited.add(result[1][0])
#         if result[2] not in visited:
#             q.append((result[2], cnt+1))
#             visited.add(result[2])
#
# if X > 1:
#     calc(X)
# print(min_cnt)


#1541 잃어버린 괄호
# formula = input()
# split_formula = []
# plus = minus = 0
# start = 0
# calc = {'+', '-'}
# for i in range(len(formula)):
#     if formula[i] in calc:
#         split_formula.extend([int(formula[start:i]),formula[i]])
#         start = i+1
# split_formula.append(int(formula[start:]))
#
# length = len(split_formula)
# result = split_formula[0]
# for i in range(1,length,2):
#     if split_formula[i] == '+':
#         result += split_formula[i+1]
#         plus = plus + 1
#     else:
#         result -= split_formula[i+1]
#         minus = minus + 1
# if plus and minus:
#     def calc(start):
#         pass
#     # 괄호 여러 개
#     # 괄호 시작과 끝
#     for i in range(2,length,2):
#         for j in range()
#             calc(i)
#
# print(result)


#1620 나는야 포켓몬 마스터 이다솜

# pypy로 해도 시간 초과
# import sys
# N, M = map(int,input().split())
# new_input = sys.stdin.readline
# monster = ['']
# for _ in range(N):
#     monster.append(new_input().rstrip())
# for _ in range(M):
#     problem = new_input().rstrip()
#     if problem.isdigit():
#         problem = int(problem)
#         print(monster[problem])
#     else:
#         for i in range(1,N+1):
#             if monster[i] == problem:
#                 print(i)
#                 break

# dict - pypy로 하면 시간 초과 x
# import sys
# N, M = map(int,input().split())
# new_input = sys.stdin.readline
# monster = {}
# for i in range(N):
#     monster[new_input().rstrip()] = i+1
# for _ in range(M):
#     problem = new_input().rstrip()
#     if problem.isdigit():
#         problem = int(problem)
#         for key,value in monster.items():
#             if value == problem:
#                 print(key)
#                 break
#     else:
#         print(monster[problem])


# dict 시간 초과 해결 위해.... - 메모리 덜 차지 & 시간 빠름
import sys
N, M = map(int,input().split())
new_input = sys.stdin.readline
monster = {}
for i in range(N):
    name = new_input().rstrip()
    monster[name] = i+1
    monster[i+1] = name
for _ in range(M):
    problem = new_input().rstrip()
    if problem.isdigit():
        problem = int(problem)
    print(monster[problem])