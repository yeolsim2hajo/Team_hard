arr = [3,5,1,1,2,3,2]

lst = list(map(int, input().split()))


result = []
for i in range(len(lst)):
    cnt = 0
    for k in range(len(arr)):
        if arr[k] == lst[i]:
            cnt += 1
    result.append(cnt)

for i in range(len(lst)):
    print(f'{lst[i]}={result[i]}개')