def create_arr(n,m,character, wall, arr):

    # 외벽 세우기
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i==0 or j==len(arr[0])-1 or j==0 or i ==len(arr)-1:
                arr[i][j]=2

    # 캐릭터의 위치 1로 설정
    arr[character[0]+1][character[1]+1] = 1

    # 장애물의 위치 2로 설정
    for i in wall:   
        arr[i[0]+1][i[1]+1] = 2 

    # 지형 출력하기
    for i in arr:
        print(i)

n=4
m=5
characher = [0,0]
wall=[[0,1],[1,1],[2,3],[1,3]]
moving = [2,2,2,4,4,4]
arr = [[0]*(n+2) for i in range(m+2)]
create_arr(n,m,characher,wall, arr)
