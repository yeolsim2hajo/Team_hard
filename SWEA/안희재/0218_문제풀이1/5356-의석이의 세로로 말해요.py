# 각 단어 버켓에 넣기
# 제일 긴 단어의 길이 수 구하고, 그거만큼 1차 포문 돌리기
# 없으면, continue
    # 어 근데, 없으면? 이 조건을 어떻게 넣지? 존재하지 않는다?
    # 아니면, 모든 단어를 제일 긴 단어만큼 늘려야 하나? *같은걸로?
    # 에러? try,except? IndexError: string index out of range
    # 에러처리가 제일 깔끔한듯!
    # 아 근데, 이 방법 ㄴㄴ. 파이썬에서만 가능함 타 언어에서는 절대 ㄴㄴ;;;
    # 안 좋은 방법임

T = int(input())

for tc in range(1,T+1):

    arr = []
    for i in range(5): # 5줄만 입력이니까
        word = input()
        arr.append(word)

    max_len = 0 
    for i in range(len(arr)): # 5단어중에서, 가장 긴 단어 길이 구하기
        if max_len < len(arr[i]):
            max_len = len(arr[i])

    result = ''
    for i in range(max_len): # i는 각 요소(단어)의 인덱스
        for j in range(5): # 제일 긴 단어만큼 반복문 돌려야 빠짐없이 추가 가능
            try:
                result += arr[j][i]
            except: #try-except문으로 인덱스초과하는 경우 넘겼음
                continue

    print(f'#{tc}', result)
