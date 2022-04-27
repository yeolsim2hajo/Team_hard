N = int(input()) # 과목 수
score = list(map(int, input().split()))
# map(int, input().split())로 할 경우 안됨.

Max = max(score)
Sum = 0

for i in score:
    Sum += (i/Max*100)

average = Sum/N
print(average)