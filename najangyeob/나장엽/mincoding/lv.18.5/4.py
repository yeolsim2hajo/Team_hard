# 하마는 여러 충치를 가지고 있는데 이빨끼리 부딪친다~
# 충치끼리 닿으면 아파.
# 배열의 값끼리 더해서 2가 되면..부딪치는 것이니 2를 카운트해서 출력해보자


up = list(map(int, input().split()))
down = list(map(int, input().split()))

# up+down을 저장할 배열 선언
pain = [0]*5

# 배열의 값끼리 더하는 for문
for k in  range(5):
    pain[k] = up[k] + down[k]

# 부딪치는 이빨 갯수 카운트 할 변수
cnt = 0

for i in range(len(pain)):
    if pain[i] == 2:
        cnt += 1
    
print("{0}개".format(cnt))