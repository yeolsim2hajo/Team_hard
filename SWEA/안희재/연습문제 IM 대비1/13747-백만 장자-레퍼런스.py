T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    sol = 0
    Max = lst[N-1]
    for i in range(N-2, -1, -1):
        if Max < lst[i]:
            Max = lst[i]
        else:
            sol += (Max - lst[i])
    
    print(f'#{tc}', sol)