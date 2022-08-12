# 예전에 풀어봤던 문제(레퍼런스 코드 참조했었던)
n = int(input())

arr = []
for _ in range(n):
    line = list(map(str, input()))
    arr.append(line)

answer = 1 # max값으로 계속 갱신시켜줄 예정

# 1. 가로로 체크했을 때, 같은 색의 사탕이 최대 몇개인지 확인해주는 함수
def width_check():
    global  answer
    for i in range(n):
        tmp = 1 # 반복문마다, 1로 초기화

        for j in range(n-1):
            if arr[i][j] == arr[i][j + 1]: # 바로 오른쪽과 색이 같다면, +1
                tmp += 1
                answer = max(answer,tmp) # 최대 기록을 계속 갱신
            else: # 색이 다르면, 1로 초기화해서 다시 시작
                tmp = 1

# 2. 세로로 체크
def vertical_check():
    for i in range(n):
        global answer
        tmp = 1
        for j in range(n-1):
            if arr[j][i] == arr[j + 1][i]:
                tmp += 1
                answer = max(answer,tmp) 
            else: 
                tmp = 1

# 3. 인접 행렬을 교환하는 모든 경우의 수를 이중반복문을 통해 체크
    # 단, 인접한 색이 같으면 굳이 교환하는 의미가 없으므로 패스 -> 처음에 이 경우 생각 못했었음
    # 그로 인해 만들어지는 새 배열에서, 가로/세로 체크해서 최대 값 갱신
    # 원상복구 필수
for i in range(n):
    for j in range(n-1):
        # 바로 오른쪽의 색이 다르다면 체크
        if arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            width_check()
            vertical_check()
            arr[i][j + 1], arr[i][j] = arr[i][j], arr[i][j + 1] # 원상복구
        # 바로 아래쪽의 색이 다르다면 체크
        if arr[j][i] != arr[j + 1][i]:
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
            width_check()
            vertical_check()
            arr[j + 1][i], arr[j][i] = arr[j][i], arr[j + 1][i] # 원상복구

print(answer)