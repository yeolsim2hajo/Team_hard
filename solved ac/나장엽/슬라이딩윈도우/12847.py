
# 시간초과
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# income = list(map(int, input().split()))

# # start = 0
# # end = m - 1

# # answer = []
# # while True:
# #     if end == len(income):
# #         break

# #     Max_income = 0
# #     for i in range(start, end + 1, 1):
# #         Max_income += income[i]
# #     answer.append(Max_income)

# #     start += 1 # 0, 1, 2
# #     end += 1 # 2, 3, 4


# # print(max(answer))

# 시간초과
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# income = list(map(int, input().split()))
# answer = []

# for i in range(0, n - m + 1):
#     Sum = 0
#     Sum += int(sum(income[i:i+m])) # 0, 3 / 1, 4 /2, 5
#     answer.append(Sum)


# print(max(answer))

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
income = list(map(int, input().split()))

slide = sum(income[0:m])
answer = slide

for i in range(m, n):
    slide += income[i] - income[i - m] #인덱스 m 부터 n까지 탐색 -> 현재의 숫자를 더하고 처음 더한 값을 빼기 0, 1, 2 ->  1, 2, 3 -> 2, 3, 4
    answer = max(answer, slide)


print(answer)