a = int(input())
lst = list(map(int,input().split()))

cnt = 0
for ele in lst:
    if ele == a:
        cnt += 1

print(cnt)