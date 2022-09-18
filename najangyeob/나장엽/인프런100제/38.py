arr = list(map(int, input().split()))

cnt = 0

if len(set(arr)) <= 3:
    cnt = len(arr)
else:
    rank4 = sorted(list(set(arr)), reverse=True)[3]
    sorted_arr= sorted(arr, reverse=True)
    for i in sorted_arr:
        if rank4 == i:
            break
        else:
            cnt += 1

print(cnt)