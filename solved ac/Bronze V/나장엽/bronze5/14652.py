# n, m 은 관중석 크기 n*m 
# k 는 관중석 번호(index)
n, m, k = map(int, input().split())

place = []

# 관중석 만드는 코드 
for i in range(n):
    for j in range(m):
        place.append([i, j])


for str in place[k]:
    print(str, end=' ')
# --------------------------------------------메모리 초과

# --------------------------------------------단순사칙연산...ㅗ
# n, m, k = map(int, input().split())
# print(k // m, k % m)
