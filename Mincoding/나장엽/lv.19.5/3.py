input = list(map(int, input().split()))

# 1 ~ 16 
# input값과 배열의 값을 비교해서 같으면... 
# 이차원 dat는 불가능한건가..?
# 간단하게...순서대로니까 print를 이용해버리자..

dat = [0]*16

for i in range(len(input)):
    dat[input[i]-1] = i+1

for k in range(0, 16, 4):
    print(*dat[k:k+4])