# 서준 코드 : 실행시간은 큰 차이 없으나, 코드가 훨씬 깔끔
# --------------------------
def Ladder(arr):
    arr=arr[::-1]
    for j in range(100):
        if arr[0][j]==2:
            break # 이렇게 하기만 해도 2인 인덱스값이 j에 담기는구나 ㄷㄷ;;
    for i in range(1,100):
        if j!=0 and arr[i][j-1]==1: # j가 0이면, 왼쪽 끝이고, j-1는 범위 벗어나므로
            while j!=0 and arr[i][j-1]==1:
                j-=1
        elif j!=99 and arr[i][j+1]==1:
            while j!=99 and arr[i][j+1]==1:
                j+=1
    return j
    # 와 생각해보면, x좌표는 굳이 나처럼 표현할 필요가 없기도 했네. 위처럼 그냥 100행 포문 돌리면

TC=10
for _ in range(10):
    t=int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]
    print(f'#{t} {Ladder(arr)}')
# --------------------------------------------------------------------