import sys
n,t = map(int, sys.stdin.readline().strip().split()) # 사람 수, 할당량
people = []
min_sum = 0
max_sum = 0

maxl = -1 
maxr = -1
res = 10**10 # 

for _ in range(n) :
    l,r = map(int, sys.stdin.readline().strip().split())
    people.append((l, r, r-l)) 

    min_sum += l 
    max_sum += r 

    if maxl < l : 
        maxl = l
    
    if maxr < r :
        maxr = r

# 불가능한 경우
if min_sum > t or max_sum < t :
    print(-1)
    exit(0) # 프로그램 종료 시키기

# 이분 탐색 범위 
l,r = maxl, maxr # 최소 주량 중 max, 최대 주량 중 max

# 이분 탐색

while l <= r : 
    s = (l + r) // 2 
    chk = t # 할당량
    more = 0 # 더 마실 수 있는 양

    for person in people : 
        pl, pr, pmore = person[0], person[1], person[2]  # l, r, r - l
        # 최소 주량, 최대 주량, more
        
        # 최소 주량부터 마시기
        chk -= pl # 남은 할당량

        more += min(s - person[0], person[2]) 
        # S의 최소값을 찾아야 함, 따라서 비교한다.
        # s - 최소 주량 vs 사람의 최대 주량 - 최소 주량 중 작은 범위
        # ex : (s가 7잔, 최소 주량이 3잔) vs (최대 8잔 최소 3잔) # 전자
        # ex : (s가 7잔, 최소 주량이 3잔) vs (최대 5잔 최소 3잔) # 후자

    if more >= chk : # more의 양이 현재까지 마시고 남은 술의 양보다 크거나 같으면 조건 만족 -> 남은 술을 더 마실 수 있는 사람에게 나눠주면, T에 정확히 맞출 수 있음.
        # 더 작은 s값이 있는지 check
        # r값을 줄인다
        if res > s : 
            res = s
        r = s - 1

    else : 
        l = s + 1

else : 
    print(res)
