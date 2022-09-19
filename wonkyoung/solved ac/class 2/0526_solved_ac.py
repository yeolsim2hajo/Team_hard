#10845 큐
# from collections import deque
# N = int(input())
# queue = deque()
# command_check ={
#     'size': lambda x: x,
#     'empty': lambda x: int(not x),
#     'front' : lambda x: queue[idx] if x else -1,
#     'back' : lambda x: queue[-1] if x else -1
# }
# for _ in range(N):
#     command = input()
#     size = 0
#     idx = 0
#     print(command)
#     if command == 'pop':
#         print(queue[idx])
#         size = size-1 if size else 0
#     elif command_check.get(command, -2) == -2:
#         queue.append(command[-1])
#         size += 1
#     else:
#         print('size :',size)
#         print(command_check[command](size))


#10989 수 정렬하기 3
# numbers = {}
# N = int(input())
# for _ in range(N):
#     number = int(input())
#     if number == 1:
#         print(1)
#     elif numbers.get(number):
#         numbers[number] += 1
#     else:
#         numbers[number] = 1
# keys = sorted(numbers)
# for key in keys:
#     for _ in range(numbers[key]):
#         print(key)


#11651 좌표 정렬하기 2
N = int(input())
position = []
for _ in range(N):
    position.append(list(map(int,input().split())))
position.sort(key=lambda x:(x[1], x[0]))
for i in range(N):
    print(*position[i])
