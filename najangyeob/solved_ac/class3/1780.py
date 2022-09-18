
def divide(start_row, start_col, size):
    global paper, minus, one, zero
    flag = True
    num = paper[start_row][start_col]

    # 종이의 모든 숫자가 같으면 TRUE, 아니면 FALSE
    for row in range(start_row, start_row + size):
        for col in range(start_col, start_col + size):
            if num != paper[row][col]: # 숫자가 다르면 false -> break 
                flag = False 
                break
        

        if not flag : # flag가 false면(모든 종이의 숫자가 다르면!) true -> break for문 탈출
            break

    #  처음부터 모든 종이의 숫자가 같다면, 그냥 count.
    if flag : 

        if num == -1:
            minus += 1

        elif num == 0:
            zero += 1

        else:
            one += 1
    # 아니라면 9분할로 분할 후  다시 체크 
    else:
        size //= 3
        divide(start_row, start_col, size) # 1분면 
        divide(start_row + size, start_col, size) # 2분면 
        divide(start_row, start_col+size, size) # 3분면 
        divide(start_row + size, start_col + size, size) # 4분면 
        divide(start_row, start_col + size * 2, size) # 5분면
        divide(start_row + size * 2, start_col, size) # 6분면
        divide(start_row + size, start_col + size * 2, size) # 7분면
        divide(start_row + size * 2, start_col + size, size) # 8분면
        divide(start_row + size * 2, start_col + size * 2, size) # 9분면



import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

minus = 0
one = 0
zero = 0

divide(0, 0, N) # (0, 0) 부터 시작
print(minus)
print(zero)
print(one)



