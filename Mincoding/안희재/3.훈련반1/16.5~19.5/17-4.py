arr = [['A','T','K','B'], ['C','Z','F','D'], ['H','G','E','I']]

# 1. T 위치 찾고, y,x축 값 플러스해서 다시 그 위치를 arr에서 찾으면 됨

str, y, x = input().split()
y, x = int(y), int(x)

position_1, position_2 = 0, 0
for i in range(3):
    for j in range(4):
        if str == arr[i][j]:
            position_1, position_2 = i, j

position_1 += y
position_2 += x

print(arr[position_1][position_2])