# max값 구하면, 처음부터 그곳 전까지 쭈욱 사고, max에서 팔기
# 그 다음 max구하기 -> 처음 max이후부터 그 다음 max이전까지 더하기 => 반복
# 언제까지? 시작인덱스가 배열 길이되기 직전까지
# 나는 처음에, 너무 복잡하게 생각했구나. 전체원리는 간단한데..
# 너무 미시적으로 파고들었음

def Profit(lst):
    sum = 0
    cnt = 0
    Max = max(lst)
    for i in range(len(lst)):
        if lst[i] != Max:
            sum -= lst[i]
            cnt += 1
        else: # Max점 도달했으면
            sum += cnt * Max
            cnt = 0
            if i+1 == len(lst):
                break
            else:
                Max = max(lst[i+1:len(lst)])

    return sum

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    prices = list(map(int,input().split()))
    print(f'#{tc}', Profit(prices))

