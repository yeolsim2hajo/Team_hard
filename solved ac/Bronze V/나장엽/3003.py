find_pieces = list(map(int, input().split(" ")))
origin = [1, 1, 2, 2, 2, 8]

for i in range(0, len(origin)) :
    print(origin[i]-find_pieces[i], end=' ')
