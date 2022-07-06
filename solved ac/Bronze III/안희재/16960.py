N, M = map(int,input().split())

# switch에 각각 어떤 램프를 켤 수 있는지에 대한 정보를 저장
    # switch리스트의 0번인덱스는 1번 스위치가 켤 수 있는 램프정보를 담고 있다
    # swtich = [[1,3,5], [2], [3,4,5], [1]]

switch = [0 for _ in range(N)]
for k in range(N):
    info = list(map(int,input().split()))
    tmp = []
    for i in range(1,len(info)):
        tmp.append(info[i])
    switch[k] = tmp

# N-1개의 스위치를 이용해서 모든 램프를 켤 수 있다면 "1"(true)를 출력해야 한다
# 첫 반복문은 어떤 스위치를 제외할지에 대한 것이다
answer = 0
for i in range(N):

    # bucket의 1번인덱스는 1번램프의 정보이다
    # 만약, 이것이 1이라면 켜졌다는 뜻이며, 0이라면 꺼져있다는 뜻
    # 즉, bucket의 합이 M과 같다면 모든 램프가 켜져있다는 뜻이 된다
    bucket = [0] * (M+1)
    for j in range(N):
        if j == i: continue # i번째 스위치 제외
        for k in range(len(switch[j])):
            bucket[switch[j][k]] = 1

    if sum(bucket) == M:
        answer = 1

print(answer)

