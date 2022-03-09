arr = [list(input()) for _ in range(4)]

for i in range(3): # 세로로 3줄ㅇㅇ; # i = 0
    for j in range(3,0,-1): # j = 3,2,1
        for k in range(0,j): # k = (0,1,2), (0,1), (0)
            if arr[k][i] == '_':
                continue
            else:
                if arr[k+1][i] == '_':
                    arr[k][i], arr[k+1][i] = arr[k+1][i], arr[k][i]
                else:
                    continue

for i in range(4):
    print(''.join(arr[i]))

# -------------------------------------------
# 원경 코드
# 오우쉣;;;;;;;;;;; cnt 변수 만들어 줌으로써 포문 1개 아예 줄여버렸네
# cnt는 유효타인 경우를 의미함. '_'를 만나면, cnt는 그대로라서,
# 결국 아래처럼 하면 문자열이 뒤에서부터 차곡차곡 쌓일 수 있음
# 버블소트이긴 한데, 훨씬 간단한 버젼이네

# arr = [list(map(str, input())) for _ in range(4)]
# for j in range(3):
#     cnt = 0
#     for i in range(3,-1,-1):
#         if arr[i][j] != '_':
#             arr[3-cnt][j], arr[i][j] = arr[i][j], arr[3-cnt][j]
#             cnt += 1
# for i in range(4):
#     print(*arr[i],sep='')
# -------------------------------------------
