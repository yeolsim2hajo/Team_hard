# 성의 첫 글자가 같은 선수 5명을 선발
# 성의 첫 글자가 같은 선수가 5명보다 적다면, 기권
# 내일 경기를 위해 뽑을 수 있는 성의 첫글자를 모두 구하려고 한다


# dat 사용?

n = int(input())

dat = [0]*200
name = []
for _ in range(n):
    name.append(input())

for i in range(len(name)):
    dat[ord(name[i][0])] += 1

flag = False
for i in range(len(dat)):
    if dat[i] >= 5:
        flag = True
        print(chr(i), end = '')
    
if flag == False:
    print('PREDAJA')