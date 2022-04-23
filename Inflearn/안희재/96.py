def solution(field):
    width = len(field[0])
    height = len(field)
    Sum = [[0] * width for i in range(len(field))]
    for i in range(0, height):
        for j in range(0, width):
            if field[i][j] == 0:
                Sum[i][j] = 1
            else:
                Sum[i][j] = 0
    
    for i in range(1, height):
        for j in range(1, width):
            if Sum[i][j] == 1:
                Sum[i][j] = min(Sum[i-1][j-1], min(Sum[i-1][j], Sum[i][j-1])) + 1

    maxValue = 0
    x = 0
    y = 0
    for i in range(0, height):
        for j in range(0, width):
            if maxValue < Sum[i][j]:
                maxValue = Sum[i][j]
                x = i
                y = j
                
    print(maxValue, x, y)
    print(maxValue, 'X', maxValue)
    
    for i in range(x - (maxValue - 1), x + 1):
        for j in range(y - (maxValue - 1), y + 1):
            field[i][j] = '#'

    return field
    
solution(input())