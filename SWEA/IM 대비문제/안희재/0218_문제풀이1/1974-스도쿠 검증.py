# 0. 입력받은 값 이중배열에 넣기
# 1. 가로 9줄 검사
# 2. 세로 9줄 검사
# 3. 3*3격자판 총 9개 검사
    # - 격자판전용 함수 만들어야 하나 흠;;
# 4. 검사원칙 : 합이 45여야 함 sum(1~9)
# 근데, 애초에 이렇게 까지 길어질.. 그런 문제인가?
    # 더 간단한 원리 없을까?
def grating(x,y): # 격자판 검사
    sum = 0
    for i in range(3):
        for j in range(3):
            sum += arr[x+i][y+j]
    if sum != 45:
        return False

def sudoku():
    answer = 1 # 1은 스도쿠 성공, 0은 실패
    # 가로검사 
    for i in range(9):
        if sum(arr[i]) != 45: # 1부터9까지의 합은 45
            answer = 0

    # 세로검사
    for i in range(9):
        c_sum = 0 # 세로 1줄 돌릴때마다, c_sum 초기화시켜서 계속 검사
        for j in range(9):
            c_sum += arr[j][i]
        if c_sum != 45:
            answer = 0

    # 격자판 검사
    for i in range(0,7,3): # 0,3,6
        for j in range(0,7,3): # 0,3,6
            if grating(i,j) == False:
                answer = 0
    
    return answer

T = int(input())

for tc in range(1,T+1):
    arr = []
    for i in range(9):
        line = list(map(int,input().split()))
        arr.append(line)

    print(f'#{tc}', sudoku())
