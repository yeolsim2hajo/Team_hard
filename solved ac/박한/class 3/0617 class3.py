# 백준 class 3++ 1107 리모컨

n = int(input())
m = int(input())
if m:
    lst = list(map(int, input().split()))
else:
    lst = []

def check(a, ls):
    rst = 0
    b = str(a)
    for i in range(len(b)):
        if int(b[i]) in ls:
            rst = 1
            break
    return rst

if n == 100:
    print(0)
else:
    abc, efg, hij = 0, len(str(n)), abs(n-100)
    if not check(n, lst):
        print(min(hij, efg))
    else:
        while 1:
            abc += 1
            if not check(n-abc, lst) or not check(n+abc, lst):
                print(min(hij, efg+abc))
                break