# 아래 코드 마지막 히든 케이스가 시간 초과로 통과 못함
# max 구하는 포문 밖으로 빼서 1중포문 해야 하나..
# 이 논리에 의하면, 이중포문이 만들어질 수 밖에 없다.
# 다시 짜기..
# -----------------------------------------------------
def Profit(lst):
    sum = 0
    cnt = 0
    for i in range(len(lst)-1): # 길이 일단 이렇게 둬보자
        if lst[i] < lst[i+1]: # 일단 사고봐야지
            sum -= lst[i]
            cnt += 1 # 재고 개수
            if i == len(lst)-2:
                sum += lst[i+1] * cnt
        else: # 직후의 가격이 더 싸다면?, 이후에 더 비싼점 없으면 sell
            max = lst[i]
            for j in range(i+2,len(lst)):
                if lst[j] > max:
                    max = lst[j]
            if lst[i] < max: # 이후에 더 비싼 지점이 있다면, 너도 사
                sum -= lst[i]
                cnt += 1
            elif lst[i] == max: # 만약, 여기가 최고점이라면 다 팔아
                sum += lst[i] * cnt
                cnt = 0
    return sum

T = int(input())
for tc in range(1,T+1):
    
    N = int(input())
    prices = list(map(int,input().split()))
    print(f'#{tc}', Profit(prices))
# -------------------------------------------------------

# 1. 1번인덱스부터 끝까지 순회
# 2. 각, 구간에서 선택해야 할 것
    # - 사자
        # - 만약, 그 후에 더 비싼 가격이 없다면 사지 말아야 함
        # - 매매지점
    # - 팔자
        # - 그 뒤에 더 비싼 가격이 있다면 팔지 말아야 함
        # - 존버지점
