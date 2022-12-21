# 백준 11687 팩토리얼 0의 개수

M = int(input())
l, r, ans = 1, M*5, 0
def find(n):
    num = 0
    while n >= 5:
        num += n // 5
        n //= 5
    return num
while l <= r:
    m = (l+r)//2
    rst = find(m)
    if rst < M:
        l = m+1
    else:
        r = m-1
        ans = m
if find(ans) == M:
    print(ans)
else:
    print(-1)