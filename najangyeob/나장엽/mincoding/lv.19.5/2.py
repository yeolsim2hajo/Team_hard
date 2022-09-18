arr = [list(map(int, input().split())) for _ in range(5)]
# 입력받은 배열에 있는 숫자 1은 세포
# 세포 1주변에 아무것도 없으면 세포들이 안정된 상태
# 8 방향에 아무런 숫자가 없어야 함


#* 8방향을 설정하자
# 배열 중에서 1을 검사하고, 1이 있으면 그곳의 8방향을 검사하고, 주변에 1이 하나라도 있으면 불안정한 상태 출력
#왼위 위 오위 왼 오 왼아 아 오아
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
result = 1
for i in range(5):
    for k in range(4): 
        if arr[i][k] == 1:   # 만약에 arr에서 1을 찾으면 그때부터 그 주변을 탐색하기 시작!
            for j in range(8):
                ny = i + dy[j]
                nx = k + dx[j]
                if 0 <= ny < 5 and 0 <= nx < 4 :
                    if arr[ny][nx] == 1:
                        result = 0
                        break

if result !=  True:
    print('불안정한 상태')
else:
    print('안정된 상태')