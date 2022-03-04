direct = [list(input().split()) for _ in range(7)]
# [['A', 'UP'], ['T', 'DOWN'], ['K', 'UP'], ['A', 'RIGHT'], ['K', 'UP'], ['K', 'LEFT'], ['A', 'LEFT']]

model = []
move = []
# 추출해서 처리해버리자
for i in range(7):
    if len(direct[i][0]) == 1:
        temp1 = direct[i][0]
        model.append(temp1)
        temp2 = direct[i][1]
        move.append(temp2)
#['A', 'T', 'K', 'A', 'K', 'K']
#[ 'UP', 'DOWN', 'UP', 'RIGHT', 'UP', 'LEFT']

#현재 위치 선언
y_a = 2
x_a = 0

y_t = 2
x_t = 1

y_k = 2
x_k = 2

# 위치 바꾸기

for i in range(7):
    if model[i] == 'A':
        if move[i] == 'UP':
            y_a -= 1
        elif move[i] =='DOWN':
            y_a += 1
        elif move[i] == 'RIGHT':
            x_a += 1
        else:
            x_a -= 1
        
    if model[i] == 'T':
        if move[i] == 'UP':
            y_t -= 1
        elif move[i] =='DOWN':
            y_t += 1
        elif move[i] == 'RIGHT':
            x_t += 1
        else:
            x_t -= 1
            
    if model[i] == 'K':
        if move[i] == 'UP':
            y_k -= 1
        elif move[i] =='DOWN':
            y_k += 1
        elif move[i] == 'RIGHT':
            x_k += 1
        else:
            x_k -= 1
            
# print할 배열 선언
result = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

result[y_a][x_a] = 'A'
result[y_t][x_t] = 'T'
result[y_k][x_k] = 'K'

for i in range(5):
    for k in range(3):
        print(result[i][k], end='')
    print()