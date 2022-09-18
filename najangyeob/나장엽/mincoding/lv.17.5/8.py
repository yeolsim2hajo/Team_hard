arr = [[3,55,42],[-5,-9,-10]]
pix = [list(map(int, input().split())) for _ in range(2)]


for i in range(2):
    for k in range(2):

        flag = 0
        for l in range(2):
            for m in range(3):
                if arr[l][m] == pix[i][k]:
                    flag = 1
                    break
        if flag == 1:
            print("Y", end = ' ')
        else:
            print("N", end = ' ')
    print()