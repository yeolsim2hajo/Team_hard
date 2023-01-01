# point: 자음은 왼손 검지손가락으로, 모음은 오른손 검지손가락으로 입력
from sys import stdin

l, r = map(str, stdin.readline().rstrip().split())
string = stdin.readline().rstrip()

# keyboard 리스트를 1,2,3째줄 순서대로 생성하고, 모음을 따로 분리하여 모음 리스트를 생성
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
vowel = 'yuiophjklbnm'
# 손 위치의 좌표
xl, yl, xr, yr = 0,0,0,0

# l, r 좌표 찾아주기
for i in range(len(keyboard)):
    if l in keyboard[i]:
        xl, yl = i, keyboard[i].index(l)
    if r in keyboard[i]:
        xr, yr = i, keyboard[i].index(r)

ans = 0
for s in string:
    # 순회할 때 마다 문자를 누르는 시간을 고려해서 1+
    ans += 1
    # 입력하려는 문자 s 가 모음일 때, 오른손 좌표로부터 해당 문자까지의 거리를 계산하여 ans에 더해주기
    if s in vowel:
        for i in range(len(keyboard)):
            if s in keyboard[i]:
                nx = i
                ny = keyboard[i].index(s) # s찾기
                ans += abs(xr - nx) + abs(yr - ny)
                xr, yr = nx, ny
                break

    # 입력하려는 문자 s 가 자음일 때, 왼손 좌표로부터 해당 문자까지의 거리를 계산하여 ans에 더해주기
    else:
        for i in range(len(keyboard)):
            if s in keyboard[i]:
                nx = i
                ny = keyboard[i].index(s)
                ans += abs(xl - nx) + abs(yl - ny)
                xl, yl = nx, ny
                break

print(ans)