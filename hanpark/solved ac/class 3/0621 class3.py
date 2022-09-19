# 백준 class 3++ 11399 ATM

n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
rst = 0
for i in range(n):
    rst += (i+1)*lst[i]
print(rst)