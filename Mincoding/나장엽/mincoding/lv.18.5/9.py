# 중복제거하기..
# 한 문장을 입력받고 , 중복 알파벳을 제거한 후 알파벳의 순서대로 출력..

#! 설계

# dat를 이용하면 될듯..
# dat의 value 값이 2 이상이면 1로 바꿔서 중복을 제거하자.
# 나머지 반복문을 통해서 출력하면 될듯.


str = list(input())

dat = [0]*123

for i in range(len(str)):
    dat[ord(str[i])] += 1


for k in range(len(dat)):
    if dat[k] >= 2:
        dat[k] = 1


for j in range(len(dat)):
    if dat[j] == 1:
        print(chr(j), end='')