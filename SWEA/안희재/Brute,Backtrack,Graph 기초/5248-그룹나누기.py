# union find
# 참고로, 한번도 호출되지 않은 자는 단일 그룹형성
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split()) # 1번부터 N번까지 존재 / M개의 그룹쌍이 주어짐
    pair = list(map(int,input().split())) # pair의 길이는 M*2 
    arr = [0] * (N+1) # 버킷(1번부터 N번까지) -> 0번인덱스는 버림 걍

    for i in range(0,len(pair),2): # 0,1  2,3 .. 이렇게 짝이므로 -> step은 2
        # 1.둘다 아직 0 -> 아직 그룹 전 -> 앞의 숫자로 넘버링해줌 => ㄴㄴ 더 작은 숫자로 넘버링해주자 걍 (7,4) 이런경우 있으니까
        if arr[pair[i]] == 0 and arr[pair[i+1]] == 0:
            if pair[i] > pair[i+1]:
                arr[pair[i]], arr[pair[i+1]] = pair[i+1], pair[i+1]
            else:
                arr[pair[i]], arr[pair[i+1]] = pair[i], pair[i]
        # 2. 한쪽만 0이라면 -> 채워져있는 숫자로 나머지 0을 넘버링
        elif arr[pair[i]] == 0: # pair[i+1]은 숫자 채워져있음(=이미 그룹화)
            arr[pair[i]] = arr[pair[i+1]]
        elif arr[pair[i+1]] == 0: # 이번엔 pair[i]가 채워져있음
            arr[pair[i+1]] = arr[pair[i]]
        # 3. 둘다 숫자가 있다면, 더 작은 숫자로 그룹 넘버링.
            # 단,
            # 5 3 / 1 2 3 4 1 3 -> 마지막의 (1,3) 경우도 고려해줘야 함
            # 둘다 숫자가 있는 경우 바뀔 당사자뿐만 아니라, 그 당사자가 포함된 그룹까지 바꿔야 함
        else:
            if arr[pair[i]] > arr[pair[i+1]]:
                before, after = arr[pair[i]], arr[pair[i+1]]
                for j in range(len(arr)):
                    if arr[j] == before:
                        arr[j] = after
            else:
                before, after = arr[pair[i+1]], arr[pair[i]]
                for j in range(len(arr)):
                    if arr[j] == before:
                        arr[j] = after

    arr = arr[1:] # 인덱스와 출석번호 맞춰주기 위해 처음에 (N+1)칸 만들었으므로
    cnt = 0
    arr.sort() # 정렬시켜줘야 같은 그룹끼리 모여있음
    for i in range(len(arr)):
        if arr[i] == 0: # 0은 단일그룹이므로, 0나올때마다 group+1
            cnt += 1
        elif arr[i] != arr[i-1]: # 이전과 다른 숫자 = 새 그룹 등장 = group+1
            cnt += 1

    print(f'#{tc} {cnt}')