arr = [["G","K","G"],["","",""]]
input = list(input().split())
arr[1] = input


# 같은 문자가 3개 이상 존재하는 지 검사하는 코드 
# 존재한다면 있음을 출력
# 없으면 없음 출력

#! solution
# dat, ord함수 를 이용해서 풀기

# dat 선언
# ord를 사용할것임. 대문자 입력받으므로 A(65) ~ Z(91) DAT 사용하려면 92길이의 DAT가 필요..
dat = [0]*92

for row in range(2):
    for col in range(3):
        dat[ord(arr[row][col])] += 1

result = 0
#if 조건 else: result = 0 하지말것 계속 초기화됨......!
for i in range(len(dat)):
    if dat[i] >= 3:
        result = 1
    


if result == 1:
    print("있음")
else:
    print("없음")