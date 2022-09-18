a, b = map(int, input().split())
cnt = 0
while True:
    if a and b == 100:
        break
    cnt += 1
    a += 1
    b += 1
print(cnt)