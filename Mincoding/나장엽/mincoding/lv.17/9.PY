vect = [[3,7,4],[2,2,4],[2,2,5]]
target = list(map(int, input().split()))

# vect를 순회하면서 target값과 일치하면 cnt를 증가?
# 입력값이 2 3 4 이면 target[0] 일때 vect[0][0~2] : cnt = 0 ->  target[0] 일때 vect[1][0~2] : cnt 2 / target[0]일때 vect[2][0~2] cnt 4
# result1, 2, 3 가 필요한가?

result = [0,0,0]

for i in range(3):
    for j in range(3):
        if vect[i][j] == target[0]:
            result[0] += 1
        elif vect[i][j] == target[1]:
            result[1] += 1
        elif vect[i][j] == target[2]:
            result[2] += 1
            
# max 값에 해당하는 숫자 출력...
# max 값 초기화
max = result[0]

for k in range(len(result)):
    if result[k] > max:
        max = result[k]
    else:
        max = max

for m in range(3):
    if max == result[m]:
        print(target[m])