# 회문이어도 길이가 M이 아니면 xx
# ㅆㅂ 세로로도 찾아진다네..
# 가로찾기, 세로찾기 나눠야 할듯
# 아니, N= 20, M= 13인 경우, 그러면 각 줄마다 구간탐색 돌려서 회문 찾으라는거?
# ㅇㅇ ㅅㅂ ㅋㅋ
# 아니 한다면 하는데, 세로찾기가 더 에바인것 같은데 간단한 방법 없나?
    # 아 그냥 가로에서는 arr[i][j]했다면, 여기선 arr[j][i]하면 될듯?
    # arr_c = [[0] * N for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         arr_c[i][j] = arr_r[j][i] -> 요로코롬

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())

    arr_r = []
    for i in range(N):
        str = list(input())
        arr_r.append(str)

    # 가로 찾기
    for i in range(N):
        for j in range(N-M+1):
            if arr_r[i][j:j+M] == arr_r[i][j:j+M][::-1]:
                answer_r = ''.join(arr_r[i][j:j+M])
                print(f'#{tc} {answer_r}')

    # 세로 정렬 배열 새로 만들고, 그대로 찾기
    arr_c = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_c[i][j] = arr_r[j][i]

    for i in range(N):
        for j in range(N-M+1):
            if arr_c[i][j:j+M] == arr_c[i][j:j+M][::-1]:
                answer_c = ''.join(arr_c[i][j:j+M])
                print(f'#{tc} {answer_c}')

# 페어 코드 - 이게 제일 나은듯. 어우 개좋다 이 방식
# 또한, tmp변수 만들어서 가독성도 훨씬 높였네 ㅇㅇ
# 특히, 나 세로전환 하는 방법 헷갈려서, 처음 str넣을때 list로 input했는데(처음부터 arr_r은 이중 리스트 만들어짐..)
# 여기선 vboard[i] += board[j][i]로 바로 만들어버렸네
# ----------------------------------------------------
# T = int(input())

# def check(board):
#     for i in range(N):
#         for j in range(N-M+1):
#             tmp = board[i][j:j+M]
#             if tmp == tmp[::-1]:
#                 print(f'#{tc+1} {tmp}')
#                 return 1 # 캬; 

# for tc in range(T):
#     N,M = map(int,input().split())
#     board = [input() for _ in range(N)]

#     if check(board): continue
        # 와 여기 2가지 원리 들어가있네, 실행시키면서 동시에 없을 경우 세로찾기 조건도 추가해주는 식(애초에 함수를 잘 짬)
#     else:
#         vboard = ['' for _ in range(N)]
#         for i in range(N):
#             for j in range(N):
#                 vboard[i] += board[j][i]
#         check(vboard)
# ----------------------------------------------------