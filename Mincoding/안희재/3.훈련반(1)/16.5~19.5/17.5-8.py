arr = [[3,55,42], [-5,-9,-10]]
pix = []

for i in range(2):
    lst = list(map(int, input().split()))
    pix.append(lst)

# 아 arr을 1차원 배열로 푸는건 아닌것 같음 그렇다고 4중 포문? 에바참치..
# 어 아니면 이중포문 2개로? 1행끼리 비교, 2행끼리 비교 이렇게
# ㄴㄴ 그냥 함수 쓰는게 훨씬 나음

def find_num(num):
    result = 0
    for i in range(2):
        for j in range(3):
            if num == arr[i][j]:
                result = 1
    return result

for i in range(2):
    for j in range(2):
        if find_num(pix[i][j]):
            pix[i][j] = 'Y'
        else:
            pix[i][j] = 'N'

print(pix[0][0], pix[0][1])
print(pix[1][0], pix[1][1])