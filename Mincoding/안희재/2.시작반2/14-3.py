a, b = map(int,input().split())

cnt = 0
while 1:
    a += 1
    b += 1
    cnt += 1
    if a >= 100 and b >= 100:
        print(cnt)
        break