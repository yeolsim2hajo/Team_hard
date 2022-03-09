vect = ["M","I","N","C","O","D","I","N","G"]
# 찾을 문자 개수 n, 찾을 문자 str
n = int(input())
str = list(input().split())


# 입력받은 각 문자가 vect 배열에 있 는지 출력하라..  I N G -> OOO 로 출력
# DAT로 체크, DAT와 STR 비교..DAT value 값이 1이면...존재하는 것이므로 O을 출력하게 만들어봅시다..

# ord 함수 쓰기.. #알파벳의 아스키 코드는 대문자 65 ~ 90  소문자 97 ~ 122 dat의 크기는 123으로 설정
dat = [0] * 123
# 아스키 코드에 해당하는 인덱스 값에 1을 저장
for i in range(len(vect)):
    dat[ord(vect[i])] = 1


for j in range(len(str)):
    if dat[ord(str[j])] == 1:
        print("O", end='')
    else:
        print('X', end='')
