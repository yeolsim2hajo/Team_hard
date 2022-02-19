T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    for a in range(N):
        for b in range(a+1, N):
            if lst[a] > lst[b]:
                lst[a], lst[b] = lst[b], lst[a]
    rst = 0
    for i in range(N):
        if lst[i] < M:
            rst += 1
            break
        if (lst[i]//M)*K < (i+1):
            rst += 1
            break
    if not rst:
        print(f"#{t+1} Possible")
    else:
        print(f"#{t+1} Impossible")
