# 백준 20436 ZOAC 3

import sys
input = sys.stdin.readline

l, r = input().strip().split()
lst = list(input().strip())
ans, test = 0, 'qwertasdfgzxcv'
def find(a):
    key = [['q','w','e','r','t','y','u','i','o','p'], ['a','s','d','f','g','h','j','k','l'], ['z','x','c','v','b','n','m']]
    for x, y in enumerate(key):
        if a in y:
            i = y.index(a)
            j = x
            return i, j
for ls in lst:
    if l == ls or r == ls:
        ans += 1
    else:
        lx, ly = find(l)
        rx, ry = find(r)
        lsx, lsy = find(ls)
        if ls in test:
            ans += abs(lx-lsx) + abs(ly-lsy) + 1
            l, lx, ly = ls, lsx, lsy
        else:
            ans += abs(rx-lsx) + abs(ry-lsy) + 1
            r, rx, ry = ls, lsx, lsy
print(ans)