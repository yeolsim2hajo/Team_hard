# 실행시간 내꺼의 1/10 ㄷ;
# 코드길이는 좀 더 길지만,

# 크게는 2가지이고, 각각 2가지로 또 세분화
# 가로 탐색 - 회문길이가 짝,홀인 경우
# 세로 탐색 - 회문길이가 짝,홀인 경우
# 세로 정렬하는 방법 간단하네.. 저렇게 하면 되는구나, x<y인 조건주고
    # 어차피, 대각선들은 그대로고, 대각위를 대각 아래로 한번만 바꿔주면 되니까 x<y임

# -----------------------------------------------
T = 10

for tc in range(1,T+1):
    max = 0
    arr = []
    N = input()
    for i in range(100):
        arr.append(list(input()))
    for y in range(100):
        for x in range(100):
            p = 0
            count= -1
            while(True):
                if(0 <= x-p) and (x+p <= 99):
                    if (arr[y][x - p] == arr[y][x + p]):
                        count +=2
                        p += 1
                    else:
                        break
                else:
                    break
            if(count > max):
                max = count
                # print(y,x,max,'-1')
    for y in range(100):
        for x in range(100):
            p = 0
            count= 0
            while(True):
                if(0 <= x-p) and (x+p+1 <= 99):
                    if (arr[y][x - p] == arr[y][x +1 + p]):
                        count +=2
                        p += 1
                    else:
                        break
                else:
                    break
            if(count > max):
                max = count
                # print(y, x, max,'-2')

    for y in range(100): # 세로 정렬
        for x in range(100):
            if (x<y):
                arr[y][x],arr[x][y] = arr[x][y],arr[y][x]

    for y in range(100):
        for x in range(100):
            p = 0
            count= -1
            while(True):
                if(0 <= x-p) and (x+p <= 99):
                    if (arr[y][x - p] == arr[y][x + p]):
                        count +=2
                        p += 1
                    else:
                        break
                else:
                    break
            if(count > max):
                max = count
                # print(y, x, max,'-3')

    for y in range(100):
        for x in range(100):
            p = 0
            count= 0
            while(True):
                if(0 <= x-p) and (x+p+1 <= 99):
                    if (arr[y][x - p] == arr[y][x +1 + p]):
                        count +=2
                        p += 1
                    else:
                        break
                else:
                    break
            if(count > max):
                max = count
                # print(y, x, max,'-4')
    print(f'#{tc} {max}')
# -----------------------------------------------