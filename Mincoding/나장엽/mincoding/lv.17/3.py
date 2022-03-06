# 숫자배열 선언
board = [[3,5,9], [4,2,1], [1,1,5]]

# 입력과 동시에 3x3 리스트를 선언
arr = [list(map(int, input().split())) for _ in range(3)]


# arr과 board의 index의 값이 같을때, arr에 1이 있다면 누적합을 구할까?

sum = 0
for col in range(3):
    for row in range(3):
        if arr[col][row] == 1:
            sum += board[col][row]
        else:
            sum = sum

print(sum)