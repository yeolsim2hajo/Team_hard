# 조예지님 코드
def func(lst):
    for i in range(9): # 가로 검사
        if sum(lst[i]) != 45:
            return 0
    for i in range(9): # 세로 검사
        if sum([lst[x][i] for x in range(9)]) != 45:
            return 0
    arr = [0, 3, 6]
    d = [0, 1, 2]
    for i in arr:
        for j in arr:
            total = 0
            for k in d:
                for l in d:
                    total += lst[i+k][j+l]
            if total != 45:
                return 0
    return 1

t = int(input())
for i in range(t):
    lst = [list(map(int, input().split())) for _ in range(9)]
    result = func(lst)
    print(f'#{i+1} {result}')

# 어우야;; 내 코드와 비교해서 진짜 아예 다르네 원리는 같은데..
# 격자판 경우, 4중포문이지만, 내 코드보다 더 빠름(155ms vs 165ms) 흠...이건 간단해서 그러긴 한듯
# 격자판 direct이용한게 굿
# 쨋든, 훨씬 깔끔하다는 것.