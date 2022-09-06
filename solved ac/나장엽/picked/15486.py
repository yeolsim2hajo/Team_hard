# DFS -> 시간초과
# def func(day, total):
#     global answer

#     if day == N: # 퇴사일일 경우
#         answer = max(answer, total) # 최대이익을 정산
#         return

#     t = data[day][0] # cost
#     p = data[day][1] # profit

#     # 해당 일부터 상담하는 경우
#     if t + day <= N: 
#         func(t + day, total + p)

#     # 해당 일의 다음 날부터 상담하는 경우
#     func(day + 1, total)


# N = int(input()) # 1 <= N <= 1,500,000
# data = [list(map(int, input().split())) for _ in range(N)]
# answer = 0

# # 순차적으로 방문,
# for day in range(N):
#     func(day, 0)

# print(answer)


# DP
import sys
input = sys.stdin.readline

def func():
    for day in range(N - 1, -1, -1): # reverse search
        t = data[day][0] # cost
        if day + t <= N: 
            p = data[day][1] # profit
            memo[day] = max(memo[day + 1], memo[day + t] + p) # 최대이익 갱신, day + t 까지 근무한 경우의 이익과, i + 1 까지 근무한 경우의 이익 중 최댓값으로 갱신
        else: # 해당일에 근무하지 않았을 경우, i + 1일까지 근무한 경우의 이익과 같음.
            memo[day] = memo[day + 1]

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
memo = [0] * (N + 1)
func()
print(memo[0])