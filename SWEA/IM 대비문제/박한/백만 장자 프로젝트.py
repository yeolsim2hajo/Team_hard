T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    rst = 0
    cnt = 0
    for n in range(N):
        if n!=N-1:
            if lst[n] <= lst[n+1]:
                rst += lst[n]
                cnt += 1
            else:
                if lst[n] == max(lst[n:]):
                    ans += (lst[n]*cnt - rst)
                    rst = 0
                    cnt = 0
                else:
                    rst += lst[n]
                    cnt += 1
        else:
            ans += (lst[n]*cnt - rst)
    print(f"#{t+1} {ans}")