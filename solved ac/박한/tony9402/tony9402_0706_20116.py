# 백준 20116 상자의 균형

n, l = map(int, input().split())
lst = list(map(int, input().split()))
a, ans, rst = 0, 1, 0
while a < n-1:
    rst += lst[n-1-a]
    if rst/(a+1) >= lst[n-2-a]+l or rst/(a+1) <= lst[n-2-a]-l:
        ans = 0
        break
    a += 1
if ans:
    print("stable")
else:
    print("unstable")