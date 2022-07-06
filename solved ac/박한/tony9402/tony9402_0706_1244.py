# 백준 1244 스위치 켜고 끄기

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
def male(a):
    for i in range(a-1, n, a):
        if lst[i] == 0:
            lst[i] = 1
        else:
            lst[i] = 0
def female(a):
    if lst[a] == 0:
        lst[a] = 1
    else:
        lst[a] = 0
    rst, ans = min(a, n-a-1), 0
    while ans < rst:
        ans += 1
        if lst[a+ans] != lst[a-ans]:
            break
        if lst[a+ans] == 0:
            lst[a+ans], lst[a-ans] = 1, 1
        else:
            lst[a+ans], lst[a-ans] = 0, 0
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        male(b)
    else:
        female(b-1)
for i in range(1, n, 20):
    print(*lst[i:i+20])

# 뭐가 틀린 거지?