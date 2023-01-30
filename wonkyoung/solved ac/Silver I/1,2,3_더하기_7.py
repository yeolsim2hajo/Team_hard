#230121
T = int(input())
div = int(1e9)+9

for _ in range(T):
    n, m = map(int, input().split())
    cnt, min_cnt = 0, n%3+1
    if n == m:
        print(1)
    elif n - 1 == m:
        print(n)
    elif m < min_cnt:
        print(0)


    print(cnt%div)
