# 등산로 깍기 K
    # 0까지는 깍을 수 있음
    # 딱 "한" 곳을 정해서 깍을 수 있음
    # 지도에서 가장 높은 봉우리는 최대 5개

# 등산로는 무조건 높이가 오름차순이어야 함(중간에 크기순서 바뀐거 못 들어감)
    # 같아도 안됨.
N, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 제일 높은 봉우리좌표"들"의 찾기
Top = []
height = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > height:
            height = arr[i][j]

for i in range(N):
    for j in range(N):
        if arr[i][j] == height:
            Top.append((i,j))


