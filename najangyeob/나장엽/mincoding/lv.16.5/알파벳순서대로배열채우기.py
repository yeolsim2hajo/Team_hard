x, y = map(int, input().split())
# 숫자를 chr함수를 통해 알파벳으로 변환할것임. +1 씩 증가시키면 A ~ R까지 입력가능.
A = 65

alpha=[]
# 빈 2차원 리스트 생성
for i in range(6):
    temp=[]
    for j in range(3):
        temp.append('')
    alpha.append(temp)


# 빈 2차원 alpha 리스트에 알파벳 추가하기
for k in range(2, -1, -1):
    for a in range(5, -1, -1):
        alpha[a][k] = chr(A)
        A+=1

print(alpha[x][y])