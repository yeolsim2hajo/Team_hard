T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    # 굳이 int안해줘도 될듯

    # 어 그냥, 90도 돌려주는 함수 만들어서, 총 3번 실행해주면 되는거 아님?
    # 90도 : 세로정렬시킨 후에, 각 행 각각 거꾸로 -> 세로 정렬도 필요없음
    def angle90(array):
        result = [''] * N
        for i in range(N):
            for j in range(N):
                result[i] += array[N-1-j][i]
        
        return result

    arr_90 = angle90(arr)
    arr_180 = angle90(arr_90)
    arr_270 = angle90(arr_180)

    print(f'#{tc}')
    for i in range(N):
        print(arr_90[i], arr_180[i], arr_270[i])