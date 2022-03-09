map = [["A", "B"," K", "G"],["T", "T", "A", "B"],["A", "C", "C", "D"]]
#문자열로 입력 받은 것을 리스트로 변환.
pattern = [list(input()) for _ in range(2)]
print(pattern)

# def isPattern(index):
#     for i in range(6):

# 0,0 0,1 0,2 / 1,0 1,1 1,2 -> isPattern 에 보내기
# 2중 for문 pattern[i][j] vs map[i+y][j+x] 비교하기

def isPattern(by, bx):
    for dy in range(2):
        for dx in range(2):
            if map[by+dy][bx+dx] != pattern[dy][dx]:
                return 0
    return 1


cnt = 0

for y in range(2):
    for x in range(3):
        if 

# board = [
#     ["A", "B", "G", "K"],
#     ["T", "T", "A", "B"],
#     ["A", "C", "C", "D"]
# ]

# ptn = [list(input()) for _ in range(2)]

# def findptn(by, bx):  #0,0  0,1 0,2  1,0 1,1 1,2
#     for dy in range(2):
#         for dx in range(2):
#             if board[by+dy][bx+dx] != ptn[dy][dx]:
#                 return 0
#     return 1

# cnt = 0
# for y in range(2):
#     for x in range(3):
#         if findptn(y, x):   0,0 ~ 1,2
#             cnt += 1

# if not cnt:
#     print("미발견")
# else:
#     print("발견(%d개)"%cnt)