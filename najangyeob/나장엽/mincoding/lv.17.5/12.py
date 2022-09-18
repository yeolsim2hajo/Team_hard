arr = [["A","B","C","D","E"],["F","G","H","I","J"],["K","L","M","N","O"],["P","Q","R","S","T"],["U","V","W","X","Y"]]
alpha = input()


# 입력받은 문자의 좌표값 구하고... 기준이 되는 m의 좌표값을 빼면될려나..
# for문을 돌려서 좌표값을 x,y에 저장하고... 출력할때 빼볼까..

x = 0
y = 0
for row in range(5):
    for col in range(5):
        if arr[row][col] == alpha:
            x, y = row, col



print("{0},{1}".format((x-2), (y-2)))
