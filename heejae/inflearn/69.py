# 먼저 소수 구하는 함수 -> 입력받은 수에서 1씩 빼면서 소수인지 확인
# 소수인 가장 큰 수가 나오면, n에서 그 수를 빼보고, 그 결과값도 소수면 return!

# ㄴㄴ 에라토스테네스의 체 이용해서 2
n = int(input())
answer = [] # n까지의 소수 모음 -> 이제 여기서 2개 선택해서 더 한 후, n이 되면 그거 출력
check = [0] * (n+1)

for i in range(2,n+1):
    if check[i] == 0: answer.append(i)
    for j in range(i+i,n+1,i):
        check[j] = 1

x, y = 0, 0
for i in range(len(answer)-1): # 중복조합
    for j in range(i,len(answer)):
        if answer[i] + answer[j] == n:
            print(answer[i],answer[j])



