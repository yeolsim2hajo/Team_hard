finger = int(input())
cnt = int(input())

if 2<=finger<=4:
    if cnt % 2 == 0:
        cnt //= 2
        print((cnt * 8) + (finger - 1))
    else:
        cnt //= 2
        print((cnt * 8) + (1 - finger))
elif finger == 1:
    print(cnt * 8)
else:
    print(cnt*8 + 4)