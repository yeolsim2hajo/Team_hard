
def R_move(array):
    tmp = array[-1]
    for i in range(4,0,-1):
        array[i] = array[i-1]
    array[0] = tmp

def L_move(array):
    tmp = array[0]
    for i in range(4):
        array[i] = array[i+1]
    array[-1] = tmp

arr = [3,5,1,9,7]
for i in range(4):
    direction = input()
    if direction == 'R':
        R_move(arr)
    else:
        L_move(arr)

print(*arr)