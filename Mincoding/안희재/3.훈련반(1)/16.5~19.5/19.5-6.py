board = [
    ["A", "B", "G", "K"],
    ["T", "T", "A", "B"],
    ["A", "C", "C", "D"]
]

ptn = [list(input()) for _ in range(2)]

def findptn(by, bx):
    for dy in range(2):
        for dx in range(2):
            if board[by+dy][bx+dx] != ptn[dy][dx]:
                return 0
    return 1 # return 1 위치 여기임 여기 / 다 끝나고, 4개 다 체크해보고 안나오면 마침내 1인것

cnt = 0
for y in range(2):
    for x in range(3):
        if findptn(y,x):
            cnt += 1

if not cnt:
    print("미발견")
else:
    print("발견(%d개)"%cnt)