arr = [['_','_','_'], ['_','_','_'], ['A','T','K'], ['_','_','_'], ['_','_','_'] ]

A_x, A_y = 2, 0
T_x, T_y = 2, 1
K_x, K_y = 2, 2


for i in range(7):
    order = input().split()

    if order[0] == 'A':
        if order[1] == 'UP':
            A_x -= 1
        elif order[1] == 'DOWN':
            A_x += 1
        elif order[1] == 'RIGHT':
            A_y += 1
        else:
            A_y -= 1
    elif order[0] == 'T':
        if order[1] == 'UP':
            T_x -= 1
        elif order[1] == 'DOWN':
            T_x += 1
        elif order[1] == 'RIGHT':
            T_y += 1
        else:
            T_y -= 1
    else:
        if order[1] == 'UP':
            K_x -= 1
        elif order[1] == 'DOWN':
            K_x += 1
        elif order[1] == 'RIGHT':
            K_y += 1
        else:
            K_y -= 1

result = [['_'] * 3 for i in range(5)]

result[A_x][A_y] = 'A'
result[T_x][T_y] = 'T'
result[K_x][K_y] = 'K'

for i in range(5):
    print(''.join(result[i]))