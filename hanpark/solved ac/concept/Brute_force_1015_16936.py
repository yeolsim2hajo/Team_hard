# 백준 16936 나3곱2

n = int(input())
ls = list(map(int, input().split()))
lst = []
def bf(a):
    global lst
    if len(a) == n:
        for i in range(1, n):
            if a[i-1] * 2 == a[i]:
                continue
            elif a[i-1] // 3 == a[i] and a[i-1] % 3 == 0:
                continue
            else:
                return
        lst = a
        return
    for i in range(n):
        if ls[i] not in a:
            bf(a + [ls[i]])
bf([])
print(*lst)