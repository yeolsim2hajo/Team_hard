case = 1
while 1:
    n = int(input())
    if n == 0:
        break
    names = [input() for _ in range(n)]
    li = [0]*n
    for _ in range(2*n-1):
        i, a = input().split()
        li[int(i)-1] += 1
    res = names[[i for i in range(n) if li[i] != 2][0]]
    print(f"{case} {res}")
    case += 1