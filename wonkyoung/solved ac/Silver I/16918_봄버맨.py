#230103
# 직접 돌리기
# R, C, N = map(int, input().split())
# total, bomb = set(), set()
# for i in range(R):
#     row = input()
#     for j in range(C):
#         total.add((i, j))
#         if row[j] == 'O':
#             bomb.add((i, j))
# second = 1
# now = set(bomb)
# while second < N:
#     now = set(total)
#     second += 1
#     if second < N:
#         now -= bomb
#         for y, x in bomb:
#             for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
#                 ny, nx = y+dy, x+dx
#                 now.discard((ny, nx))
#         second += 1
#         bomb = set(now)
#     else:
#         break
# for i in range(R):
#     for j in range(C):
#         if (i, j) in now:
#             print('O', end='')
#         else:
#             print('.', end='')
#     print()


# 규칙 - 17에서 틀림
'''
6 7 7
.......
...O...
....O..
.......
OO.....
OO.....
'''
R, C, N = map(int, input().split())
total, bomb = set(), set()
for i in range(R):
    row = input()
    for j in range(C):
        total.add((i, j))
        if row[j] == 'O':
            bomb.add((i, j))
if N%4 == 1 or N == 0:
    now = bomb
elif N%2 == 0:
    now = total
else:
    now = set(total)
    for y, x in bomb:
        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)):
            ny, nx = y+dy, x+dx
            now.discard((ny, nx))
for i in range(R):
    for j in range(C):
        if (i, j) in now:
            print('O', end='')
        else:
            print('.', end='')
    print()



