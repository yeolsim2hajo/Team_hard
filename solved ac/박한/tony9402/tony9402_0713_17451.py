# 백준 17451 평행 우주

n = int(input())
lst = list(map(int, input().split()))
rst = 0
for i in range(n-1, -1, -1):
    if lst[i] <= rst:
        if rst % lst[i] != 0:
            rst = (rst//lst[i]+1)*lst[i]
    else:
        rst = lst[i]
print(rst)