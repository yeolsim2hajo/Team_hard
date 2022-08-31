# 풀이
# 가격 하나를 선택해서 그 가격보다 크거나 같은 가격을 카운트하기
# 카운트가 N보다 크면 안됨.
N, M = map(int, input().split())
price = []
for _ in range(M):
    price.append(int(input()))
        
Max = -1231312313123 # 초기화
for i in range(M): # 가격 선택
    cnt = 0
    for k in range(M): #선택한 가격에 대해 비교
        if price[i] <= price[k]: # 선택 가격보다 크거나 같으면 ++
            cnt += 1

    if cnt > N: 
        continue # 판매한 달걀이 달걀보다 많아지면 cut
    
    profit = cnt * price[i] # 수익 계산
    Max = max(Max, profit) # 최대값 갱신
    if Max == profit: 
        pick_price = price[i]

print(pick_price, Max)