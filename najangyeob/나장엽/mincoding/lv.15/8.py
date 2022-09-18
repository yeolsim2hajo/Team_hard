arr = [list(input()) for _ in range(5)]

result = []

for i in range(5):
    result.append(len(arr[i]))
max = result[0]
idx = 0
for i in range(len(result)):
    if max < result[i]:
        max = result[i]
        idx = i
    else:
        max = max


print(*arr[idx], sep='')