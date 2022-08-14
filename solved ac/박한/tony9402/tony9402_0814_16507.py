# 백준 16507 어두운 건 무서워
# 108892KB / 3756ms

import sys
input = sys.stdin.readline
r, c, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
arr1 = [[0]*(c+1) for _ in range(r)]
for i in range(r):
    arr1[i][1] = arr[i][0]
    for j in range(2, c+1):
        arr1[i][j] = arr[i][j-1] + arr1[i][j-1]
def abc(y1, x1, y2, x2):
    rst, num = 0, (y2-y1+1)*(x2-x1+1)
    for i in range(y1-1, y2):
        rst += (arr1[i][x2]-arr1[i][x1-1])
    print(rst//num)
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    abc(r1, c1, r2, c2)

# 아무 생각없이 했다가 75% 정도에서 시간초과 나서 다시 풀어봄
# 정답용(?) 배열을 만들어서 그걸 계속 갖다 쓰는 식으로!
# 한 번 만드는데도 오래 걸려서 시간이 많이 걸렸음