# 운동을 할 수 없는 경우 -> 초기맥박 + 운동 시 증가하는 맥박 > 최대맥박 -> 반복문을 나온다
# 현재 맥박 + 운동 시 증가하는 맥박 <= 최대맥박 -> 운동 가능 / 운동 시간 증가, 현재 맥박 = 현재맥박 + 증가 맥박
# 휴식 현재 맥박 + 운동시 증가하는 맥박 > 최대 맥박 -> 현재맥박 - R이 m보다 작을 때 현재 맥박은 m이기 때문에, max(현재맥박 - R, m)


N, m, M, T, R = map(int, input().split())

workout, rest = 0, 0
heart = m

while workout < N:
    if m + T > M:
        break

    if heart + T <= M:
        heart += T
        workout += 1

    else:
        heart = max(heart-R, m)

    
    rest += 1

print(rest if workout == N else -1)
