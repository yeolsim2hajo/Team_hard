#7662 이중 우선순위 큐
# from heapq import heappush, heappop, nlargest
# from sys import stdin
# T = int(input())
# for _ in range(T):
#     K = int(input())
#     q = []
#     new_input = stdin.readline
#     for _ in range(K):
#         command = new_input().split()
#         if command[0] == 'I':
#             heappush(q, int(command[1]))
#         elif command[1] == '1':
#             length = len(q)
#             max_val = q[length-1]
#             for i in range(length//2+1, length-1):
#                 ma
#         else:
#             heappop(q)
#     if q:
#         pass
#     else:
#         print('EMPTY')

#1598 꼬리를 무는 숫자 나열
# num1, num2 = map(int, input().split())
# y1, y2 = (num1-1)%4, (num2-1)%4
# x1, x2 = (num1-1)//4, (num2-1)//4
# print(abs(y1-y2)+abs(x1-x2))


# num1, num2 = map(int, input().split())
# x1, y1 = divmod(num1-1, 4)
# x2, y2 = divmod(num2-1, 4)
# print(abs(y1-y2)+abs(x1-x2))
