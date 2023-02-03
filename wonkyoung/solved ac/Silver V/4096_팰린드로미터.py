#230203
# 전체 돌기
from sys import stdin
new_input = stdin.readline
while True:
    N = new_input().rstrip()
    if N == '0':
        break
    elif N == N[::-1]:
        print(0)
    else:
        to_next = {str(i): str(i+1) for i in range(9)}
        num = list(map(str, N))
        length = len(num)
        cnt = 0
        while True:
            cnt += 1
            for i in range(length-1, -1, -1):
                element = num[i]
                if to_next.get(element):
                    num[i] = to_next[element]
                    break
                else:
                    num[i] = '0'
            if num == num[::-1]:
                print(cnt)
                break




