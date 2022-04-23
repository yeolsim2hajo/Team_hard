stamps = list(map(int,input().split()))

stamps.sort()

for i in range(len(stamps)-1):
    if stamps[i] + 1 != stamps[i+1]:
        print('NO')
        break
else:
    print('YES')

# 아 문제 진짜 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ