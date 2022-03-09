# Ladder
import sys
sys.stdin = open("input (5).txt","r")

for _ in range(1,11):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    x = y = 0
    while ladder[y][x] != 2:
        print(y,x)
        if ladder[y][x]:
            print(y,x)
            if y == 99:
                x += 1
                y = 0
            elif ladder[y][x+1] == 1:
                x += 1
                if ladder[y+1][x+1]== 1:
                    x -= 1
                    y += 1
            elif x > 0 and ladder[y][x-1] == 1:
                x -= 1
                if ladder[y+1][x+1]== 1:
                    x += 1
                    y += 1
            elif ladder[y+1][x]:
                y += 1
        else:
            x += 1
            y = 0

    print('#{} {}'.format(tc,x))

# 백만 장자 프로젝트
import sys
sys.stdin = open('input(7).txt','r')

T = int(input())
for tc in range(1,11):
    n = int(input())
    price = list(map(int, input().split()))
    sell = buy = max_val = 0
    for i in range(1,n): # 끝값
        sell = price[i]
        buy = 0
        cnt = 0
        for j in range(i):
            if price[j] < price[i]:
                buy += price[j]
                cnt += 1
                profit = sell*cnt - buy
            if max_val < profit:
                max_val = profit
    print('#{} {}'.format(tc, max_val))


    # for i in range(n):
    #     if start == end:
    #         end += 1
    #         profit = price[end] - price[start]
    #     if profit > max_val:
    #         max_val = profit

