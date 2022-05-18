#10816 숫자 카드2
# 시간 초과
# N = int(input())
# cards = list(map(int,input().split()))
# visited = [False] * N
# M = int(input())
# conf = list(map(int,input().split()))
#
# for i in range(M):
#     cnt = 0
#     for j in range(N):
#         if visited[j] == False and conf[i] == cards[j]:
#             cnt += 1
#             visited[j] = True
#     print(cnt, end=' ')

# N = int(input())
# cards = list(map(int,input().split()))
# check = {}
# for card in cards:
#     if check.get(card, -1) == -1:
#         check[card] = 1
#     else:
#         check[card] += 1
# M = int(input())
# conf = list(map(int,input().split()))
# for i in range(M):
#     if check.get(conf[i], -1) == -1:
#         print(0, end=' ')
#     else:
#         print(check[conf[i]], end=' ')


#10828 스택
# 시간 초과
# N = int(input())
# stack = []
# command_list = {
#     'pop' : lambda : -1 if not stack else stack.pop(),
#     'size' : lambda : len(stack),
#     'empty' : lambda : int(not stack),
#     'top' : lambda : -1 if not stack else stack[-1]
# }
# for _ in range(N):
#     command = input().split()
#     word = command[0]
#     if word == 'push':
#         stack.append(command[1])
#     else:
#         print(command_list[word]())

# 시간 초과
# 틀림
# N = int(input())
# stack = []
# command_list = [{
#     'top' : -1,
#     'pop' : -1,
#     'size' : 0
# },
# {
#     'top': lambda : stack[-1],
#     'pop': lambda : stack.pop(),
#     'size': lambda : len(stack)
# }]
#
# for _ in range(N):
#     command = input().split()
#     empty = not stack
#     word = command[0]
#     if word == 'push':
#         stack.append(command[1])
#     elif word == 'empty':
#         print(empty)
#     elif empty:
#         print(command_list[0][word])
#     else:
#         print(command_list[1][word]())

