# 백준 17175 피보나치는 지겨웡~

n = int(input())
lst = [0]*(n+1)
lst[0]
if n < 2:
    print(1)
else:
    lst[0], lst[1] = 1, 1
    for i in range(2, n+1):
        lst[i] = lst[i-1] + lst[i-2] + 1
    print(lst[n]%1000000007)