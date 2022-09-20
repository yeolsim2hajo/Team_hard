# i번째 버스 노선 : Ai이상, Bi이하만 다님
# N은 버스 노선 개수
# A1=1, B1=3 -> 첫번째 버스노선은 1~3만 다님
# 두번째 버스노선은 2~5만 다님

# 1. 빈 버켓 P의 개수만큼 만들고,
# 2. 각 노선마다 1씩 추가해주고
# 최종적으로 그 버킷 출력하면 될듯?
T = int(input())

for tc in range(1,T+1):

    N = int(input())
    arr = []
    for i in range(N):
        route = list(map(int,input().split()))
        arr.append(route)

    P = int(input())
    arr2 = []
    for i in range(1,P+1):
        station = int(input())
        arr2.append(station) 

    bucket = [0] * 5001 # 정류장 개수+1만큼 버켓 만들고, (1번인덱스 = 1번정류장)
                        # 아니지, 넉넉하게 만들어야 함

    for i in range(N): # 각 노선만큼 반복문 돌려서, 각 정류장 지날때마다 +1
        for j in range(arr[i][0],arr[i][1]+1):
            bucket[j] += 1

    # 버스정류장(C1,2..의 값이)이 1,2,3,4,5가 아니라 1,2,3,6,9이런식일 수도 있으므로
    for i in range(len(arr2)):
        arr2[i] = bucket[arr2[i]]

    print(f'#{tc}', *arr2)