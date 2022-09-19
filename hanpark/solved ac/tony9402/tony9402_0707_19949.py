# 백준 19949 영재의 시험

lst = list(map(int, input().split()))
lst1 = []
ans = 0

def dfs(depth):
    global ans
    if depth == 10:
        rst = 0
        for i in range(10):
            if lst1[i] == lst[i]:
                rst += 1
        if rst >= 5:
            ans += 1
        return ;
    for n in range(1, 6):
        if depth > 1 and lst1[depth-2] == lst1[depth-1] == n:
            continue
        lst1.append(n)
        dfs(depth+1)
        lst1.pop()

dfs(0)
print(ans)