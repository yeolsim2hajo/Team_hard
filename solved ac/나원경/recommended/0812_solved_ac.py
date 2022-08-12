#1547 공
M = int(input())
now = '1'
for _ in range(M):
    cup1, cup2 = input().split()
    if cup1 == now:
        now = cup2
    elif cup2 == now:
        now = cup1
print(now)