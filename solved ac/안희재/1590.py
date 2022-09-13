N, T = map(int, input().split())
res = []
for _ in range(N):
    t, d, n = map(int, input().split())
    li = [t+d*i for i in range(n)]
    if li[-1] < T:
        continue
    s, e = 0, n-1
    a = 0
    while s <= e:
        m = (s+e)//2
        if li[m] >= T:
            a = m
            e = m-1
        else:
            s = m+1
    res.append(li[a]-T)
print(min(res) if res else -1)