weight = []
limit = int(input())
n = int(input())
for i in range(5):
    weight.append(int(input()))


cnt = 0
total = 0

for i in range(len(weight)):
    total += weight[i]
    if total <= limit:
        cnt += 1


print(cnt)