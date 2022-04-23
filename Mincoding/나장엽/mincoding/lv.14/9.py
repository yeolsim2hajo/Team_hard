arr = [10,50,40,20,30,40]
target = list(map(int, input().split()))
result = []
for i in range(len(target)):
    cnt = 0
    for k in range(len(arr)):
        if arr[k] > target[i]:
            cnt += 1
    result.append(cnt)

for i in range(len(target)):
    print(f'{target[i]}={result[i]}개')