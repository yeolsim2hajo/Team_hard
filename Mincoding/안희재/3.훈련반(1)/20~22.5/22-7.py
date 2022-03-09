# 깊이는 3, card는 4개(브랜치도 4개, 패스도 4개)

word = list(input()) # list꼭 해야 path랑 비교 가능함
card = ['A', 'B', 'C', 'D']
path = [''] * 3

cnt = 0
def abc(level):
    global cnt
    if level == 3:
        cnt += 1
        if path == word:
            print(f'{cnt}번째')
        return

    for i in range(4):
        path[level] = card[i]
        abc(level+1)


abc(0)