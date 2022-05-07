S = list(input())
check = [-1]*26 #알파벳의 위치 -1로 초기화(포함되지 않은 경우)

alpha = [] # 소문자 알파벳 아스키 코드 사용하여 만들기
for i in range(97, 123):
    alpha.append(chr(i))

for i in range(len(S)):
    for k in range(len(alpha)):
        # baekjoon 의 경우 "o" 가 2개 이므로 마지막 "o"의 인덱스가 check배열에 들어감
        if check[k] != -1: # 동일 알파벳이 있는 경우를 피하기 위해 -1인지 체크.
                continue
        if S[i] == alpha[k]: # S의 소문자가 alpha 배열에 있는지 check.
            check[k] = i # 있다면 check[k]에 i의 인덱스를 할당->등장하는 위치 저장

print(*check, sep = ' ')