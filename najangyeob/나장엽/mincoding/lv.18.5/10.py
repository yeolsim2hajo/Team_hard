# 각 글자 수 세기
# 한 문장을 입력받고, 각 글자의 수를 출력하기...
# BTABATP
# A:2
# B:2
# P:1
# T:2


# DAT를 이용해서 누적시키기..
# DAT의 VALUE 값을 이용해서 출력하면 될듯...!


str = list(input())

dat=[0]*123

for i in range(len(str)):
    dat[ord(str[i])] += 1

for k in range(len(dat)):
    if dat[k] >= 1:
        print("{0}:{1}".format(chr(k), dat[k]))