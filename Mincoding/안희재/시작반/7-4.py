num = map(int,input().split())

arr = []
for i in num:
    arr.append(i)

cnt = 0
for i in arr:
    if 3 <= i <= 7:
        cnt +=1

print(cnt)