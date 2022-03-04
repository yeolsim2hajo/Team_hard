arr = list(map(int, input().split()))

# 같은 숫자가 존재하는 지 확인?
# dat 가 2 이상이면 같은 존재가 있는 것임
# dat 를 이용해서 풀어보자.


dat = [0]*7

for k in range(len(arr)):
    dat[arr[k]] += 1

result = 0
for i in range(len(dat)):
    if dat[i] >= 2:
        result = 1

if result :
    print("도플갱어 발견")
else:
    print("미발견")