def fn():
    a, b = map(int, input().split())
    return a+b


def output(n):
    i = 5
    while True:
        print(i, end= ' ')
        if i >= n:
            break
        i += 1
        
output(fn())