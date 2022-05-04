T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    # banana bana

    cnt = 0
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            cnt += 1

    print(f'#{tc} {len(a)-(len(b)-1)*cnt}')
