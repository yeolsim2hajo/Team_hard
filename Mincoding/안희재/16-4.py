T = [list(map(int,input().split())) for _ in range(2)]

new_lst = [0] * 4

for i in range(4):
    new_lst[i] = T[0][i] + T[1][3-i]

print(' '.join(map(str, new_lst)))