input = [list(map(int, input().split())) for _ in range(4)]

vect = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]

# vect 배열에서 input 배열에 든 좌표에 해당하는 곳을 찾아 5를 넣어라!!!!!!!!!!
# input[0][0] = 0 input[0][1] = 1
# input[1][0] = 1 input[1][1] = 0
# input[2][0] = 3 input[2][1] = 0
# input[3][0] = 3 input[3][1] = 1

# vect[input[0][0]][input[0][1]] = 5
# vect[input[1][0]][input[1][1]] = 5
# vect[input[2][0]][input[2][1]] = 5
# vect[input[3][0]][input[3][1]] = 5
# 이렇게 하면 될거같은데...

for i in range(4):
    vect[input[i][0]][input[i][1]] = 5

for k in range(4):
    for c in range(3):
        print(vect[k][c], end= ' ')
    print()