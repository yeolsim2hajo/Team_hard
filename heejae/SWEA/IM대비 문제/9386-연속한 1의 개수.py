T = int(input())

for tc in range(1,T+1):
    n = int(input())
    line = input()
    # 이 문제 풀고, 고대유적 풀어야했는데.....
    # 고대유적 레퍼런스 방식으로 풀어보기
    max = 0
    for ruin in line.split('0'):
        now = len(ruin)
        if max < now: 
            max = now

    print(f'#{tc}', max)