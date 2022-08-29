t = int(input())

for tc in range(1, t + 1) :
    min_value = -1
    n, a, b = map(int, input().split())
    for r in range(1, n + 1) :
        c = 1
        while r * c <= n :
            value = a * (abs(r - c)) + b * (n - (r * c))
            if min_value == -1 :
                min_value = value
            else :
                min_value = min(min_value, value)
            c += 1

    print('#%d %d' % (tc, min_value))