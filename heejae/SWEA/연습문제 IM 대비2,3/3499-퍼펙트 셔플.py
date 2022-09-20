T = int(input())

# N이 짝, 홀수인 경우에 따라 배열을 각각 앞뒤로 잘라주고,
# arr_front부터 맨 앞을 하나씩 번갈아서 새 배열인 result에 담고,
# 담으면 arr_front,back은 맨 앞을 동시에 계속 빼주기
for tc in range(1,T+1):
    N = int(input())
    arr = input().split()
    arr_front = []
    arr_back = []
    result = []

    if N % 2 == 0:
        arr_front = arr[:N//2]
        arr_back = arr[N//2:]
    else:
        arr_front = arr[:N//2 +1]
        arr_back = arr[N//2 +1:]

    for i in range(N//2 +1): # +1로 하고, 비어있으면 continue로 하자
        if len(arr_front) == 0: # N이 짝수인 경우, 여기도 넣어줘야 인덱스 에러 안뜸
            continue
        else:
            result.append(arr_front[0])
            arr_front = arr_front[1:]
        if len(arr_back) == 0:
            continue
        else:
            result.append(arr_back[0])
            arr_back = arr_back[1:]

    print(f'#{tc}', *result)