# 체스판의 크기는 8 by 8 가장 위쪽 칸(0,0)은 하얀색
# 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성해라
# 하얀색은 0 2 4 6 
# % 연산자로 체크.
# 
arr = []

for _ in range(8):
    arr.append(list(input()))

cnt = 0
for i in range(8):
    for k in range(8):
        if (i + k)  % 2 == 0:
            if arr[i][k] == 'F':
                cnt += 1


print(cnt)