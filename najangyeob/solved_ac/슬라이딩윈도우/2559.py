import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data  = list(map(int, input().split()))

total = sum(data[0:k])
answer = total
for i in range(k, n):
    total += data[i] - data[i - k]
    answer = max(answer, total)
print(answer)


# n, k = map(int, input().split())
# data  = list(map(int, input().split()))
# answer = []
# for i in range(0, n-k+1):
#     answer.append(int(sum(data[i:i+k]))) #0:2, 1:3, 2:4, 3:5, 4:6, 5:7, 6:8, 7:9 8:10


# print(max(answer))