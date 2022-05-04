T = int(input())

for i in range(1,T+1):
    P, PA, PB = map(int,input().split())

    arr = []
    for j in range(1,P+1):
        arr.append(j)

    # 이 문제의 경우, 페이지를 못 찾는 경우는 없으므로, s > e : break 써줄 필요 없음
    def bs(s,e,value):
        cnt = 0 # 이거 밖에다 써줘야지
        while (1):
            m = (s+e)//2
            if arr[m] == value:
                cnt += 1
                return cnt # 여기서 종료
            elif arr[m] < value:
                s = m+1
                cnt += 1
            elif arr[m] > value:
                e = m-1
                cnt += 1

    answer = ''
    if bs(1,P,PA) > bs(1,P,PB):
        answer = 'B'
    elif bs(1,P,PA) < bs(1,P,PB):
        answer = 'A'
    else:
        answeer = 0

    print(f'#{i}', answer)