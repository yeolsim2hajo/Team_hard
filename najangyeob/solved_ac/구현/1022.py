r1,c1,r2,c2 = list(map(int,input().split()))
pad = max(abs(r1),abs(c1),abs(r2),abs(c2))
r1 += pad; c1 += pad; r2 += pad; c2 += pad;

## pad,pad 부터 소용돌이 시작
x,y = pad,pad
cnt = 1
ans = [[0 for i in range(c2-c1+1)] for i in range(r2 - r1 + 1)]
if r1 <= x <= r2 and c1 <= y <= c2:
    ans[x-r1][y-c1] = cnt

dx = [-1,0,1,0] ## 위 오른쪽 아래 왼쪽
dy = [0,1,0,-1]
for k in range(1,pad+1):
    for t in [1,0,3,2,1]:
        while pad - k <= x + dx[t] <= pad + k and pad - k <= y + dy[t] <= pad + k:
            x = x + dx[t]
            y = y + dy[t]
            cnt += 1
            if r1 <= x <= r2 and c1 <= y <= c2:
                ans[x-r1][y-c1] = cnt

m = 0
for i in range(len(ans)):
    for j in range(len(ans[0])):
        m = max(m,ans[i][j])
mstr = str(m)
length = len(mstr)

for i in range(len(ans)):
    for j in range(len(ans[0])):
        tmp = str(ans[i][j])
        print(tmp.rjust(length," "), end = ' ')
    print()