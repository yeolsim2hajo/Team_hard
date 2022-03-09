for tc in range(1,11):

    a = int(input())
    arr = []
    for i in range(100):
        str = input()
        arr.append(str)

    def find_palin(x):
        max = 0
        length = 0
        for k in range(0,len(arr)): #0행부터 7행까지 - 처음에 이중포문만 했었음. ㅠ 그러니 안되지
            for i in range(1,len(arr)+1): # i: 길이가 i인 회문 찾기
                for j in range(len(arr)+1-i):  # j: 길이가 i인 구간 탐색 횟수
                    data = x[k][j:j+i]
                    if data == data[::-1]:
                        length = i
                if max < length:
                    max = length
        return max

    # 세로로 재정렬
    arr_c = ['' for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr_c[i] += arr[j][i]

    print(f'#{a} {max(find_palin(arr),find_palin(arr_c))}')

# 회문 길이 가능 : 1부터 100까지 -> 가장 긴 회문 길이 탐색
    # 0. 한 줄에서 회문 max길이 찾기
    # 1. 가로로 쭉 찾고, max길이
    # 2. 세로로도 찾아서 max길이
    # 1,2 비교해서 높은거 pick
# 인덱스는 0~99
# 1인경우 100개(99index) 탐색, 2인경우 99개(98) 탐색 10인경우 91개 탐색

# 후기 : 내 코드 3중포문 -> 시행시간 3000ms임. 성주씨 코드가 300ms임ㅋㅋㅋㅋ
# 허허허