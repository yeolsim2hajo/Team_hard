#18870 좌표 압축
# N = int(input())
# numbers = list(map(int,input().split()))
# data = sorted((set(numbers)))
# result = [0] * N
# for i in range(N):
#     result[i] = data.index(numbers[i])
# print(*result)

# 시간초과 날 듯
# N = int(input())
# numbers = list(map(int,input().split()))
# result = [0] * N
# for i in range(N):
#     cnt = 0
#     visited = set()
#     for j in range(N):
#         if numbers[j] not in visited and numbers[j] < numbers[i]:
#             visited.add(numbers[j])
#             cnt += 1
#     result[i] = cnt
# print(*result)

# 풀었지만, 메모리, 시간 오래 걸림
# N = int(input())
# numbers = list(map(int,input().split()))
# data = sorted(set(numbers))
# numbers = list(enumerate(numbers))
# numbers.sort(key=lambda x:x[1])
# result = [0] * N
# numbers_i = data_i = 0
# while numbers_i < N:
#     if numbers[numbers_i][1] == data[data_i]:
#         result[numbers[numbers_i][0]] = data_i
#         numbers_i += 1
#     else:
#         data_i += 1
#
# print(*result)


#1107 리모컨
channel = input()
M = int(input())
min_path = abs(int(channel) - 100)
n = len(channel)
if min_path >= n:
    if M:
        buttons = input().split()
        position = []
        for i in range(n):
            number = channel[i]
            if number in buttons:
                position.append(i)
        if position:
            def find_min_path():
                global min_path
                possible_button = list(map(str, [i for i in range(1, 10) if str(i) not in buttons]))
                via = list(map(str,channel))
                for idx in position:
                    for button in possible_button:



                # q = [(button, 1) for button in possible_button]
                # target = int(channel)
                # limit = min(n + 2, 6)
                # while q:
                #     number, length = q.pop(0)
                #     if length > limit:
                #         return
                #     if n - 1 <= length <= n + 1:
                #         dif = abs(target - int(number))
                #         if str(dif) in possible_button:
                #             if dif + n < min_path:
                #                 min_path = dif + n
                #     for i in possible_button:
                #         q.append((number + i, length + 1))

            find_min_path()
        else:
            min_path = n
    else:
        min_path = min(min_path, n)
print(min_path)