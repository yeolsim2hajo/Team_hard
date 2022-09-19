#99 토끼들의 행진
# rock = list(map(int,input().split()))
# jump = list(map(int,input().split()))
# length = len(jump)
# okay = ['통과']*length
# for i in range(length):
#     for j in range(0,len(rock),jump[i]):
#         if rock[j]:
#             rock[j] -= 1
#         else:
#             okay[i] = '통과 못함'
#     print(okay[i],end=' ')

#100 퍼즐 게임
def score():
    N,M = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    order = list(map(int,input().split()))
    score = 0
    result = []
    for i in order:
        for j in range(N):
            if puzzle[j][i-1]:
                result.append(puzzle[j][i-1])
                puzzle[j][i-1] = 0
                break
        else:
            score -= 1
    idx = 0
    while idx < len(result):
        if result[idx-1] == result[idx]:
            score += result[idx] * 2
            idx += 1
        idx += 1
    print(score)

score()

'''
5 4
0 0 0 0
0 1 0 3
2 5 0 1
2 4 4 1
5 1 1 1
1 1 1 1 3 3 3
'''
