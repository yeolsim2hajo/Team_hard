vect = ['B','T','K','I','G','Z']
target = input().split()

cnt = 0
for i in vect:
    for j in target:
        if j == i:
            cnt +=1
print(cnt)