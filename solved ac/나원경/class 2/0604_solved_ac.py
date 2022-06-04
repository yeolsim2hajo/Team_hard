#10866 덱

# deque import X (readline 안 쓰면 시간 초과)
# from sys import stdin
# deque = []
# N = int(input())
# new_input = stdin.readline
# size = 0
# for _ in range(N):
#     command = new_input().rstrip()
#     if command == 'size':
#         answer = size
#     elif command == 'empty':
#         answer = int(not size)
#     elif command == 'front':
#         answer = deque[0] if size else -1
#     elif command == 'back':
#         answer = deque[-1] if size else -1
#     elif command == 'pop_front':
#         answer = deque.pop(0) if size else -1
#         size = size-1 if size else 0
#     elif command == 'pop_back':
#         answer = deque.pop() if size else -1
#         size = size-1 if size else 0
#     else:
#         command = command.split()
#         size += 1
#         if command[0] == 'push_front':
#             deque.insert(0,command[1])
#         else:
#             deque.append(command[1])
#         continue
#     print(answer)


# import deque(deque만 하면 시간 초과) - deque 안 한 것보다 시간, 메모리가 더 나옴?
# import collections
# from sys import stdin
# deque = collections.deque()
# N = int(input())
# new_input = stdin.readline
# size = 0
# for _ in range(N):
#     command = new_input().rstrip()
#     if command == 'size':
#         answer = size
#     elif command == 'empty':
#         answer = int(not size)
#     elif command == 'front':
#         answer = deque[0] if size else -1
#     elif command == 'back':
#         answer = deque[-1] if size else -1
#     elif command == 'pop_front':
#         answer = deque.popleft() if size else -1
#         size = size-1 if size else 0
#     elif command == 'pop_back':
#         answer = deque.pop() if size else -1
#         size = size-1 if size else 0
#     else:
#         command = command.split()
#         size += 1
#         if command[0] == 'push_front':
#             deque.appendleft(command[1])
#         else:
#             deque.append(command[1])
#         continue
#     print(answer)

# 2108 통계학
# from sys import stdin
# N = int(input())
# freq = {}
# numbers = []
# new_input = stdin.readline
# total = 0
# for _ in range(N):
#     number = int(new_input())
#     if freq.get(number):
#         freq[number] += 1
#     else:
#         freq[number] = 1
#     total += number
#     numbers.append(number)
# numbers.sort()
# cnt = 1
# key_list = []
# for key, value in freq.items():
#     if value > cnt:
#         cnt = value
#         key_list = [key]
#     elif value == cnt:
#         key_list.append(key)
# if len(key_list) > 1:
#     key_list.sort()
#     most = key_list[1]
# else:
#     most = key_list[0]
# print(round(total/N), numbers[N//2], most, numbers[-1]-numbers[0], sep='\n')


# statistics 사용 - 메모리, 시간 더 나옴
# from sys import stdin
# from statistics import mean, median, multimode
# N = int(input())
# numbers = []
# new_input = stdin.readline
# for _ in range(N):
#     numbers.append(int(new_input()))
# cnt = 1
# freq_list = multimode(numbers)
# if len(freq_list) > 1:
#     freq_list.sort()
#     most = freq_list[1]
# else:
#     most = freq_list[0]
# print(round(mean(numbers)), median(numbers), most, max(numbers)-min(numbers), sep='\n')


# 섞음 - 시간 더나왔지만 메모리는 줄어듦
# from sys import stdin
# from statistics import mean, multimode
# N = int(input())
# numbers = []
# new_input = stdin.readline
# for _ in range(N):
#     numbers.append(int(new_input()))
# numbers.sort()
# cnt = 1
# freq_list = multimode(numbers)
# if len(freq_list) > 1:
#     freq_list.sort()
#     most = freq_list[1]
# else:
#     most = freq_list[0]
# print(round(mean(numbers)), numbers[N//2], most, numbers[-1] - numbers[0], sep='\n')