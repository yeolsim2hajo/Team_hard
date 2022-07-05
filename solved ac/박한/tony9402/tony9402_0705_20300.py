# 백준 20300 서강근육맨

n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
ans = 0
if n%2 == 1:
    ans = lst[0]
    for i in range(n//2):
        rst = lst[1+i] + lst[-i-1]
        if rst > ans:
            ans = rst
else:
    for i in range(n//2):
        rst = lst[i] + lst[-i-1]
        if rst > ans:
            ans = rst
print(ans)

# 개수가 짝수인 경우에는 최소 n번째 값과 최대 n번째 값의 합이 가장 큰 경우
# 개수가 홀수인 경우에는 최대값을 따로 빼고, 최소 n번째 값과 최대 n+1번째 값의 합이 가장 큰 경우