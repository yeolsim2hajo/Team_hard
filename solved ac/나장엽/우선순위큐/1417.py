import sys
input = sys.stdin.readline

n = int(input())
candidate = []
for _ in range(n):
    candidate.append(int(input()))


cnt = 0 # 매수자 
# 다솜이가 최대 득표자이고, 최대득표자가 자기 자신만 있을 때 
if max(candidate) == candidate[0] and candidate.count(max(candidate)) == 1:
    print(0)
else:
    while True:
        max_candi = -99829323
        max_candi_idx = 0

        for i in range(1, n):
            if candidate[i] > max_candi:
                max_candi = candidate[i]
                max_candi_idx = i
            
        # 최대 득표자와 다솜이 비교하여 크면 최대득표자의 표 -1 다솜 표 +1, 매수자 1 증가
        if max_candi >= candidate[0]:
            candidate[max_candi_idx] -= 1 
            candidate[0] += 1
            cnt += 1
        # 최대득표자가 1명이고 그 최대득표자가 다솜이면 매수자 출력 후 종료
        if candidate.count(max(candidate)) == 1 and max(candidate) == candidate[0]:
            print(cnt)
            break
