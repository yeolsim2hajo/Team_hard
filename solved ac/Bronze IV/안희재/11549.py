a = int(input())
b = list(map(int,input().split()))

cnt = 0
for i in b:
    if i == a:
        cnt +=1

print(cnt)