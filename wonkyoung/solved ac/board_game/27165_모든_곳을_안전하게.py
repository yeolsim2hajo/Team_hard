#230129
n = int(input())
cnt = list(map(int, input().split()))
choice = int(input())
unsafe = []
for i in range(n+1):
    if cnt[i] == 1:
        unsafe.append(i)
length = len(unsafe)
answer = 'NO'
if length > 0:
    start, end = unsafe[0], unsafe[0] + choice
    if length == 2:
        if end == unsafe[1]:
            answer = 'YES'
    elif length == 1:
        if end <= n and cnt[end] >= 1:
            answer = 'YES'
else:
    for i in range(n + 1):
        if cnt[i] >= 3:
            unsafe.append(i)
    length = len(unsafe)
    for start in unsafe:
        end = start + choice
        if end <= n and cnt[end] >= 1:
            answer = 'YES'
            break
    if length == 0:
        for i in range(n-choice+1):
            if cnt[i]:
                break
        else:
            for i in range(n-choice+1, n+1):
                if cnt[i]:
                    answer = 'YES'
                    start = end = i
                    break
print(answer)
if answer == 'YES':
    print(start, end)


