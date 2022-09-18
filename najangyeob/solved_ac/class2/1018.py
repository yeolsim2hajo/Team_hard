#bwbw
#wbwb
# 8X8 사이즈보다 큰 경우
# b로 시작하는 경우, w로 시작하는 경우
# 구한 갯수를 answer 리스트에 넣은 후 min값 출력

N, M = map(int, input().split())
arr = []
answer = []
for i in range(N):
    a = input()
    arr.append(a)

for i in range(N-7):
    for k in range(M-7):
        count1 = 0
        count2 = 0
        for a in range(i, i+8):
            for b in range(k, k+8):
                if (a+b) % 2 == 0 :
                    if arr[a][b] != 'W': # w가 아닐때
                        count1 += 1 # w로 칠해주는 갯수 카운트
                    else:
                        count2 += 1 # b가 아니면 b로 칠해주는 개수
                else: 
                    if arr[a][b] != 'B': # b가 아닐때 
                        count1 += 1 # b로 칠해주는 개수
                    else: # w가 아니면 w로 칠해주는 개수
                        count2 += 1

        answer.append(count1)
        answer.append(count2)

print(min(answer))
