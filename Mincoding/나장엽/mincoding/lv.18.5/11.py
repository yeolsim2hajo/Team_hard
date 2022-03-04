# 유령은 존재할까?

# 한 문장을 입력받고, 문장에 GHOST 단어가 존재하는지 찾아서 출력
# 패턴을 찾는 문제..!


str = list(input())
target = list("GHOST")

for i in range(3):
    flag = 0
    for j in range(0, 5, 1):
        if target[j] != str[i+j]:
            flag = 1
            break
    if flag == 0:
        break

if flag == 1:
    print("존재하지 않음")
else: 
    print("존재")