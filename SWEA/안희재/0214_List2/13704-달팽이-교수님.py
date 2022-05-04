test_case=int(input())
for tc in range(test_case):
    n=int(input())
    arr=[[0 for _ in range(n)] for _ in range(n)]

    value=1
    dir=1 # 좌표가 증가 또는 감소
    y=0
    x=-1

    while n>0:
        for _ in range(n):
            x+=dir
            arr[y][x]=value
            value+=1
        n-=1
        for _ in range(n):
            y+=dir
            arr[y][x]=value
            value+=1
        dir*=-1

    print('#{}'.format(tc+1))

    for i in range(len(arr)):
        print(*arr[i])