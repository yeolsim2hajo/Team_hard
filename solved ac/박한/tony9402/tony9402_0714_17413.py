# 백준 17413 단어 뒤집기 2

lst = list(input())
n = len(lst)
ans = []
rst = 0
while rst < n:
    if lst[rst] == '<':
        for i in range(rst+1, n):
            if lst[i] == '>':
                ans += lst[rst : i+1]
                rst = i
                break
    elif lst[rst] == ' ':
        ans.append(lst[rst])
    else:
        check = 0
        for i in range(rst+1, n):
            if lst[i] == '<' or lst[i] == ' ':
                lst1 = lst[rst : i]
                lst1.reverse()
                ans += lst1
                rst = i-1
                check = 1
                break
        if check == 1:
            rst += 1
            continue
        lst1 = lst[rst : n]
        lst1.reverse()
        ans += lst1
        rst = n-1
    rst += 1
for i in range(n):
    print(ans[i], end="")